package org.example.util;

import java.util.*;
import java.util.concurrent.ConcurrentHashMap;

public class DirectedGraph {
	// Map to store the adjacency list for each node
	private Map<Node, Set<Edge>> adjList;

	// Map to store nodes by their ID
	private Map<String, Node> nodes;

	private Node root;

	// Constructor to initialize the adjacency list
	public DirectedGraph(String rootId, Object rootProperty1, Object rootProperty2) {
		adjList = new ConcurrentHashMap<>();
		nodes = new ConcurrentHashMap<>();
		addNode(rootId, rootProperty1, rootProperty2);
		root = nodes.get(rootId);
	}

	// Method to add a node to the graph
	public void addNode(String id, Object property1, Object property2) {
		if (!nodes.containsKey(id)) {
			Node node = new Node(id, property1, property2);
			adjList.put(node, new HashSet<Edge>());
			nodes.put(node.id, node);
		}
	}

	public String getRootId() {
		return root.id;
	}

	public boolean hasNode(String id) {
		return nodes.containsKey(id);
	}

	// Method to add an edge to the graph
	public void addEdge(String sourceId, String destinationId, Object property) {
		Node source = nodes.get(sourceId);
		Node destination = nodes.get(destinationId);

		if (source == null || destination == null) {
			throw new IllegalArgumentException("Source or Destination node does not exist.");
		}

		Edge edge = new Edge(source, destination, property);
		adjList.get(source).add(edge);
	}

	// Helper method for cycle detection using DFS
	private boolean dfs(Node node, Set<Node> visited, Set<Node> recursionStack) {
		if (recursionStack.contains(node)) {
			return true;
		}
		if (visited.contains(node)) {
			return false;
		}

		visited.add(node);
		recursionStack.add(node);

		for (Edge edge : adjList.getOrDefault(node, Collections.emptySet())) {
			Node neighbor = edge.destination;
			if (dfs(neighbor, visited, recursionStack)) {
				return true;
			}
		}

		recursionStack.remove(node);
		return false;
	}

	// Method to print the graph starting from the root node
	public void printGraphFromRoot() {
		if (root == null) {
			System.out.println("Root is not set.");
			return;
		}

		Set<Node> visited = new HashSet<>();
		printGraphFromNode(root, visited, "", null);
	}

	// Helper method to print the graph starting from a given node
	private void printGraphFromNode(Node node, Set<Node> visited, String indent, Object property) {
		if (visited.contains(node)) {
			return;
		}

		visited.add(node);

		if (!node.id.contains("dummyMainClass") && node.id.contains("invoke")) {
			System.out.println(indent + node + (Boolean.valueOf(true).equals(property) ? " implicit" : ""));
		}

		for (Edge edge : adjList.getOrDefault(node, Collections.emptySet())) {
			Node neighbor = edge.destination;
			printGraphFromNode(neighbor, visited, indent + " ", edge.property);
		}
	}

	public class Node {
		public String id;
		public Object property1;
		public Object property2;

		public Node(String id, Object property1, Object property2) {
			this.id = id;
			this.property1 = property1;
			this.property2 = property2;
		}

		@Override
		public String toString() {
			// return "Node{" + "id='" + id + '\'' + ", property1=" + property1 + ",
			// property2=" + property2 + '}';
			return id;
		}

		@Override
		public boolean equals(Object o) {
			if (this == o)
				return true;
			if (o == null || getClass() != o.getClass())
				return false;

			Node node = (Node) o;

			return id.equals(node.id);
		}

		@Override
		public int hashCode() {
			return id.hashCode();
		}
	}

	public class Edge {
		public Node source;
		public Node destination;
		public Object property;

		public Edge(Node source, Node destination, Object property) {
			this.source = source;
			this.destination = destination;
			this.property = property;
		}

		@Override
		public boolean equals(Object o) {
			if (this == o)
				return true;
			if (o == null || getClass() != o.getClass())
				return false;

			Edge edge = (Edge) o;
			return source.equals(edge.source) && destination.equals(edge.destination) && property.equals(edge.property);
		}

		@Override
		public int hashCode() {
			int result = source.hashCode();
			result = 31 * result + destination.hashCode();
			result = 31 * result + property.hashCode();
			return result;
		}

		@Override
		public String toString() {
			// return "Edge{" + "source=" + source + ", destination=" + destination + ",
			// property=" + property + '}';
			return "-->" + destination + ", property=" + property;
		}
	}
}
