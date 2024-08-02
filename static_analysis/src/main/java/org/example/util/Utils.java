package org.example.util;

import soot.PrimType;
import soot.RefType;
import soot.Scene;
import soot.SootClass;
import soot.SootMethod;
import soot.Type;
import soot.jimple.infoflow.typing.TypeUtils;
import soot.jimple.toolkits.callgraph.CallGraph;
import soot.jimple.toolkits.callgraph.Edge;
import soot.toolkits.scalar.Pair;

import java.util.*;
import java.util.logging.Logger;

import org.example.xq.Globals;

import com.google.common.collect.Iterators;

public class Utils {
	public static final Logger LOGGER = Logger.getLogger(Utils.class.getName());

	public static class ValueError extends RuntimeException {
		public ValueError(String message) {
			super(message);
		}
	}

	public static List<String> SP_APIS = Arrays.asList(new String[] {
			"<android.content.SharedPreferences$Editor: android.content.SharedPreferences$Editor putInt(java.lang.String,int)>",
			"<android.content.SharedPreferences$Editor: android.content.SharedPreferences$Editor putLong(java.lang.String,long)>",
			"<android.content.SharedPreferences$Editor: android.content.SharedPreferences$Editor putString(java.lang.String,java.lang.String)>",
			"<android.content.SharedPreferences$Editor: android.content.SharedPreferences$Editor putBoolean(java.lang.String,boolean)>" });

	public static List<String> ONCREATE_APIS = Arrays.asList(new String[] {
		"<android.app.Activity: void onCreate(android.os.Bundle)>"
	});

