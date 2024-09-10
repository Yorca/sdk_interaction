from androguard.misc import AnalyzeAPK
import androguard.core.analysis.analysis
import matplotlib.pyplot as plt
import pickle
import networkx as nx

from networkx.drawing.nx_pydot import write_dot, read_dot

def find_maximal_paths_containing_node(digraph, node_class, node_method):
    """
    Finds all maximal paths in the directed graph that contain the specified node.

    Parameters:
    digraph (nx.DiGraph): A directed graph.
    node: The node that must be contained in the paths.

    Returns:
    List of maximal paths (each path is represented as a list of nodes).
    """
    all_paths = []

    node = None
    for item in digraph.nodes:
        if item.class_name == node_class and item.name == node_method:
            node = item
            break

    if not node:
        return []

    # Iterate over all possible pairs of source and target nodes
    for source in digraph.nodes:
        for target in digraph.nodes:
            if source != target:
                # Find all paths between the source and target
                paths = nx.all_simple_paths(digraph, source, target)
                # Filter paths that contain the specified node
                for path in paths:
                    if node in path:
                        all_paths.append(path)

    # Remove subpaths to get only maximal paths containing the node
    maximal_paths = []
    for path in all_paths:
        is_subpath = False
        for other_path in all_paths:
            if path != other_path and set(path).issubset(set(other_path)):
                is_subpath = True
                break
        if not is_subpath:
            maximal_paths.append(path)

    return maximal_paths

def find_method_usage(apk_path, class_name ,method_name):
    a, d, dx = AnalyzeAPK(apk_path)

    # Get the call graph for the specific method in the class
    call_graph = dx.get_call_graph()
    write_dot(call_graph, "call_graph2.dot")
    paths = find_maximal_paths_containing_node(call_graph, class_name, method_name)
    print(paths)
    with open("path.txt", "w") as f:
        f.writelines(paths)
    # Find the starting node for the specified method
    # entry_node = None
    # for node in call_graph.nodes():
    #     if node.class_name == class_name and node.name == method_name:
    #         entry_node = node
    #         break
    #
    # if entry_node is None:
    #     print("Specified method not found in the call graph.")
    #     return
    #
    # # Collect all nodes and edges reachable from the entry node
    # reachable_nodes = set()
    # reachable_edges = set()
    #
    # def traverse_graph(node):
    #     if node in reachable_nodes:
    #         return
    #     reachable_nodes.add(node)
    #     for successor in call_graph.successors(node):
    #         reachable_edges.add((node, successor))
    #         traverse_graph(successor)
    #
    # traverse_graph(entry_node)
    #
    # # Create a subgraph containing only the reachable nodes and edges
    # subgraph = call_graph.subgraph(reachable_nodes)
    #
    # # Convert the subgraph to a DOT file
    # dot_file_name = f"complete_call_graph_{class_name.replace('/', '_')}_{method_name}.dot"
    # write_dot(subgraph, dot_file_name)
    # print(f"Complete call graph DOT file generated: {dot_file_name}")




apk_path = "test_apk/KawaiiWorld-CraftandBuild_1.5.2_Apkpure.apk"
class_name = "Lcom/applovin/sdk/AppLovinPrivacySettings;"
api_name = "setIsAgeRestrictedUser"
find_method_usage(apk_path, class_name, api_name)

# let AppLovinPrivacySettings = Java.use("com.applovin.sdk.AppLovinPrivacySettings");
# AppLovinPrivacySettings["setIsAgeRestrictedUser"].implementation = function (z, context) {
#     console.log(`AppLovinPrivacySettings.setIsAgeRestrictedUser is called: z=${z}, context=${context}`);
#     this["setIsAgeRestrictedUser"](z, context);
# };