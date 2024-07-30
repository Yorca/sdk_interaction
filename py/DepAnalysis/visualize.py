from networkx.drawing.nx_pydot import read_dot
from networkx.drawing.nx_agraph import to_agraph
import networkx as nx
import matplotlib.pyplot as plt

dot = read_dot('call_graph.dot')
print(dot)


# Draw the graph
pos = nx.spring_layout(dot)  # positions for all nodes
nx.draw(dot, pos, with_labels=True, node_color='lightblue', node_size=500, edge_color='gray')
plt.show()