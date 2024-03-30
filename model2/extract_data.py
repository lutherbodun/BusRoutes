import json
import networkx as nx
import matplotlib.pyplot as plt

# Load the graph data from the JSON file
with open('temp.json', 'r') as file:
    data = json.load(file)

# Create a graph object
G = nx.Graph()

# Add nodes with positions
for node, pos in data["node_positions"].items():
    G.add_node(node, pos=pos)

# Add edges from the adjacency list
for node, edges in data["graph"].items():
    for edge in edges:
        G.add_edge(node, edge[0], weight=edge[1])

# Extract positions
pos = {node: data["node_positions"][node] for node in G.nodes()}

# Draw the graph
nx.draw(G, pos, with_labels=True, node_size=700, node_color="lightblue", font_size=10, font_weight="bold")

# Show plot
plt.show()
