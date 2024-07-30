package org.example;
import soot.*;
import soot.jimple.toolkits.callgraph.CallGraph;
import soot.jimple.toolkits.callgraph.Edge;
import soot.options.Options;
import soot.toolkits.graph.*;
import soot.util.cfgcmd.CFGToDotGraph;

import java.util.*;

public class CallGraphGenerator {
    public static void main(String[] args) {
        // Set Soot options
        Options.v().set_prepend_classpath(true);
        Options.v().set_process_dir(Collections.singletonList("/Users/yorca/PycharmProjects/sdk_interaction/DepAnalysis/test_apk/KawaiiWorld-CraftandBuild_1.5.2_Apkpure.apk"));
        Options.v().set_android_jars("/Users/yorca/Library/Android/sdk/platforms");
        Options.v().set_src_prec(Options.src_prec_apk);
      //  Options.v().set_force_android_jar("/Users/yorca/Library/Android/sdk/platforms/android-28/android.jar");
        Options.v().set_whole_program(true);
        Options.v().set_allow_phantom_refs(true);

        // Load the APK
        Scene.v().loadNecessaryClasses();

        // Set the entry point
        SootClass appClass = Scene.v().getSootClass("com.appodeal.ads.RestrictedData");
        SootMethod entryPoint = appClass.getMethodByName("isUserAgeRestricted");
        List<SootMethod> entryPoints = new ArrayList<>();
        entryPoints.add(entryPoint);
        Scene.v().setEntryPoints(entryPoints);

        // Enable Spark call graph construction
        Options.v().setPhaseOption("cg.spark", "on");

        // Run Soot
        PackManager.v().runPacks();
        PackManager.v().writeOutput();

        // Get the call graph
        CallGraph cg = Scene.v().getCallGraph();
        Iterator<Edge> edges = cg.iterator();

        // Print the call graph
        while (edges.hasNext()) {
            Edge edge = edges.next();
            System.out.println(edge.getSrc() + " -> " + edge.getTgt());
        }

        // Optionally, generate a DOT file for visualization
        CFGToDotGraph cfgToDot = new CFGToDotGraph();
        for (SootClass sc : Scene.v().getApplicationClasses()) {
            for (SootMethod sm : sc.getMethods()) {
                if (sm.hasActiveBody()) {
                    Body body = sm.retrieveActiveBody();
                    BlockGraph blockGraph = new BriefBlockGraph(body);
                    cfgToDot.drawCFG(blockGraph, body).plot("cfg_" + sm.getName() + ".dot");
                }
            }
        }


    }
}
