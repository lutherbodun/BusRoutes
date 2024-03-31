import json
import math


def euclidean_distance(coord1, coord2):
    # Calculate the Euclidean distance and scale it as if it's in kilometers
    # This scaling is arbitrary and should be adjusted based on your actual data's scale
    scale_factor = 100000
    distance = math.sqrt((coord1["longitude"] - coord2["longitude"])
                         ** 2 + (coord1["latitude"] - coord2["latitude"])**2)
    scaled_distance = round(distance * scale_factor, 2)
    return scaled_distance


def generate_graph_adjacency_list(coordinates):
    adj_list = {}
    for node_a in coordinates:
        for node_b in coordinates:
            if node_a != node_b:
                distance = euclidean_distance(
                    coordinates[node_a], coordinates[node_b])
                if node_a not in adj_list:
                    adj_list[node_a] = []
                adj_list[node_a].append((node_b, distance))
    return adj_list


def adjust_node_positions(node_positions):
    # Here we adjust the node positions directly based on your existing logic
    # For visualization on a screen, you would likely need to further adapt this
    return {node: [round(pos[0], 2), round(pos[1], 2)] for node, pos in node_positions.items()}


file_path = 'temp.json'

# Load the existing data from the JSON file
with open(file_path, 'r') as file:
    data = json.load(file)

# Generate graph adjacency list based on coordinates
coordinates = data["coordinates"]
graph_adj_list = generate_graph_adjacency_list(coordinates)
data["graph"] = graph_adj_list

# Adjust node positions for visualization
data["node_positions"] = adjust_node_positions(data["node_positions"])

# Save the updated data back to the JSON file
with open(file_path, 'w') as file:
    json.dump(data, file, indent=4)

print("Graph adjacency list and node positions updated and saved to JSON file successfully.")
