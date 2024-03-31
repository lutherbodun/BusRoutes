import json
import math
import random

# Rough conversion factor from degrees to kilometers
DEGREE_TO_KM = 111

def euclidean_distance(coord1, coord2):
    # Calculate the Euclidean distance and scale it to kilometers
    d_lon = (coord1["longitude"] - coord2["longitude"]) * DEGREE_TO_KM
    d_lat = (coord1["latitude"] - coord2["latitude"]) * DEGREE_TO_KM
    return math.sqrt(d_lon**2 + d_lat**2)

def generate_graph_adjacency_list_with_random_connections(coordinates):
    adj_list = {}
    for node_a, coord_a in coordinates.items():
        all_possible_connections = [
            (node_b, round(euclidean_distance(coord_a, coord_b), 2))
            for node_b, coord_b in coordinates.items() if node_a != node_b
        ]
        # Determine a random number of connections for this node
        num_connections = random.randint(1, len(all_possible_connections))
        # Randomly select connections to add to this node
        adj_list[node_a] = random.sample(all_possible_connections, num_connections)
    return adj_list

# Assuming the coordinates are defined in your data structure
# For demonstration purposes, let's assume you have a 'coordinates' dictionary already available

# Example coordinates for demonstration; replace with `data["coordinates"]` in your actual code
with open('read_from_js.json', 'r') as file:
    data = json.load(file)

# Generate the graph adjacency list based on coordinates
coordinates = data["coordinates"]

# Generate the graph adjacency list with random connections
graph_adj_list_with_random_connections = generate_graph_adjacency_list_with_random_connections(coordinates)

# Here you would follow with the JSON reading and writing logic as before
# Update your 'data' structure accordingly
data["graph"] = graph_adj_list_with_random_connections

# Write the updated data back to the JSON file
json_file_path = 'read_from_js.json'
with open(json_file_path, 'w') as file:
    json.dump(data, file, indent=4)

print("Graph adjacency list with random connections generated and written back to the JSON file.")