	public static List<String> NETWORK_APIS = Arrays.asList(new String[] {
			"<android.content.SharedPreferences$Editor: android.content.SharedPreferences$Editor putFloat(java.lang.String,float)>",
			"<android.database.sqlite.SQLiteDatabase: android.database.Cursor query(boolean,java.lang.String,java.lang.String[],java.lang.String,java.lang.String[],java.lang.String,java.lang.String,java.lang.String,java.lang.String)>",
			"<android.database.sqlite.SQLiteDatabase: android.database.Cursor query(java.lang.String,java.lang.String[],java.lang.String,java.lang.String[],java.lang.String,java.lang.String,java.lang.String)>",
			"<android.database.sqlite.SQLiteDatabase: android.database.Cursor query(java.lang.String,java.lang.String[],java.lang.String,java.lang.String[],java.lang.String,java.lang.String,java.lang.String,java.lang.String)>",
			"<android.database.sqlite.SQLiteDatabase: android.database.Cursor rawQuery(java.lang.String,java.lang.String[])>",
			"<android.database.sqlite.SQLiteQueryBuilder: android.database.Cursor query(android.database.sqlite.SQLiteDatabase,java.lang.String[],java.lang.String,java.lang.String[],java.lang.String,java.lang.String,java.lang.String)>",
			"<java.io.BufferedOutputStream: void write(byte[])>",
			"<java.io.BufferedOutputStream: void write(byte[],int,int)>",
			"<java.io.ByteArrayOutputStream: void write(byte[])>",
			"<java.io.ByteArrayOutputStream: void write(byte[],int,int)>",
			"<java.io.DataOutputStream: void write(byte[])>", "<java.io.DataOutputStream: void write(byte[],int,int)>",
			"<java.io.DataOutputStream: void writeBytes(java.lang.String)>",
			"<java.io.DataOutputStream: void writeChars(java.lang.String)>",
			"<java.io.DataOutputStream: void writeUTF(java.lang.String)>",
			"<java.io.FileOutputStream: void write(byte[])>", "<java.io.FileOutputStream: void write(byte[],int,int)>",
			"<java.io.FilterOutputStream: void write(byte[])>", "<java.io.ObjectOutputStream: void write(byte[])>",
			"<java.io.ObjectOutputStream: void writeUTF(java.lang.String)>",
			"<java.io.OutputStream: void write(byte[])>", "<java.io.OutputStream: void write(byte[],int,int)>",
			"<java.io.OutputStreamWriter: void write(java.lang.String)>",
			"<android.telephony.SmsManager: void sendDataMessage(java.lang.String,java.lang.String,short,byte[],android.app.PendingIntent,android.app.PendingIntent)>",
			"<android.telephony.SmsManager: void sendMultipartTextMessage(java.lang.String,java.lang.String,java.util.ArrayList,java.util.ArrayList,java.util.ArrayList)>",
			"<android.telephony.SmsManager: void sendTextMessage(java.lang.String,java.lang.String,java.lang.String,android.app.PendingIntent,android.app.PendingIntent)>",
			"<android.telephony.gsm.SmsManager: void sendDataMessage(java.lang.String,java.lang.String,short,byte[],android.app.PendingIntent,android.app.PendingIntent)>",
			"<android.telephony.gsm.SmsManager: void sendMultipartTextMessage(java.lang.String,java.lang.String,java.util.ArrayList,java.util.ArrayList,java.util.ArrayList)>",
			"<android.telephony.gsm.SmsManager: void sendTextMessage(java.lang.String,java.lang.String,java.lang.String,android.app.PendingIntent,android.app.PendingIntent)>",
			"<android.webkit.WebView: void loadData(java.lang.String,java.lang.String,java.lang.String)>",
			"<android.webkit.WebView: void loadDataWithBaseURL(java.lang.String,java.lang.String,java.lang.String,java.lang.String,java.lang.String)>",
			"<android.webkit.WebView: void loadUrl(java.lang.String)>",
			"<android.webkit.WebView: void loadUrl(java.lang.String,java.util.Map)>",
			"<com.android.volley.RequestQueue: com.android.volley.Request add(com.android.volley.Request)>",
			"<com.ibm.mqtt.MqttClient: com.ibm.mqtt.IMqttClient createMqttClient(java.lang.String,com.ibm.mqtt.MqttPersistence)>",
			"<com.ibm.mqtt.MqttClient: void <init>(java.lang.String)>",
			"<com.ibm.mqttclient.factory.MqttClientFactory: com.ibm.mqttclient.MqttClient createMqttClient(java.lang.String,java.lang.String,com.ibm.mqttclient.factory.MqttProperties)>",
			"<com.ibm.mqttclient.factory.MqttClientFactory: com.ibm.mqttclient.MqttClient createMqttClient(java.lang.String,java.lang.String,com.ibm.mqttclient.factory.MqttProperties,com.ibm.mqttclient.MqttPersistence)>",
			"<com.octo.android.robospice.SpiceManager: void execute(com.octo.android.robospice.request.SpiceRequest,com.octo.android.robospice.request.listener.RequestListener)>",
			"<com.octo.android.robospice.SpiceManager: void execute(com.octo.android.robospice.request.SpiceRequest,java.lang.Object,long,com.octo.android.robospice.request.listener.RequestListener)>",
			"<com.squareup.okhttp.OkHttpClient: com.squareup.okhttp.Call newCall(com.squareup.okhttp.Request)>",
			"<java.io.FileOutputStream: void write(byte[])>", "<java.io.FileOutputStream: void write(byte[],int,int)>",
			"<java.io.FileOutputStream: void write(int)>", "<java.io.OutputStream: void write(byte[])>",
			"<java.io.OutputStream: void write(byte[],int,int)>", "<java.io.OutputStream: void write(int)>",
			"<java.io.OutputStreamWriter: java.io.Writer append(java.lang.CharSequence)>",
			"<java.io.Writer: java.io.Writer append(java.lang.CharSequence)>", "<java.io.Writer: void write(char[])>",
			"<java.io.Writer: void write(char[],int,int)>", "<java.io.Writer: void write(int)>",
			"<java.io.Writer: void write(java.lang.String)>", "<java.io.Writer: void write(java.lang.String,int,int)>",
			"<java.net.DatagramSocket: void <init>(int)>", "<java.net.DatagramSocket: void send(java.net.DatagramPacket)>",
			"<java.net.HttpURLConnection: java.io.OutputStream getOutputStream()>",
			"<java.net.HttpURLConnection: void <init>(int)>", "<java.net.HttpURLConnection: void connect()>",
			"<java.net.HttpURLConnection: void setDoOutput(boolean)>",
			"<java.net.HttpURLConnection: void setRequestMethod(java.lang.String)>",
			"<java.net.MulticastSocket: void <init>(int)>", "<java.net.MulticastSocket: void <init>(java.net.SocketAddress)>",
			"<java.net.MulticastSocket: void bind(java.net.SocketAddress)>",
			"<java.net.MulticastSocket: void send(java.net.DatagramPacket)>", "<java.net.ServerSocket: void <init>(int)>",
			"<java.net.ServerSocket: void bind(java.net.SocketAddress)>",
			"<java.net.Socket: java.io.OutputStream getOutputStream()>", "<java.net.Socket: void <init>(int)>",
			"<java.net.Socket: void connect(java.net.SocketAddress)>",
			"<java.net.Socket: void connect(java.net.SocketAddress,int)>",
			"<java.net.URL: java.io.InputStream openStream()>",
			"<java.net.URL: java.net.URLConnection openConnection()>",
			"<java.net.URLConnection: java.io.OutputStream getOutputStream()>",
			"<java.net.URLConnection: void setDoOutput(boolean)>",
			"<java.nio.channels.DatagramChannel: int send(java.nio.ByteBuffer,java.net.SocketAddress)>",
			"<java.nio.channels.DatagramChannel: int write(java.nio.ByteBuffer)>",
			"<java.nio.channels.DatagramChannel: long write(java.nio.ByteBuffer[])>",
			"<java.nio.channels.DatagramChannel: long write(java.nio.ByteBuffer[],int,int)>",
			"<javax.net.ssl.HttpsURLConnection: java.io.OutputStream getOutputStream()>",
			"<okhttp3.OkHttpClient: okhttp3.Call newCall(okhttp3.Request)>",
			"<org.apache.http.client.HttpClient: org.apache.http.HttpResponse execute(org.apache.http.client.methods.HttpUriRequest)>",
			"<org.apache.http.client.HttpClient: org.apache.http.HttpResponse execute(org.apache.http.client.methods.HttpUriRequest,org.apache.http.protocol.HttpContext)>",
			"<org.apache.http.client.methods.HttpGet: void <init>(java.lang.String)>",
			"<org.apache.http.client.methods.HttpGet: void <init>(java.net.URI)>",
			"<org.apache.http.client.methods.HttpGet: void addHeader(java.lang.String,java.lang.String)>",
			"<org.apache.http.client.methods.HttpGet: void setHeader(java.lang.String,java.lang.String)>",
			"<org.apache.http.client.methods.HttpPost: void <init>(java.lang.String)>",
			"<org.apache.http.client.methods.HttpPost: void addHeader(java.lang.String,java.lang.String)>",
			"<org.apache.http.client.methods.HttpPost: void setEntity(org.apache.http.HttpEntity)>",
			"<org.apache.http.client.methods.HttpPost: void setHeader(java.lang.String,java.lang.String)>",
			"<org.apache.http.impl.client.AbstractHttpClient: org.apache.http.HttpResponse execute(org.apache.http.client.methods.HttpUriRequest)>",
			"<org.apache.http.impl.client.AbstractHttpClient: org.apache.http.HttpResponse execute(org.apache.http.client.methods.HttpUriRequest,org.apache.http.protocol.HttpContext)>",
			"<org.apache.http.impl.client.DefaultHttpClient: org.apache.http.HttpResponse execute(org.apache.http.client.methods.HttpUriRequest)>",
			"<org.apache.http.impl.client.DefaultHttpClient: void <init>(int)>",
			"<org.eclipse.paho.android.service.MqttAndroidClient: org.eclipse.paho.client.mqttv3.IMqttDeliveryToken publish(java.lang.String,byte[],int,boolean)>",
			"<org.eclipse.paho.android.service.MqttAndroidClient: org.eclipse.paho.client.mqttv3.IMqttDeliveryToken publish(java.lang.String,byte[],int,boolean,java.lang.Object,org.eclipse.paho.client.mqttv3.IMqttActionListener)>",
			"<org.eclipse.paho.android.service.MqttAndroidClient: org.eclipse.paho.client.mqttv3.IMqttDeliveryToken publish(java.lang.String,org.eclipse.paho.client.mqttv3.MqttMessage)>",
			"<org.eclipse.paho.android.service.MqttAndroidClient: org.eclipse.paho.client.mqttv3.IMqttDeliveryToken publish(java.lang.String,org.eclipse.paho.client.mqttv3.MqttMessage,java.lang.Object,org.eclipse.paho.client.mqttv3.IMqttActionListener)>",
			"<org.eclipse.paho.client.mqttv3.MqttClient: org.eclipse.paho.client.mqttv3.MqttTopic getTopic(java.lang.String)>",
			"<org.eclipse.paho.client.mqttv3.MqttClient: void <init>(java.lang.String,java.lang.String)>",
			"<org.eclipse.paho.client.mqttv3.MqttClient: void <init>(java.lang.String,java.lang.String,org.eclipse.paho.client.mqttv3/MqttClientPersistence)>",
			"<org.eclipse.paho.client.mqttv3.MqttClient: void publish(java.lang.String,byte[],int,boolean)>",
			"<org.eclipse.paho.client.mqttv3.MqttClient: void publish(java.lang.String,org.eclipse.paho.client.mqttv3.MqttMessage)>",
			"<org.eclipse.paho.client.mqttv3.MqttTopic: org.eclipse.paho.client.mqttv3.MqttDeliveryToken publish(byte[],int,boolean)>",
			"<org.eclipse.paho.client.mqttv3.MqttTopic: org.eclipse.paho.client.mqttv3.MqttDeliveryToken publish(org.eclipse.paho.client.mqttv3.MqttMessage)>",
			"<org.jetbrains.anko.AsyncKt: java.util.concurrent.Future doAsync$default(java.lang.Object,kotlin.jvm.functions.Function1,kotlin.jvm.functions.Function1,int,java.lang.Object)>",
			"<org.ksoap2.transport.AndroidHttpTransport: void call(java.lang.String,org.ksoap2.SoapEnvelope)>",
			"<org.ksoap2.transport.HttpTransportSE: void call(java.lang.String,org.ksoap2.SoapEnvelope)>",
			"<org.ksoap2x.transport.HttpTransportSE: java.util.List call(java.lang.String,org.ksoap2x.SoapEnvelope,java.util.List)>",
			"<org.ksoap2x.transport.HttpTransportSE: java.util.List call(java.lang.String,org.ksoap2x.SoapEnvelope,java.util.List,java.io.File)>",
			"<org.ksoap2x.transport.KeepAliveHttpTransportSE: java.util.List call(java.lang.String,org.ksoap2x.SoapEnvelope,java.util.List)>",
			"<org.springframework.web.client.RestOperations: org.springframework.http.ResponseEntity exchange(java.lang.String,org.springframework.http.HttpMethod,org.springframework.http.HttpEntity,java.lang.Class,java.lang.Object[])>",
			"<org.springframework.web.client.RestTemplate: org.springframework.http.ResponseEntity exchange(java.lang.String,org.springframework.http.HttpMethod,org.springframework.http.HttpEntity,java.lang.Class,java.lang.Object[])>",
			"<retrofit.client.ApacheClient: org.apache.http.HttpResponse execute(org.apache.http.client.HttpClient,org.apache.http.client.methods.HttpUriRequest)>",
			"<retrofit.client.OkClient: retrofit.client.Response execute(retrofit.client.Request)>",
			"<retrofit2.Retrofit$Builder: retrofit2.Retrofit build()>",
			"<io.fabric.sdk.android.services.network.HttpRequest: io.fabric.sdk.android.services.network.HttpRequest send(java.lang.CharSequence)>",
			"<io.fabric.sdk.android.services.network.HttpRequest: io.fabric.sdk.android.services.network.HttpRequest send(java.io.InputStream)>",
			"<com.google.android.gms.ads.internal.gmsg.HttpClient: org.json.JSONObject send(org.json.JSONObject)>",
			"<com.loopj.android.http.AsyncHttpClient: com.loopj.android.http.RequestHandle sendRequest(org.apache.http.impl.client.DefaultHttpClient,org.apache.http.protocol.HttpContext,org.apache.http.client.methods.HttpUriRequest,java.lang.String,com.loopj.android.http.ResponseHandlerInterface,android.content.Context)>",
			"<com.loopj.android.http.AsyncHttpClient: void post(android.content.Context,java.lang.String,org.apache.http.HttpEntity,java.lang.String,com.loopj.android.http.AsyncHttpResponseHandler)>",
			"<com.loopj.android.http.AsyncHttpClient: void post(java.lang.String,com.loopj.android.http.RequestParams,com.loopj.android.http.AsyncHttpResponseHandler)>",
			"<org.eclipse.paho.client.mqttv3.MqttAsyncClient: org.eclipse.paho.client.mqttv3.IMqttDeliveryToken publish(java.lang.String,byte[],int,boolean)>",
			"<org.eclipse.paho.client.mqttv3.MqttAsyncClient: org.eclipse.paho.client.mqttv3.IMqttDeliveryToken publish(java.lang.String,byte[],int,boolean,java.lang.Object,org.eclipse.paho.client.mqttv3.IMqttActionListener)>",
			"<org.eclipse.paho.client.mqttv3.MqttAsyncClient: org.eclipse.paho.client.mqttv3.IMqttDeliveryToken publish(java.lang.String,org.eclipse.paho.client.mqttv3.MqttMessage,java.lang.Object,org.eclipse.paho.client.mqttv3.IMqttActionListener)>",
			"<org.eclipse.paho.client.mqttv3.MqttClient: void publish(java.lang.String,org.eclipse.paho.client.mqttv3.MqttMessage)>",
			"<org.eclipse.paho.client.mqttv3.MqttTopic: org.eclipse.paho.client.mqttv3.MqttDeliveryToken publish(org.eclipse.paho.client.mqttv3.MqttMessage)>",
			"<org.eclipse.paho.client.mqttv3.internal.IDisconnectedBufferCallback: void publishBufferedMessage(org.eclipse.paho.client.mqttv3.BufferedMessage)>",
			"<com.amazonaws.mobileconnectors.iot.AWSIotMqttManager: void publishData(byte[],java.lang.String,com.amazonaws.mobileconnectors.iot.AWSIotMqttQos)>",
			"<com.amazonaws.mobileconnectors.iot.AWSIotMqttManager: void publishData(byte[],java.lang.String,com.amazonaws.mobileconnectors.iot.AWSIotMqttQos,com.amazonaws.mobileconnectors.iot.AWSIotMqttMessageDeliveryCallback,java.lang.Object)>",
			"<com.amazonaws.mobileconnectors.iot.AWSIotMqttManager: void publishString(java.lang.String,java.lang.String,com.amazonaws.mobileconnectors.iot.AWSIotMqttQos)>",
			"<com.amazonaws.mobileconnectors.iot.AWSIotMqttManager: void publishString(java.lang.String,java.lang.String,com.amazonaws.mobileconnectors.iot.AWSIotMqttQos,com.amazonaws.mobileconnectors.iot.AWSIotMqttMessageDeliveryCallback,java.lang.Object)>" });

