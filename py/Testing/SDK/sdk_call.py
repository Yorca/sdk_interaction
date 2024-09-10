import sqlite3
import matplotlib.pyplot as plt
import networkx as nx

conn = sqlite3.connect('/Users/yorca/Downloads/final_filter_all_v2.db')
cursor = conn.cursor()

cursor.execute('SELECT CalleeSdkName, CallerSdkName from sdkconnectionrough')

calls = []
for row in cursor.fetchall():
    callee, caller = row
    if callee == 'Facebook Audience Network':
        callee = 'Facebook'
    if caller == 'Facebook Audience Network':
        caller = 'Facebook'
    if (caller, callee) not in calls:
        calls.append((caller, callee))


conn.close()

print(len(calls))
for call in calls:
    with open("sdk_call_1to1.txt", "a") as file:
        file.write(call[0] + "->" + call[1] + "\n")


G = nx.DiGraph()
G.add_edges_from(calls)

edge_colors = {}
colors = ['red', 'green', 'blue', 'cyan', 'magenta', 'yellow', 'black'] # Extend this list as needed

# Assign colors to edges based on their source node
source_colors = {} # Dictionary to keep track of colors assigned to each source node
for edge in G.edges():
    source = edge[0]
    if source not in source_colors:
        # Assign the next available color to this source
        source_colors[source] = colors[len(source_colors) % len(colors)]
    # Use the source node's color for the edge
    edge_colors[edge] = source_colors[source]

# Convert edge_colors values to a list matching the order of G.edges() for drawing
edge_color_list = [edge_colors[edge] for edge in G.edges()]

plt.figure(figsize=(20, 6))
# Draw the graph with the specified edge colors
nx.draw(G, with_labels=True, node_size=100, node_color="lightblue", font_size=5, arrows=True, edge_color=edge_color_list, width=0.1, arrowsize=3)
plt.title("Call Graph with Custom Edge Colors")
plt.show()

start_nodes = [node for node in G.nodes() if G.in_degree(node) == 0]

all_paths = []
for start_node in start_nodes:
    for target_node in nx.descendants(G, start_node):
        for path in nx.all_simple_paths(G, source=start_node, target=target_node):
            all_paths.append(path)

# Since the user is interested in full sequences, let's ensure we capture the full length paths for each start node
full_length_paths = [path for path in all_paths if len(path) == max(len(p) for p in all_paths)]
print(len(all_paths))
for path in all_paths:

    path_text = ''
    for i in range(len(path)):
        if i == len(path) - 1:
            path_text += path[i]
        else:
            path_text += path[i] + '->'
    print(path_text)
    with open("sdk_call.txt", "a") as file:
        file.write(path_text + "\n")


