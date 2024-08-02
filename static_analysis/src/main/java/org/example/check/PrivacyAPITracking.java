package org.example.check;

import java.io.*;
import java.util.*;
import java.util.logging.Logger;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

import org.example.util.PrivacyAPISummary;
import org.example.util.Utils;
import org.example.util.DirectedGraph;
import org.example.util.DirectedGraph.Node;
import org.example.util.DirectedGraph.Edge;
import org.example.xq.Globals;
import org.example.xq.MySetupApplication;
import org.json.JSONArray;
import org.json.JSONObject;
import org.xmlpull.v1.XmlPullParserException;
import soot.*;
import soot.jimple.DefinitionStmt;
import soot.jimple.FieldRef;
import soot.jimple.Stmt;
import soot.jimple.infoflow.InfoflowManager;
import soot.jimple.infoflow.android.InfoflowAndroidConfiguration;
import soot.jimple.infoflow.android.manifest.ProcessManifest;
import soot.jimple.infoflow.data.Abstraction;
import soot.jimple.infoflow.handlers.ResultsAvailableHandler;
import soot.jimple.infoflow.handlers.TaintPropagationHandler;
import soot.jimple.infoflow.results.InfoflowResults;
import soot.jimple.infoflow.results.ResultSinkInfo;
import soot.jimple.infoflow.results.ResultSourceInfo;
import soot.jimple.infoflow.solver.cfg.IInfoflowCFG;
import soot.jimple.infoflow.taintWrappers.EasyTaintWrapper;
import soot.jimple.infoflow.InfoflowConfiguration;
import soot.jimple.infoflow.InfoflowConfiguration.DataFlowSolver;
import soot.jimple.infoflow.InfoflowConfiguration.ImplicitFlowMode;
import soot.jimple.infoflow.InfoflowConfiguration.CodeEliminationMode;
import soot.jimple.infoflow.InfoflowConfiguration.DataFlowDirection;
import soot.options.Options;
import soot.jimple.infoflow.data.AccessPath;
import soot.toolkits.scalar.Pair;

import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.util.concurrent.ConcurrentHashMap;

import static org.example.util.PrivacyAPISummary.*;

/*
 * Tracking privacy APIs for dynamic analysis.
 */
public class PrivacyAPITracking {
	private static final Logger LOGGER = Logger.getLogger(PrivacyAPITracking.class.getName());
	private static final Map<String, DirectedGraph> forwardGraph = new ConcurrentHashMap<>();
	private static final Map<String, DirectedGraph> backwardGraph = new ConcurrentHashMap<>();