	public static boolean isInterestingTypes(Type type) {
		if (type instanceof PrimType || TypeUtils.isStringType(type) || TypeUtils.isPrimitiveArray(type)) {
			return true;
		}

		Set<String> interestingTypes = new HashSet<>(Arrays.asList("java.lang.Integer", "java.lang.Byte",
				"java.lang.Short", "java.lang.Long", "java.lang.Float", "java.lang.Double", "java.lang.Boolean",
				"java.lang.Character", "java.util.List", "java.util.ArrayList", "java.util.LinkedList", "java.util.Set",
				"java.util.HashSet", "java.util.LinkedHashSet", "java.util.Map", "java.util.HashMap",
				"java.util.LinkedHashMap", "java.util.Collection", "org.json.JSONObject"));

		if (type instanceof RefType) {
			SootClass classOfType = ((RefType) type).getSootClass();
			if (interestingTypes.contains(classOfType.getName())) {
				return true;
			}

			if (classOfType.isEnum()) {
				return true;
			}
		}

		return false;
	}

	public static boolean isSamePackage(String package1, String package2) {
		int dotCnt = 0;
		int minLength = Math.min(package1.length(), package2.length());
		for (int i = 0; i < minLength; i++) {
			if (package1.charAt(i) != package2.charAt(i)) {
				return dotCnt >= 2;
			}

			if (package1.charAt(i) == '.') {
				dotCnt += 1;
			}
		}

		return dotCnt >= 2;
	}

