import networkx as nx
from networkx.drawing.nx_pydot import read_dot

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

    # Iterate over all possible pairs of source and target nodes
    for source in digraph.nodes:
        print(source)
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

# Example usage
if __name__ == "__main__":
    # Create a directed graph
    with open("path.txt", "w") as f:
        f.writelines([])
    cg = read_dot("call_graph.dot")
    print(cg)


    # Specify the node to be included in the paths


    # Find and print the maximal paths containing the specified node
    maximal_paths_with_node = find_maximal_paths_containing_node(cg, "Lcom/applovin/sdk/AppLovinPrivacySettings;", "setIsAgeRestrictedUser")
    for path in maximal_paths_with_node:
        print("Maximal path containing node {}: {}".format(node_to_include, path))
