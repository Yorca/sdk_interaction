package org.example.custom;

import java.util.*;

import soot.*;
import soot.jimple.toolkits.callgraph.*;
import soot.jimple.*;
import soot.jimple.infoflow.InfoflowManager;
import soot.jimple.infoflow.android.InfoflowAndroidConfiguration;
import soot.jimple.infoflow.android.callbacks.AndroidCallbackDefinition;
import soot.jimple.infoflow.android.resources.controls.AndroidLayoutControl;
import soot.jimple.infoflow.android.source.AccessPathBasedSourceSinkManager;
import soot.jimple.infoflow.data.AccessPath;
import soot.jimple.infoflow.data.AccessPath.ArrayTaintType;
import soot.jimple.infoflow.entryPointCreators.SimulatedCodeElementTag;
import soot.jimple.infoflow.sourcesSinks.definitions.AccessPathTuple;
import soot.jimple.infoflow.sourcesSinks.definitions.FieldSourceSinkDefinition;
import soot.jimple.infoflow.sourcesSinks.definitions.ISourceSinkDefinition;
import soot.jimple.infoflow.sourcesSinks.definitions.StatementSourceSinkDefinition;
import soot.jimple.infoflow.sourcesSinks.manager.SinkInfo;
import soot.jimple.infoflow.sourcesSinks.manager.SourceInfo;
import soot.toolkits.scalar.Pair;
import org.javatuples.Triplet;

public class MyAccessPathBasedSourceSinkManager extends AccessPathBasedSourceSinkManager {
	private Map<Pair<String, String>, Set<String>> stmtSourceSigsMap;

	// use for one source at a time
	private Set<Triplet<String, String, String>> stmtSourceSigsSet;
	private Iterator<Triplet<String, String, String>> stmtSourceSigsIterator;
	private Triplet<String, String, String> currentStmtSourceSigs;

	public MyAccessPathBasedSourceSinkManager(Collection<? extends ISourceSinkDefinition> sources,
			Collection<? extends ISourceSinkDefinition> sinks, Set<AndroidCallbackDefinition> callbackMethods,
			InfoflowAndroidConfiguration config, Map<Integer, AndroidLayoutControl> layoutControls,
			Map<Pair<String, String>, Set<String>> stmtSourceSigsMap) {
		super(sources, sinks, callbackMethods, config, layoutControls);
		this.stmtSourceSigsMap = stmtSourceSigsMap;

		System.out.println("Looking for stmt sources");
		this.stmtSourceSigsSet = new HashSet<>();

		if (Scene.v().hasCallGraph()) {
			ReachableMethods reachableMethods = Scene.v().getReachableMethods();
			reachableMethods.update();
			for (Iterator<MethodOrMethodContext> iter = reachableMethods.listener(); iter.hasNext();) {
				SootMethod sm = iter.next().method();

				Pair<String, String> methodKey = new Pair<String, String>(sm.getDeclaringClass().getName(),
						sm.getSubSignature());
				if (this.stmtSourceSigsMap.containsKey(methodKey)) {
					for (String stmtSig : this.stmtSourceSigsMap.get(methodKey)) {
						stmtSourceSigsSet.add(Triplet.with(methodKey.getO1(), methodKey.getO2(), stmtSig));
						System.out.println("Adding source: " + methodKey + " " + stmtSig);
					}
				}
			}
		}
	}

	private boolean isStmtSourceAll(Stmt sCallSite, InfoflowManager manager) {
		SootMethod method = manager.getICFG().getMethodOf(sCallSite);

		if (method != null) {
			Pair<String, String> methodKey = new Pair<String, String>(method.getDeclaringClass().getName(),
					method.getSubSignature());

			if (this.stmtSourceSigsMap.containsKey(methodKey)) {
				for (String stmtSig : this.stmtSourceSigsMap.get(methodKey)) {
					if (sCallSite.toString().contains(stmtSig)) {
						System.out.println("isStmtSourceAll: " + sCallSite);
						System.out.println("oneSourceAtATime: " + oneSourceAtATime);
						return true;
					}
				}
			}
		}
		return false;
	}

	private boolean isStmtSourceOneAtATime(Stmt sCallSite, InfoflowManager manager) {
		SootMethod method = manager.getICFG().getMethodOf(sCallSite);

		if (method != null && 
				method.getDeclaringClass().getName().equals(this.currentStmtSourceSigs.getValue0()) && 
				method.getSubSignature().equals(this.currentStmtSourceSigs.getValue1()) && 
				sCallSite.toString().contains(this.currentStmtSourceSigs.getValue2())) {
			System.out.println("isStmtSourceOneAtATime: " + sCallSite + " currentStmtSourceSigs" + this.currentStmtSourceSigs);
			return true;
		}

		return false;
	}