	public static String getClassFromMethodSignature(String methodSignature) {
		if (methodSignature == null || methodSignature.isEmpty()) {
			throw new IllegalArgumentException("Method signature cannot be null or empty");
		}
		int start = methodSignature.indexOf('<') + 1; // Find the index of '<'
		int end = methodSignature.indexOf(':'); // Find the index of ':'

		if (start < 1 || end < 1 || start >= end) {
			throw new IllegalArgumentException("Invalid method signature format");
		}

		return methodSignature.substring(start, end).trim(); // Extract and return class name
	}

	public static String getTopDomain(String packageName) {
		if (packageName == null || packageName.isEmpty()) {
			return "";
		}

		String[] components = packageName.split("\\.");

		// Check if there are enough components to form a top domain
		if (components.length < 2) {
			return packageName; // or return an error message or throw an exception
		}

		// Concatenate the first three components to form the top domain
		return String.join(".", Arrays.copyOfRange(components, 0, 2));
	}

	public static HashMap<String, Set<String>> getXrefWithOverrides(String className, String methodName) {
		SootClass givenClass = Scene.v().getSootClass(className);
		CallGraph cg = Scene.v().getCallGraph();

		HashMap<String, Set<String>> xrefs = new HashMap<String, Set<String>>();

		// Iterate over methods in the given class
		for (SootMethod method : givenClass.getMethods()) {
			if (method.getName().equals(methodName)) {
				Set<String> callers = new HashSet<String>();

				// Now, print the xrefs (callers) for the method
				for (Iterator<Edge> it = cg.edgesInto(method); it.hasNext();) {
					Edge e = it.next();
					callers.add(e.src().method().getSignature());
				}
				xrefs.put(method.getSignature(), callers);
			}
		}
		return xrefs;
	}