	public static MySetupApplication setupFlowdroid(Map<Pair<String, String>, 
			Set<String>> stmtSourceSigs, 
			String sourceSinkFilePath,
			boolean isBackward)
			throws XmlPullParserException, IOException {
		G.reset();

		File file = new File(Globals.APK_PATH);
		String apkPath = file.getAbsolutePath();

		final InfoflowAndroidConfiguration config = new InfoflowAndroidConfiguration();
		config.getAnalysisFileConfig().setTargetAPKFile(apkPath);
		config.getAnalysisFileConfig().setAndroidPlatformDir(Globals.FRAMEWORK_DIR);
		// To provide single view to analysis
		config.setMergeDexFiles(true);
		// Write analysis result to files for further analysis
		config.setWriteOutputFiles(true);
		//config.setImplicitFlowMode(ImplicitFlowMode.AllImplicitFlows);
		
		if (isBackward) {
			config.setDataFlowDirection(DataFlowDirection.Backwards);
		}
		
		config.getAnalysisFileConfig().setSourceSinkFile(sourceSinkFilePath);
		config.getCallbackConfig().setEnableCallbacks(true);
		config.setCallgraphAlgorithm(InfoflowConfiguration.CallgraphAlgorithm.VTA);
		config.setDataFlowTimeout(5400);
		config.setCodeEliminationMode(CodeEliminationMode.NoCodeElimination);
		config.getAccessPathConfiguration().setAccessPathLength(4);
		config.getPathConfiguration().setMaxPathLength(20);
		//config.getSolverConfiguration().setDataFlowSolver(DataFlowSolver.FlowInsensitive);
		//config.getSolverConfiguration().setDataFlowSolver(DataFlowSolver.SparseContextFlowSensitive);

		Options.v().set_output_format(Options.output_format_jimple);
		Options.v().set_output_dir(Globals.JIMPLE_SUBDIR);
		PackManager.v().writeOutput();
		Options.v().set_whole_program(true);
		Options.v().set_verbose(true);
		Options.v().set_process_multiple_dex(true);
		Options.v().set_allow_phantom_refs(true);
		List<String> excludePackagesList = Arrays.asList(new String[] { "androidx.*", "android.*", "com.android.*" });
		Options.v().set_exclude(excludePackagesList);
		Options.v().set_no_bodies_for_excluded(true);
		Scene.v().loadNecessaryClasses();

		// Using the Source custom code here:
		MySetupApplication app = new MySetupApplication(config, new HashSet<>(), new HashSet<>(), stmtSourceSigs);

		EasyTaintWrapper easyTaintWrapper = new EasyTaintWrapper("./EasyTaintWrapperSource.txt");
		app.setTaintWrapper(easyTaintWrapper);

		LOGGER.info("setupFlowdroid Finished!");

		return app;
	}

