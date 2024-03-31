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

def generate_directed_graph_adjacency_list(coordinates):
    adj_list = {}
    for node_a, coord_a in coordinates.items():
        adj_list[node_a] = []
        
    # Create a list of all possible edges
    all_edges = [(node_a, node_b) for node_a in coordinates for node_b in coordinates if node_a != node_b]
    
    # Randomly choose a direction for each edge
    for edge in all_edges:
        if random.choice([True, False]):
            # Add edge A -> B
            distance = euclidean_distance(coordinates[edge[0]], coordinates[edge[1]])
            adj_list[edge[0]].append((edge[1], round(distance, 2)))
        else:
            # Add edge B -> A
            distance = euclidean_distance(coordinates[edge[1]], coordinates[edge[0]])
            adj_list[edge[1]].append((edge[0], round(distance, 2)))
            
    return adj_list

# Assuming the JSON structure is stored in a file named 'read_from_js.json'
json_file_path = 'read_from_js.json'

# Read the existing data from the JSON file
with open(json_file_path, 'r') as file:
    data = json.load(file)

# Generate the directed graph adjacency list based on coordinates
coordinates = data["coordinates"]
directed_graph_adj_list = generate_directed_graph_adjacency_list(coordinates)

# Update the data with the generated directed graph adjacency list
data["graph"] = directed_graph_adj_list

# Write the updated data back to the JSON file
with open(json_file_path, 'w') as file:
    json.dump(data, file, indent=4)

print("Directed graph adjacency list generated and written back to the JSON file.")
