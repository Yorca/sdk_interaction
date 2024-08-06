package org.example.check;

import java.io.*;
import java.util.*;
import java.util.logging.Logger;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import soot.jimple.*;
import soot.toolkits.graph.*;
import soot.*;
import soot.options.Options;
import soot.jimple.toolkits.callgraph.*;
import soot.util.*;

import org.example.util.PrivacyAPISummary;
import org.example.util.Utils;
import org.example.util.DirectedGraph;
import org.example.util.DirectedGraph.Node;
import org.example.xq.Globals;
import org.example.xq.CustomSetupApplication;
import org.json.JSONArray;
import org.json.JSONObject;
import org.xmlpull.v1.XmlPullParserException;
import soot.*;
import soot.jimple.DefinitionStmt;
import soot.jimple.FieldRef;
import soot.jimple.Stmt;
import soot.jimple.IfStmt;
import soot.jimple.SwitchStmt;
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
import soot.jimple.infoflow.methodSummary.taintWrappers.SummaryTaintWrapper;
import soot.jimple.infoflow.methodSummary.data.provider.LazySummaryProvider;
import soot.jimple.infoflow.data.AccessPath;
import soot.toolkits.scalar.Pair;
import soot.jimple.infoflow.solver.cfg.IInfoflowCFG.UnitContainer;

import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.util.concurrent.ConcurrentHashMap;
import soot.jimple.infoflow.android.SetupApplication;

import static org.example.util.PrivacyAPISummary.*;

/*
 * Tracking privacy APIs for dynamic analysis.
 */
public class PrivacyAPITracking {
	private static final Logger LOGGER = Logger.getLogger(PrivacyAPITracking.class.getName());
	private static final DirectedGraph forwardGraph = new DirectedGraph("forward.dummy.id", "forward.dummy.stmt",
			"forward.dummy.method");
	private static final DirectedGraph backwardGraph = new DirectedGraph("backward.dummy.id", "backward.dummy.stmt",
			"backward.dummy.method");

	public static SetupApplication setupFlowdroid(Map<Pair<String, String>, Set<String>> stmtSourceSigs,
			String sourceSinkFilePath, boolean isBackward) throws XmlPullParserException, IOException {
		G.reset();

		File file = new File(Globals.APK_PATH);
		String apkPath = file.getAbsolutePath();

		final InfoflowAndroidConfiguration config = new InfoflowAndroidConfiguration();
		config.getAnalysisFileConfig().setTargetAPKFile(apkPath);
		config.getAnalysisFileConfig().setAndroidPlatformDir(Globals.FRAMEWORK_DIR);
		config.setMergeDexFiles(true);
		config.setWriteOutputFiles(true);

		config.setImplicitFlowMode(ImplicitFlowMode.AllImplicitFlows);
		if (isBackward) {
			config.setDataFlowDirection(DataFlowDirection.Backwards);
		}

		config.getAnalysisFileConfig().setSourceSinkFile(sourceSinkFilePath);
		config.getCallbackConfig().setEnableCallbacks(true);
		config.setDataFlowTimeout(5400);
		// config.setCodeEliminationMode(CodeEliminationMode.NoCodeElimination);
		// config.getAccessPathConfiguration().setAccessPathLength(5);

		config.setCallgraphAlgorithm(InfoflowConfiguration.CallgraphAlgorithm.VTA);

		Options.v().set_output_format(Options.output_format_jimple);
		Options.v().set_output_dir(Globals.JIMPLE_SUBDIR);
		PackManager.v().writeOutput();
		Options.v().set_whole_program(true);
		Options.v().set_verbose(true);
		Options.v().set_process_multiple_dex(true);
		Options.v().set_allow_phantom_refs(true);

		Options.v().set_exclude(Arrays.asList(new String[] { "androidx.", "android.", "com.android.", "java.", "javax.",
				"kotlin.", "sun.", "org.apache.", "soot.", "javax.servlet." }));
		Options.v().set_no_bodies_for_excluded(true);
		Scene.v().loadNecessaryClasses();

		SetupApplication app = new CustomSetupApplication(config, new HashSet<>(), new HashSet<>(), stmtSourceSigs);

		try {
			SummaryTaintWrapper summaryWrapper = new SummaryTaintWrapper(new LazySummaryProvider("summariesManual"));
			EasyTaintWrapper easyTaintWrapper = EasyTaintWrapper.getDefault();
			summaryWrapper.setFallbackTaintWrapper(easyTaintWrapper);
			app.setTaintWrapper(summaryWrapper);
		} catch (Exception e) {
			e.printStackTrace();
		}

		LOGGER.info("setupFlowdroid Finished!");

		return app;
	}