	// remembering all paths may lead to out of memory error.
	public static Set<Pair<String, String>> findPathsBFSNoPaths(String className, String methodName,
			Set<Pair<String, String>> targetMethods) {
		Set<Pair<String, String>> reachable = new HashSet<>();
		SootClass givenClass = Scene.v().getSootClass(className);
		CallGraph cg = Scene.v().getCallGraph();

		// Iterate over methods in the given class
		for (SootMethod method : givenClass.getMethods()) {
			if (method.getName().equals(methodName)) {
				Queue<Pair<SootMethod, Integer>> queue = new LinkedList<>();
				Set<SootMethod> visited = new HashSet<>();
				traverseBFSNoPaths(cg, method, reachable, targetMethods, queue, visited);
			}
		}

		return reachable;
	}

	private static void traverseBFSNoPaths(CallGraph cg, SootMethod startNode, Set<Pair<String, String>> reachable,
			Set<Pair<String, String>> targetMethods, Queue<Pair<SootMethod, Integer>> queue, Set<SootMethod> visited) {
		// Initialize the queue with the starting node
		queue.offer(new Pair<>(startNode, 0));
		visited.add(startNode);

		while (!queue.isEmpty()) {
			Pair<SootMethod, Integer> currentNode = queue.poll();
			SootMethod currentMethod = currentNode.getO1();
			Integer currentStep = currentNode.getO2();

			if (currentStep >= Globals.MAX_DEPTH) {
				continue;
			}

			// If the current node is not the start node, copy paths from the previous node
			// and add the current node
			for (Iterator<Edge> it = cg.edgesOutOf(currentMethod); it.hasNext();) {
				Edge edge = it.next();
				SootMethod tgt = edge.tgt();

				// we ignore the non-application methods on call graph, since modeling of these
				// methods is most likely inaccurate, such as <java.lang.Thread: void run()>
				if (!tgt.getDeclaringClass().isApplicationClass()) {
					continue;
				}

				if (!visited.contains(tgt)) {
					Pair<String, String> newKey = new Pair<>(tgt.getDeclaringClass().getName(), tgt.getName());

					if (targetMethods.contains(newKey)) {
						reachable.add(newKey);
					}

					queue.offer(new Pair<>(tgt, currentStep + 1));
					visited.add(tgt);

					// Utils.LOGGER.info(
					// String.format("visiting: %s --- %s", currentMethod.getSignature(),
					// tgt.getSignature()));
				}
			}
		}
	}

