package org.example;

import java.util.HashMap;
import java.util.HashSet;
import java.util.Iterator;
import java.util.List;
import java.util.Map;
import java.util.Set;

import org.example.check.HardCodeConfiguration;
import org.example.check.MisssingConfiguration;
import org.example.check.PrivacyAPITracking;
import org.example.check.PrivacyLandscape;
import org.example.check.UnevenPrivacySupport;
import org.example.xq.AnalysisAPIs;
import org.example.xq.Globals;

import soot.Scene;
import soot.Body;
import soot.SootMethod;
import soot.BodyTransformer;
import soot.Transform;
import soot.jimple.toolkits.callgraph.ReachableMethods;
import soot.toolkits.scalar.Pair;

import org.example.util.PrivacyAPILoader;
import org.example.util.PrivacyAPISummary;
import org.example.util.Utils;
import org.example.util.PrivacyAPISummary.APIDescriptor;

public class Main {
	public static void main(String[] args) throws Exception {
//		if (args.length != 1) {
//			System.err.println("Provide Params <APK_PATH>");
//			System.exit(-1);
//		}
//
//		String apkPath = args[0];
		//new Main().run("./apks/air.jp.globalgear.ptomo2.apk");
		new Main().run("./apks/test1.apk");
		// new Main().runAnalysis();
	}

	private void run(String apkPath) {
		String platformPath = "./platforms";
		Globals.setupApkForAnalysis(apkPath, platformPath);

		long startTime = 0;
		long endTime = 0;
		startTime = System.currentTimeMillis();
		// Set up paths & privacy API string
		PrivacyAPILoader.loadPrivacyAPIs("res/Priv_impl5.json");
		AnalysisAPIs.runCustomPack("jtp",
				new Transform[] { new Transform("jtp.emptyBodyTransformer", new BodyTransformer() {
					@Override
					protected void internalTransform(Body b, String phaseName, Map<String, String> options) {
						// TODO Auto-generated method stub

					}
				}) });

		// Set up custom code in Flowdroid
		System.out.println("apis" + PrivacyAPISummary.getPrivacyAPIs());
		Main.this.runAnalysis();
		endTime = System.currentTimeMillis();
		Utils.LOGGER.info(String.format("#FINISH# Analysis of %s costs %d seconds", Globals.APK_PATH,
				(endTime - startTime) / 1000));
	}

	private void runAnalysis() {
		try {
			new PrivacyAPITracking().runForwardAnalysis();
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
}
