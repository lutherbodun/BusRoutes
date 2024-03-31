import json
import math

# Load the existing data from the JSON file
with open('read_from_js.json', 'r') as file:
    data = json.load(file)

graph = data["graph"]
node_keys = list(graph.keys())

# Number of nodes
N = len(node_keys)

# Calculate positions (arrange nodes in a circle for visualization)
radius = 200  # Radius of the circle on which nodes will be positioned
center_x, center_y = 0, 0  # Center of the circle
angle = 360 / N  # Angle between nodes

node_positions = {}
for i, node in enumerate(node_keys):
    theta = math.radians(angle * i)
    x = center_x + radius * math.cos(theta)
    y = center_y + radius * math.sin(theta)
    node_positions[node] = (x, y)

# Update the JSON data with the calculated node positions
data["node_positions"] = node_positions

# Save the updated data back to the JSON file
with open('read_from_js.json', 'w') as file:
    json.dump(data, file, indent=4)

print("Node positions added to JSON file successfully.")