	// remembering all paths may lead to out of memory error.
	public static Map<SootMethod, List<List<SootMethod>>> findPathsBFS(String className, String methodName,
			Set<Pair<String, String>> targetMethods) {
		Map<SootMethod, List<List<SootMethod>>> paths = new HashMap<>();
		SootClass givenClass = Scene.v().getSootClass(className);
		CallGraph cg = Scene.v().getCallGraph();

		// Iterate over methods in the given class
		for (SootMethod method : givenClass.getMethods()) {
			if (method.getName().equals(methodName)) {
				Queue<Pair<SootMethod, Integer>> queue = new LinkedList<>();
				Set<SootMethod> visited = new HashSet<>();
				traverseBFS(cg, method, paths, targetMethods, queue, visited);
			}
		}

		return paths;
	}

	private static void traverseBFS(CallGraph cg, SootMethod startNode, Map<SootMethod, List<List<SootMethod>>> paths,
			Set<Pair<String, String>> targetMethods, Queue<Pair<SootMethod, Integer>> queue, Set<SootMethod> visited) {
		// Initialize the queue with the starting node
		queue.offer(new Pair<>(startNode, 0));
		visited.add(startNode);
		paths.computeIfAbsent(startNode, k -> new ArrayList<>()).add(Collections.singletonList(startNode));

		while (!queue.isEmpty()) {
			Pair<SootMethod, Integer> currentNode = queue.poll();
			SootMethod currentMethod = currentNode.getO1();
			Integer currentStep = currentNode.getO2();

			if (currentStep < Globals.MAX_DEPTH) {
				// If the current node is not the start node, copy paths from the previous node
				// and add the current node
				// the order the edges are traversed impacts the discovery of paths; we shuffle
				// the edges here.
				for (Iterator<Edge> it = shuffleIterator(cg.edgesOutOf(currentMethod)); it.hasNext();) {
					Edge edge = it.next();
					SootMethod tgt = edge.tgt();

					// we ignore the non-application methods on call graph, since modeling of these
					// methods is most likely inaccurate, such as <java.lang.Thread: void run()>
					if (!tgt.getDeclaringClass().isApplicationClass()) {
						continue;
					}

					if (!visited.contains(tgt)) {
						List<List<SootMethod>> newPaths = new ArrayList<>();

						for (List<SootMethod> path : paths.get(currentMethod)) {
							List<SootMethod> newPath = new ArrayList<>(path);
							newPath.add(tgt);
							newPaths.add(newPath);
						}

						if (paths.containsKey(tgt)) {
							paths.get(tgt).addAll(newPaths);
						} else {
							paths.put(tgt, newPaths);
						}

						queue.offer(new Pair<>(tgt, currentStep + 1));
						visited.add(tgt);

						// Utils.LOGGER.info(String.format("visiting: %s --- %s",
						// currentMethod.getSignature(), tgt.getSignature()));
					}
				}
			}

			if (!targetMethods
					.contains(new Pair<>(currentMethod.getDeclaringClass().getName(), currentMethod.getName()))) {
				paths.remove(currentMethod);
			}
		}
	}

