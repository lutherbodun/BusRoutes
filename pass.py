import json

# Load the graph data from a JSON file
with open('temp.json', 'r') as file:
    data = json.load(file)

graph = data['graph']

# Initialize positions with the source node and a set for visited nodes
positions = {'source': (0, 0)}
visited = {'source'}

# Function to place nodes
def place_nodes(node, x_offset=100, y_offset=100, level=0):
    if node not in graph:
        return
    
    for adj_node, weight in graph[node]:
        if adj_node not in visited:
            visited.add(adj_node)
            x = positions[node][0] + (level + 1) * x_offset * weight
            # Alternates placement up and down from the source line
            y = positions[node][1] + ((level % 2) * 2 - 1) * y_offset * weight
            positions[adj_node] = (x, y)
            place_nodes(adj_node, x_offset, y_offset, level + 1)

# Start placing nodes from the source
place_nodes('source')

# Update the original data with new positions
data['node_positions'] = {node: list(pos) for node, pos in positions.items()}

# Write the updated data back to the JSON file
with open('updated_graph_data.json', 'w') as file:
    json.dump(data, file, indent=4)

print("Updated node positions have been saved to 'updated_graph_data.json'.")
