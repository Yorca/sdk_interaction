package org.example.custom;

import java.io.IOException;
import java.util.ArrayList;
import java.util.Collection;
import java.util.List;
import java.util.Map;
import java.util.Set;

import org.xmlpull.v1.XmlPullParserException;
import soot.Scene;
import soot.SootClass;
import soot.SootMethod;
import soot.jimple.infoflow.android.InfoflowAndroidConfiguration;
import soot.jimple.infoflow.android.SetupApplication;
import soot.jimple.infoflow.android.callbacks.AndroidCallbackDefinition;
import soot.jimple.infoflow.android.resources.LayoutFileParser;
import soot.jimple.infoflow.android.source.AccessPathBasedSourceSinkManager;
import soot.jimple.infoflow.sourcesSinks.manager.ISourceSinkManager;
import soot.toolkits.scalar.Pair;

public class CustomSetupApplication extends SetupApplication {
	private Map<Pair<String, String>, Set<String>> stmtSourceSigs;
	private boolean oneSourceAtATime;

	public CustomSetupApplication(InfoflowAndroidConfiguration config,
			Map<Pair<String, String>, Set<String>> stmtSourceSigs, boolean oneSourceAtATime) {
		super(config);
		this.stmtSourceSigs = stmtSourceSigs;
		this.oneSourceAtATime = oneSourceAtATime;
	}

	@Override
	protected void constructCallgraphInternal() {
		// add dymmyMainMethod back
		List<SootMethod> entryPoints = new ArrayList<SootMethod>();
		entryPoints.addAll(Scene.v().getEntryPoints());

		// add additional entry points
		for (Pair<String, String> entry_item : Globals.ENTRY_POINTS) {
			try {
				SootClass c = Scene.v().forceResolve(entry_item.getO1(), SootClass.BODIES);
				c.setApplicationClass();
				Scene.v().loadNecessaryClasses();
				SootMethod m = c.getMethod(entry_item.getO2());
				entryPoints.add(m);
				System.out.println("Adding entry point " + entry_item);
			} catch (Exception e) {
				e.printStackTrace();
			}
		}

		Scene.v().setEntryPoints(entryPoints);

		try {
			super.constructCallgraphInternal();
		} catch (Exception e) {
			e.printStackTrace();
		}
	}

	@Override
	protected void parseAppResources() throws IOException, XmlPullParserException {
		try {
			super.parseAppResources();
		} catch (Exception e) {
			e.printStackTrace();
		}

		for (Pair<String, String> entry_item : Globals.ENTRY_POINTS) {
			try {
				SootClass c = Scene.v().forceResolve(entry_item.getO1(), SootClass.BODIES);
				c.setApplicationClass();
				Scene.v().loadNecessaryClasses();
				this.entrypoints.add(c);
			} catch (Exception e) {
				e.printStackTrace();
			}
		}
		entryPointCreator = new MyAndroidEntryPointCreator(this.manifest, this.entrypoints);
	}

	@Override
	protected ISourceSinkManager createSourceSinkManager(LayoutFileParser lfp,
			Set<AndroidCallbackDefinition> callbacks) {

		Map userControlsByID;
		Collection sources = this.sourceSinkProvider.getSources();
		Collection sinks = this.sourceSinkProvider.getSinks();
		InfoflowAndroidConfiguration infoflowAndroidConfiguration = this.config;
		if (lfp == null) {
			userControlsByID = null;
		} else {
			userControlsByID = lfp.getUserControlsByID();
		}
		AccessPathBasedSourceSinkManager sourceSinkManager2 = new MyAccessPathBasedSourceSinkManager(sources, sinks,
				callbacks, infoflowAndroidConfiguration, userControlsByID, this.stmtSourceSigs);

		sourceSinkManager2.setAppPackageName(this.manifest.getPackageName());
		sourceSinkManager2.setResourcePackages(this.resources.getPackages());
		sourceSinkManager2.setOneSourceAtATimeEnabled(this.oneSourceAtATime);
		return sourceSinkManager2;
	}
}