	public static <T> Iterator<T> shuffleIterator(Iterator<T> iterator) {
		List<T> list = new ArrayList<>();

		// Convert the iterator to a list
		while (iterator.hasNext()) {
			list.add(iterator.next());
		}

		// Shuffle the list
		Collections.shuffle(list);

		// Return an iterator over the shuffled list
		return list.iterator();
	}

	// if we use visited in DFS, we are not able to find all paths;
	// if we don't use visited, large apps cause timeout.
	public static Map<Pair<String, String>, List<List<SootMethod>>> findPathsDFS(String className, String methodName,
			Set<Pair<String, String>> targetMethods) {
		Map<Pair<String, String>, List<List<SootMethod>>> paths = new HashMap<>();
		SootClass givenClass = Scene.v().getSootClass(className);
		CallGraph cg = Scene.v().getCallGraph();

		// Iterate over methods in the given class
		for (SootMethod method : givenClass.getMethods()) {
			if (method.getName().equals(methodName)) {
				List<SootMethod> path = new ArrayList<>();
				Set<SootMethod> visited = new HashSet<>();
				traverseDFS(cg, method, path, paths, targetMethods, visited);
			}
		}

		return paths;
	}

	private static void traverseDFS(CallGraph cg, SootMethod current, List<SootMethod> path,
			Map<Pair<String, String>, List<List<SootMethod>>> paths, Set<Pair<String, String>> targetMethods,
			Set<SootMethod> visited) {

		if (path.size() > 1) {
			Pair<String, String> currentSig = new Pair<>(current.getDeclaringClass().getName(), current.getName());
			if (targetMethods.contains(currentSig)) {
				paths.computeIfAbsent(currentSig, k -> new ArrayList<>()).add(new ArrayList<>(path));
			}
		}

		// early stop of very deep paths
		// we ignore the non-application methods on call graph, since modeling of these
		// methods is most likely inaccurate, such as <java.lang.Thread: void run()>
		if (path.size() > Globals.MAX_DEPTH || !current.getDeclaringClass().isApplicationClass()) {
			return;
		}

		path.add(current);
		visited.add(current);

		for (Iterator<Edge> it = cg.edgesOutOf(current); it.hasNext();) {
			Edge edge = it.next();
			SootMethod tgt = edge.tgt();
			if (!visited.contains(tgt)) {
				Utils.LOGGER
						.info(String.format("traverse: %s --- %s", current.getSignature(), edge.tgt().getSignature()));
				traverseDFS(cg, tgt, path, paths, targetMethods, visited);
			} else {
				Utils.LOGGER
						.info(String.format("ignore: %s --- %s", current.getSignature(), edge.tgt().getSignature()));
			}
		}

		path.remove(path.size() - 1);
	}