	public static Map<Pair<String, String>, Set<String>> getSourceParamsMapForForward() {
		Map<Pair<String, String>, Set<String>> stmtSourceSigs = new HashMap<>();
		String parameter_str = ":= @parameter%d:"; // %d is a placeholder for the index of parameter.
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
			FileWriter fileWriter = new FileWriter(Globals.SRC_SINK_FILE_XML);
			PrintWriter printWriter = new PrintWriter(fileWriter);
			printWriter.printf("%s\n", Utils.HEAD_XML);
			for (String sc : Utils.DUMMY_SOURCE_XML) {
				printWriter.printf("%s\n", sc);
			}

			for (Map.Entry<String, List<APIDescriptor>> sdk : sdks.entrySet()) {
				String sdk_name = sdk.getKey();
				List<APIDescriptor> apiDescriptors = sdk.getValue();

				for (APIDescriptor apiDescriptor : apiDescriptors) {
					String clazzNm = apiDescriptor.apiClazzName;
					String methodNm = apiDescriptor.apiMethodName;
					if (null == clazzNm || null == methodNm || apiDescriptor.ppArgs == null) {
						continue;
					}

					try {
						List<SootMethod> methods = Utils.findMethod(clazzNm, methodNm);
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
									sourceParams.add(String.format("<param index=\"%d\" description=\"Value\">\n"
											+ "        <accessPath isSource=\"false\" isSink=\"true\" />\n"
											+ "    </param>", paramIndex));
								}
							}

							if (sourceParams.size() < 1) {
								continue;
							}

							printWriter.printf("<method signature=\"%s: %s\">\n", clazzNm, short_sig);
							for (String param : sourceParams) {
								printWriter.printf("%s\n", param);
							}
							printWriter.printf("%s", "</method>\n");
						}
					} catch (Exception e) {
						e.printStackTrace();
					}
				}
			}

			printWriter.printf("%s\n", Utils.END_XML);
			printWriter.close();
		} catch (Exception e) {
			e.printStackTrace();
		}

		SetupApplication app = setupFlowdroid(new HashMap<>(), Globals.SRC_SINK_FILE_XML, true);

		app.setTaintPropagationHandler(new TaintPropagationHandler() {
			@Override
			public void notifyFlowIn(Unit stmt, Abstraction taint, InfoflowManager manager, FlowFunctionType type) {
			}

			protected boolean isActivityContextType(Type type) {
				if (type instanceof RefType) {
					RefType refType = (RefType) type;
					SootClass sootClass = refType.getSootClass();

					while (sootClass != null) {
						if (sootClass.getName().equals("android.content.Context")
								|| sootClass.getName().equals("android.app.Activity")) {
							return true;
						}

						if (sootClass.hasSuperclass()) {
							sootClass = sootClass.getSuperclass();
						} else {
							sootClass = null;
						}
					}
				}
				return false;
			}

			protected Set<Abstraction> filterByPropagationPathLength(Set<Abstraction> outgoing) {
				int MAX_PATH_LENGTH = 15;
				Set<Abstraction> newOutgoing = new HashSet<>();
				for (Abstraction abs : outgoing) {
					if (abs.getPathLength() > MAX_PATH_LENGTH) {
						continue;
					}

					if (isActivityContextType(abs.getAccessPath().getBaseType())) {
						//System.out.println("Ignore Abs: " + abs + " BaseType:" + abs.getAccessPath().getBaseType());
						continue;
					}

					newOutgoing.add(abs);
				}
				return newOutgoing;
			}

			@Override
			public Set<Abstraction> notifyFlowOut(Unit unit, Abstraction d1, Abstraction incoming,
					Set<Abstraction> outgoing, InfoflowManager manager, FlowFunctionType type) {
				Set<Abstraction> newOutgoing = filterByPropagationPathLength(outgoing);

				if (!(unit instanceof Stmt)) {
					return outgoing;
				}

				boolean isOfInterest = false;
				Stmt stmt = (Stmt) unit;
				SootMethod method = manager.getICFG().getMethodOf(stmt);

				if (!incoming.getAccessPath().isEmpty() && isDefAt(stmt, incoming.getAccessPath())) {
					isOfInterest = true;
				}

				isOfInterest = isOfInterest || newOutgoing.stream().anyMatch(
						item -> !item.equals(incoming) && !item.getAccessPath().equals(incoming.getAccessPath()));

				if (isOfInterest) {
					String parentNodeId = null;
					Abstraction pd = incoming;
					while (pd != null) {
						Stmt pdStmt = pd.getCurrentStmt();
						if (pdStmt != null && !pd.getAccessPath().isEmpty()) {
							SootMethod pdMethod = manager.getICFG().getMethodOf(pdStmt);
							String pdId = String.format("[%s] %s", pdMethod.getSignature(), pdStmt);
							if (backwardGraph.hasNode(pdId)) {
								parentNodeId = pdId;
								break;
							}
						}
						pd = pd.getPredecessor();
					}

					if (parentNodeId == null) {
						parentNodeId = backwardGraph.getRootId();
					}

					String currentNodeId = String.format("[%s] %s", method.getSignature(), stmt);
					backwardGraph.addNode(currentNodeId, stmt.toString(), method.getSignature());
					backwardGraph.addEdge(parentNodeId, currentNodeId, incoming.isImplicit());
					//System.out.println("Edge: " + parentNodeId + " --> " + currentNodeId);
				}

				return newOutgoing;
			}
		});

		app.runInfoflow();
		backwardGraph.printGraphFromRoot();

		LOGGER.info("runBackwardAnalysis ends!");
	}

	public void runForwardAnalysis() throws XmlPullParserException, IOException {
		Map<Pair<String, String>, Set<String>> stmtSourceSigs = getSourceParamsMapForForward();

		try {
			FileWriter fileWriter = new FileWriter(Globals.SRC_SINK_FILE);
			PrintWriter printWriter = new PrintWriter(fileWriter);
			for (String sc : Utils.ONCREATE_APIS) {
				printWriter.printf("%s -> _SINK_\n", sc);
			}
			printWriter.close();
		} catch (Exception e) {
			e.printStackTrace();
		}

		SetupApplication app = setupFlowdroid(stmtSourceSigs, Globals.SRC_SINK_FILE, false);

		app.setTaintPropagationHandler(new TaintPropagationHandler() {
			@Override
			public void notifyFlowIn(Unit stmt, Abstraction taint, InfoflowManager manager, FlowFunctionType type) {
			}
			
			protected boolean isActivityContextType(Type type) {
				if (type instanceof RefType) {
					RefType refType = (RefType) type;
					SootClass sootClass = refType.getSootClass();

					while (sootClass != null) {
						if (sootClass.getName().equals("android.content.Context")
								|| sootClass.getName().equals("android.app.Activity")) {
							return true;
						}

						if (sootClass.hasSuperclass()) {
							sootClass = sootClass.getSuperclass();
						} else {
							sootClass = null;
						}
					}
				}
				return false;
			}

			protected Set<Abstraction> filterByPropagationPathLength(Set<Abstraction> outgoing) {
				int MAX_PATH_LENGTH = 15;
				Set<Abstraction> newOutgoing = new HashSet<>();
				for (Abstraction abs : outgoing) {
					if (abs.getPathLength() > MAX_PATH_LENGTH) {
						continue;
					}
					
					if (isActivityContextType(abs.getAccessPath().getBaseType())) {
						//System.out.println("Ignore Abs: " + abs + " BaseType:" + abs.getAccessPath().getBaseType());
						continue;
					}
					
					newOutgoing.add(abs);
				}
				return newOutgoing;
			}

			@Override
			public Set<Abstraction> notifyFlowOut(Unit unit, Abstraction d1, Abstraction incoming,
					Set<Abstraction> outgoing, InfoflowManager manager, FlowFunctionType type) {
				Set<Abstraction> newOutgoing = filterByPropagationPathLength(outgoing);

				if (!(unit instanceof Stmt)) {
					return newOutgoing;
				}

				boolean isOfInterest = false;
				Stmt stmt = (Stmt) unit;
				SootMethod method = manager.getICFG().getMethodOf(stmt);
				if (isReadAt(stmt, incoming.getAccessPath())) {
					if (stmt.containsInvokeExpr()
							&& !stmt.getInvokeExpr().getMethod().getDeclaringClass().isApplicationClass()) {
						isOfInterest = true;
					}
				}
				isOfInterest = isOfInterest || newOutgoing.stream().anyMatch(
						item -> !item.equals(incoming) && !item.getAccessPath().equals(incoming.getAccessPath()));

				if (isOfInterest) {
					String parentNodeId = null;
					Abstraction pd = incoming;
					while (pd != null) {
						Stmt pdStmt = pd.getCurrentStmt();
						if (pdStmt != null && !pd.getAccessPath().isEmpty()) {
							SootMethod pdMethod = manager.getICFG().getMethodOf(pdStmt);
							String pdId = String.format("[%s] %s", pdMethod.getSignature(), pdStmt);
							if (forwardGraph.hasNode(pdId)) {
								parentNodeId = pdId;
								break;
							}
						}
						pd = pd.getPredecessor();
					}

					if (parentNodeId == null) {
						parentNodeId = forwardGraph.getRootId();
					}

					String currentNodeId = String.format("[%s] %s", method.getSignature(), stmt);
					forwardGraph.addNode(currentNodeId, stmt.toString(), method.getSignature());
					forwardGraph.addEdge(parentNodeId, currentNodeId, incoming.isImplicit());
				}

				return newOutgoing;
			}
		});

		app.runInfoflow();
		forwardGraph.printGraphFromRoot();
		LOGGER.info("runForwardAnalysis ends!");
	}

	/**
	 * Check whether the access path is wrote at unit.
	 *
	 * @param unit unit
	 * @param ap   access path
	 * @return true if ap is wrote at unit
	 */
	protected boolean isDefAt(Stmt stmt, AccessPath ap) {
		for (ValueBox box : stmt.getDefBoxes())
			if (box.getValue() == ap.getPlainValue()) {
				return true;
			}
		return false;
	}

	/**
	 * Check whether the access path is read at unit.
	 *
	 * @param unit unit
	 * @param ap   access path
	 * @return true if ap is read at unit
	 */
	protected boolean isReadAt(Stmt stmt, AccessPath ap) {
		if (stmt.containsInvokeExpr()) {
			for (Value argValue : stmt.getInvokeExpr().getArgs()) {
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

	protected void traverseAndPrintStatements(UnitGraph graph, Unit start, Unit end, boolean isForward) {
		Set<Unit> visited = new HashSet<>();
		Queue<Unit> queue = new LinkedList<>();
		queue.add(start);

		while (!queue.isEmpty()) {
			Unit current = queue.poll();
			if (!visited.add(current)) {
				continue;
			}

			System.out.println("ControlDeps: " + current);

			if (current.equals(end)) {
				break;
			}

			for (Unit succ : graph.getSuccsOf(current)) {
				if (!visited.contains(succ)) {
					queue.add(succ);
				}
			}
		}
	}
}