	@Override
	public SourceInfo getSourceInfo(Stmt sCallSite, InfoflowManager manager) {
		SourceInfo ret = super.getSourceInfo(sCallSite, manager);
		SootMethod method = manager.getICFG().getMethodOf(sCallSite);

		if (!oneSourceAtATime) {
			if (!isStmtSourceAll(sCallSite, manager)) {
				return ret;
			} else {}
		} else {
			if (osaatType == SourceType.MethodCall) {
				return ret;
			} else {
				if (!isStmtSourceOneAtATime(sCallSite, manager)) {
					return ret;
				} else {}
			}
		}

		System.out.println("additional source " + sCallSite.toString() + " at " + method.getSignature());

		try {
			if (sCallSite instanceof DefinitionStmt) {
				Value lhs = ((DefinitionStmt) sCallSite).getLeftOp();
				if (lhs instanceof FieldRef) {
					SootField lhsField = ((FieldRef) lhs).getField();

					HashSet<ISourceSinkDefinition> defs = new HashSet<>();
					ISourceSinkDefinition def = new FieldSourceSinkDefinition(lhsField.getSignature());
					defs.add(def);
					this.sourceFields.put(lhsField, def);
					SourceInfo fret = new SourceInfo(createSourceInfoPairs(sCallSite, manager, defs));
					return fret;
				} else {
					Local local = null;
					for (ValueBox vb : sCallSite.getUseAndDefBoxes()) {
						if (vb.getValue() instanceof Local) {
							local = (Local) vb.getValue();
							break;
						}
					}

					if (local != null) {
						Set<AccessPathTuple> apTuple = new HashSet<AccessPathTuple>();
						apTuple.add(AccessPathTuple.create(true, false));
						ISourceSinkDefinition def = new StatementSourceSinkDefinition(sCallSite, local, apTuple);
						HashSet<ISourceSinkDefinition> defs = new HashSet<>();
						defs.add(def);
						this.sourceStatements.put(sCallSite, def);
						SourceInfo fret = new SourceInfo(createSourceInfoPairs(sCallSite, manager, defs));
						return fret;
					}
				}
			} else if (sCallSite.containsInvokeExpr()) {
				if (sCallSite.getInvokeExpr() instanceof InstanceInvokeExpr) {
					Local lLocal = (Local) (((InstanceInvokeExpr) sCallSite.getInvokeExpr()).getBase());
					Set<AccessPathTuple> apTuple = new HashSet<AccessPathTuple>();
					apTuple.add(AccessPathTuple.create(true, false));
					ISourceSinkDefinition def = new StatementSourceSinkDefinition(sCallSite, lLocal, apTuple);
					HashSet<ISourceSinkDefinition> defs = new HashSet<>();
					defs.add(def);
					this.sourceStatements.put(sCallSite, def);
					SourceInfo fret = new SourceInfo(createSourceInfoPairs(sCallSite, manager, defs));
					return fret;
				}
			}
		} catch (Exception e) {
			e.printStackTrace();
		}

		return null;
	}

	@Override
	public SinkInfo getSinkInfo(Stmt sCallSite, InfoflowManager manager, AccessPath sourceAccessPath) {
		return super.getSinkInfo(sCallSite, manager, sourceAccessPath);
	}

	@Override
	public void resetCurrentSource() {
		super.resetCurrentSource();
	}

	public void nextSource() {
		if (osaatType == SourceType.MethodCall) {
			currentSource = this.osaatIterator.next();
			// FlowDroid will use call back methods as sources as well
			// so even though in source APIs are specified, it will analyze a number of call
			// back APIs as source.
			System.out.println("Moving on to next method source: " + currentSource);
		} else {
			this.currentStmtSourceSigs = this.stmtSourceSigsIterator.next();
			
			/*remove the original source definitions in the oneSourceAtATime mode*/
			this.sourceStatements.clear();
			this.sourceFields.clear();
			System.out.println("Moving on to next stmt source: " + this.currentStmtSourceSigs);
		}
	}

	public boolean hasNextSource() {
		if (osaatType == SourceType.MethodCall) {
			if (this.osaatIterator.hasNext())
				return true;
			else {
				this.osaatType = SourceType.NoSource;
				this.stmtSourceSigsIterator = this.stmtSourceSigsSet.iterator();
				return this.hasNextSource();
			}
		} else {
			return this.stmtSourceSigsIterator.hasNext();
		}
	}
}