	public static List<SootMethod> findMethod(String target_class, String target_method) {
		// Load the target class
		SootClass sootClass;
		try {
			if (!Scene.v().containsClass(target_class)) {
				Scene.v().forceResolve(target_class, SootClass.BODIES);
			}

			sootClass = Scene.v().getSootClass(target_class);
			if (sootClass.isInterface()) {
				LOGGER.warning(target_class + " is an interface.");
			} else if (sootClass.isAbstract()) {
				LOGGER.warning(target_class + " is an abstract class.");
			} else if (sootClass.isPhantom()) {
				LOGGER.warning(target_class + " is treated as a phantom class by Soot.");
			} else if (sootClass.getMethods().isEmpty()) {
				LOGGER.warning(target_class + " is an empty class.");
			}
		} catch (RuntimeException e) {
			LOGGER.warning(e.getMessage());
			LOGGER.warning("Class not found!");
			return null;
		}

		List<SootMethod> methods_list = new ArrayList<>();

		// Iterate through methods to find and print the signatures
		for (SootMethod method : sootClass.getMethods()) {
			if (method.getName().equals(target_method)) {
				methods_list.add(method);
			}
		}

		if (methods_list.isEmpty()) {
			LOGGER.warning("No method found!");
			return null;
		}

		LOGGER.info("Found " + methods_list.size() + " methods!");
		LOGGER.info("findMethod() Finished!");

		return methods_list;
	}

	public static boolean isSubclassOf(SootClass childClass, SootClass parentClass) {
		// Check if childClass is a subclass of parentClass
		return Scene.v().getOrMakeFastHierarchy().isSubclass(childClass, parentClass);
	}

	public static boolean implementsInterface(SootClass classToCheck, SootClass interfaceToCheck) {
		// Check if classToCheck implements interfaceToCheck
		return Scene.v().getOrMakeFastHierarchy().canStoreType(classToCheck.getType(), interfaceToCheck.getType());
	}
}
