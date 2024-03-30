import json
import math

def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1["longitude"] - coord2["longitude"])**2 + (coord1["latitude"] - coord2["latitude"])**2)

def generate_graph_adjacency_list(coordinates):
    adj_list = {}
    for node_a in coordinates:
        for node_b in coordinates:
            if node_a != node_b:
                distance = euclidean_distance(coordinates[node_a], coordinates[node_b])
                if node_a not in adj_list:
                    adj_list[node_a] = []
                adj_list[node_a].append((node_b, distance))
    return adj_list

# Load the existing data from the JSON file
with open('temp.json', 'r') as file:
    data = json.load(file)

# Generate graph adjacency list based on coordinates
coordinates = data["coordinates"]
graph_adj_list = generate_graph_adjacency_list(coordinates)

# Update the graph in the data with the generated adjacency list
data["graph"] = graph_adj_list

node_keys = list(data["graph"].keys())

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
    node_positions[node] = [x, y]

# Update the JSON data with the calculated node positions
data["node_positions"] = node_positions

# Save the updated data back to the JSON file
with open('temp.json', 'w') as file:
    json.dump(data, file, indent=4)

print("Graph adjacency list and node positions added to JSON file successfully.")