	public static Map<Pair<String, String>, Set<String>> getSourceParamsMapForForward() {
		Map<Pair<String, String>, Set<String>> stmtSourceSigs = new HashMap<>();
		String parameter_str = ":= @parameter%d:"; // %d is a placeholder for the index of parameter.
//		PrivacyAPISummary.initTestCases();
		System.out.println(sdks);
		// Looping through each sdk in the sdks
		for (Map.Entry<String, List<APIDescriptor>> sdk : sdks.entrySet()) {
			String sdk_name = sdk.getKey();
			List<APIDescriptor> apiDescriptors = sdk.getValue();

			Utils.LOGGER.info("SDK: " + sdk_name); // Printing the key (SDK name)

			// Looping through each APIDescriptor in the list
			for (APIDescriptor apiDescriptor : apiDescriptors) {
				String clazzNm = apiDescriptor.apiClazzName;
				String methodNm = apiDescriptor.apiMethodName;
				// if current class name or method name is null, continue to next api.
				if (null == clazzNm || null == methodNm || apiDescriptor.ppArgs == null) {
					continue;
				}

				try {
					List<SootMethod> methods = Utils.findMethod(clazzNm, methodNm);
					// if current api can't be found in the apk, continue to next api
					if (null == methods) {
						continue;
					}

					for (SootMethod method : methods) {
						String short_sig = method.getSubSignature();

						// Checking if any privacy preserving parameter index is greater than the
						// method's parameter count.
						boolean notMatch = apiDescriptor.ppArgs.entrySet().stream()
								.anyMatch(ppArg -> method.getParameterCount() < (ppArg.getKey() + 1));
						// If so, continue to next overload method.
						if (notMatch)
							continue;

						Set<String> sourceParams = new HashSet<String>();
						for (Integer paramIndex : apiDescriptor.ppArgs.keySet()) {
							if (Utils.isInterestingTypes(method.getParameterType(paramIndex))) {
								// Why do we check isInterestingTypes here?
								// The input Priv_impl.json defines APIs based on a tuple (class, methodname);
								// this becomes a problem when a method has multiple implementations where the
								// privacy parameters are not in the specified index, leading to error tracking
								// of privacy parameters.
								sourceParams.add(String.format(parameter_str, paramIndex));
							}
						}

						if (sourceParams.size() < 1) {
							continue;
						}

						// Otherwise, add the method and the params index set into the stmtSourceSigs.
						stmtSourceSigs.put(new Pair<>(clazzNm, short_sig), sourceParams);
					}
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		}

		Utils.LOGGER.info("The sources in stmtSourceSigs:>>");
		// Looping through each entry in the stmtSourceSigs map
		for (Map.Entry<Pair<String, String>, Set<String>> entry : stmtSourceSigs.entrySet()) {
			Pair<String, String> pairKey = entry.getKey();
			Set<String> values = entry.getValue();

			// Printing the key and values of each entry
			Utils.LOGGER.info("Key: (" + pairKey.getO1() + ", " + pairKey.getO2() + ")");
			Utils.LOGGER.info("Values: " + values);
		}
		Utils.LOGGER.info("getSourceParamsMapForForward() finish.");

		return stmtSourceSigs;
	}

	public void runBackwardAnalysis() throws XmlPullParserException, IOException {
		try {
			FileWriter fileWriter = new FileWriter(Globals.SRC_SINK_FILE);
			PrintWriter printWriter = new PrintWriter(fileWriter);
			for (String sc : Utils.SP_APIS) {
				printWriter.printf("%s -> _SOURCE_\n", sc);
			}
			
			for (String sc : Utils.NETWORK_APIS) {
				printWriter.printf("%s -> _SOURCE_\n", sc);
			}
			
			for (Map.Entry<String, List<APIDescriptor>> sdk : sdks.entrySet()) {
				List<APIDescriptor> apiDescriptors = sdk.getValue();
				
				// Looping through each APIDescriptor in the list
				for (APIDescriptor apiDescriptor : apiDescriptors) {
					String clazzNm = apiDescriptor.apiClazzName;
					String methodNm = apiDescriptor.apiMethodName;
					// if current class name or method name is null, continue to next api.
					if (null == clazzNm || null == methodNm || apiDescriptor.ppArgs == null) {
						continue;
					}

					try {
						List<SootMethod> methods = Utils.findMethod(clazzNm, methodNm);
						// if current api can't be found in the apk, continue to next api
						if (null == methods) {
							continue;
						}

						for (SootMethod method : methods) {
							String short_sig = method.getSubSignature();

							// Checking if any privacy preserving parameter index is greater than the
							// method's parameter count.
							boolean notMatch = apiDescriptor.ppArgs.entrySet().stream()
									.anyMatch(ppArg -> method.getParameterCount() < (ppArg.getKey() + 1));
							// If so, continue to next overload method.
							if (notMatch)
								continue;
							
							printWriter.printf("%s -> _SINK_\n", method.getSignature());
						}
					} catch (Exception e) {
						e.printStackTrace();
					}
				}
			}
			
			printWriter.close();
		} catch (Exception e) {
			e.printStackTrace();
		}
		
		MySetupApplication app = setupFlowdroid(new HashMap<>(), Globals.SRC_SINK_FILE, true);
		
		app.setTaintPropagationHandler(new TaintPropagationHandler() {
			@Override
			public void notifyFlowIn(Unit stmt, Abstraction taint, InfoflowManager manager, FlowFunctionType type) {
			}

			@Override
			public Set<Abstraction> notifyFlowOut(Unit unit, Abstraction d1, Abstraction incoming,
					Set<Abstraction> outgoing, InfoflowManager manager, FlowFunctionType type) {
                                if (!(unit instanceof Stmt)) {
                                        return outgoing;
                                }

				Stmt stmt = (Stmt) unit;
				SootMethod method = manager.getICFG().getMethodOf(stmt);
				if (method.getDeclaringClass().getName().contains("dummyMainClass")) {
					return new HashSet<>();
				}

				System.out.println("notifyFlowOut: " + stmt + " in method: " + method);
				System.out.println("incoming: " + incoming.getAccessPath());
				for (Abstraction abs : outgoing) {
					System.out.println("outgoing: " + abs.getAccessPath());
				}

                                if (!isReadAt(stmt, incoming.getAccessPath())) {
                                        return outgoing;
                                }

                                for (Abstraction abs : outgoing) {
                                        Abstraction rootAbs = abs;
                                        while (rootAbs.getPredecessor() != null) {
                                                rootAbs = rootAbs.getPredecessor();
                                        }

                                        Stmt rootStmt = rootAbs.getCurrentStmt();
                                        if (rootStmt != null) {
                                                SootMethod rootMethod = manager.getICFG().getMethodOf(rootStmt);
                                                String rootId = String.format("[%s] %s", rootMethod.getSignature(), rootStmt);
                                                DirectedGraph directedGraph = backwardGraph.get(rootId);
                                                if (directedGraph == null) {
                                                        directedGraph = new DirectedGraph(rootId, rootStmt.toString(), rootMethod.getSignature());
                                                        backwardGraph.put(rootId, directedGraph);
                                                }

                                                String childNodeId = null;
                                                Object childProperty = null;
                                                if (abs.equals(incoming)) {
                                                        SootMethod curMethod = manager.getICFG().getMethodOf(stmt);
                                                        if (stmt.containsInvokeExpr() && !stmt.getInvokeExpr().getMethod().getDeclaringClass().isApplicationClass()) {
                                                                childNodeId = String.format("[%s] %s",curMethod.getSignature(), stmt);
                                                                childProperty = Boolean.valueOf(false);
                                                                directedGraph.addNode(childNodeId, stmt.toString(), curMethod.getSignature());
                                                        }
                                                }
                                                Abstraction pd = abs;
                                                while (pd != null) {
                                                        Stmt pdStmt = pd.getCurrentStmt();
                                                        if (pdStmt != null) {
                                                                SootMethod pdMethod = manager.getICFG().getMethodOf(pdStmt);
                                                                String pdNodeId = String.format("[%s] %s", pdMethod.getSignature(), pdStmt);
                                                                directedGraph.addNode(pdNodeId, pdStmt.toString(), pdMethod.getSignature());
                                                                if (childNodeId != null) {
                                                                        directedGraph.addEdge(pdNodeId, childNodeId, childProperty);
                                                                }
                                                                childNodeId = pdNodeId;
                                                                childProperty = Boolean.valueOf(pd.isImplicit());
                                                        }
                                                        pd = pd.getPredecessor();
                                                }
                                        }
                                }
                                return outgoing;
			}
		});

		app.runInfoflow();
		
		for (Map.Entry<String, DirectedGraph> entry : backwardGraph.entrySet()) {
			entry.getValue().printGraphFromRoot();
		}

		LOGGER.info("runBackwardAnalysis ends!");
		
	}
	
	public void runForwardAnalysis() throws XmlPullParserException, IOException {
		// Set up and launch Flowdroid analysis with custom modifications
		// Using MySetupApplication to generate the returned SetupApplication.
		Map<Pair<String, String>, Set<String>> stmtSourceSigs = getSourceParamsMapForForward();
		
		try {
			FileWriter fileWriter = new FileWriter(Globals.SRC_SINK_FILE);
			PrintWriter printWriter = new PrintWriter(fileWriter);
			for (String sc : Utils.ONCREATE_APIS) {
				printWriter.printf("%s -> _SINK_\n", sc);
			}
			
			//for (String sc : Utils.NETWORK_APIS) {
			//	printWriter.printf("%s -> _SINK_\n", sc);
			//}
			printWriter.close();
		} catch (Exception e) {
			e.printStackTrace();
		}
		
		MySetupApplication app = setupFlowdroid(stmtSourceSigs, Globals.SRC_SINK_FILE, false);

		app.setTaintPropagationHandler(new TaintPropagationHandler() {
			@Override
			public void notifyFlowIn(Unit stmt, Abstraction taint, InfoflowManager manager, FlowFunctionType type) {
				// Check whether any use matches the incoming taint
				//if (stmt.toString().contains("putBoolean")) {
				//	SootMethod method = manager.getICFG().getMethodOf(stmt);
				//	System.out.println("notifyFlowIn: " + stmt + " accessPathLength: " + taint.getAccessPath().getFragmentCount() + " " + taint.getAccessPath() + " " + isReadAt(stmt, taint.getAccessPath()) + " " + method);
				//}
				//if (manager.getSourceSinkManager().getSinkInfo((Stmt) stmt, manager, taint.getAccessPath()) != null) {
				//	System.out.println("notifyFlowIn - sink: " + stmt);
				//}
			}

			@Override
			public Set<Abstraction> notifyFlowOut(Unit unit, Abstraction d1, Abstraction incoming,
					Set<Abstraction> outgoing, InfoflowManager manager, FlowFunctionType type) {
				if (!(unit instanceof Stmt)) {
					return outgoing;
				}

				Stmt stmt = (Stmt) unit;

                                SootMethod method = manager.getICFG().getMethodOf(stmt);
                                if (method.getDeclaringClass().getName().contains("dummyMainClass")) {
                                        return new HashSet<>();
                                }

				if (!isReadAt(stmt, incoming.getAccessPath())) {
					return outgoing;
				}

				for (Abstraction abs : outgoing) {
					Abstraction rootAbs = abs;
					while (rootAbs.getPredecessor() != null) {
						rootAbs = rootAbs.getPredecessor();
					}

					Stmt rootStmt = rootAbs.getCurrentStmt();
					if (rootStmt != null) {
						SootMethod rootMethod = manager.getICFG().getMethodOf(rootStmt);
    						String rootId = String.format("[%s] %s", rootMethod.getSignature(), rootStmt);
						DirectedGraph directedGraph = forwardGraph.get(rootId);
						if (directedGraph == null) {
							directedGraph = new DirectedGraph(rootId, rootStmt.toString(), rootMethod.getSignature());
							forwardGraph.put(rootId, directedGraph);
						}

						String childNodeId = null;
						Object childProperty = null;
						if (abs.equals(incoming)) {
                                                	SootMethod curMethod = manager.getICFG().getMethodOf(stmt);
							if (stmt.containsInvokeExpr() && !stmt.getInvokeExpr().getMethod().getDeclaringClass().isApplicationClass()) {
                                                        	childNodeId = String.format("[%s] %s",curMethod.getSignature(), stmt);
								childProperty = Boolean.valueOf(false);
                                                        	directedGraph.addNode(childNodeId, stmt.toString(), curMethod.getSignature());
                                                	}
                                        	}

						Abstraction pd = abs;
						while (pd != null) {
							Stmt pdStmt = pd.getCurrentStmt();
							if (pdStmt != null) {
								SootMethod pdMethod = manager.getICFG().getMethodOf(pdStmt);
								String pdNodeId = String.format("[%s] %s", pdMethod.getSignature(), pdStmt);
								directedGraph.addNode(pdNodeId, pdStmt.toString(), pdMethod.getSignature());
								if (childNodeId != null) {
									directedGraph.addEdge(pdNodeId, childNodeId, childProperty);
								}
								childNodeId = pdNodeId;
								childProperty = Boolean.valueOf(pd.isImplicit());
							}
							pd = pd.getPredecessor();
						}
					}
				}
				return outgoing;
			}
		});

		app.runInfoflow();
		
        	for (Map.Entry<String, DirectedGraph> entry : forwardGraph.entrySet()) {
        		entry.getValue().printGraphFromRoot();
        	}

		LOGGER.info("runForwardAnalysis ends!");
	}

	/**
	 * Check whether the access path is read at unit.
	 *
	 * @param unit unit
	 * @param ap access path
	 * @return true if ap is read at unit
	 */
	protected boolean isReadAt(Stmt stmt, AccessPath ap) {
		if (stmt.containsInvokeExpr()) {
			for (Value argValue: stmt.getInvokeExpr().getArgs()) {
				if (argValue == ap.getPlainValue())
					return true;
			}
		} else {
			for (ValueBox box : stmt.getUseBoxes())
				if (box.getValue() == ap.getPlainValue())
					return true;
		}
		return false;
	}
}
