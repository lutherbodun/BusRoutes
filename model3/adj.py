import json
import math

# Rough conversion factor from degrees to kilometers
DEGREE_TO_KM = 111

def euclidean_distance(coord1, coord2):
    # Calculate the Euclidean distance and scale it to kilometers
    d_lon = (coord1["longitude"] - coord2["longitude"]) * DEGREE_TO_KM
    d_lat = (coord1["latitude"] - coord2["latitude"]) * DEGREE_TO_KM
    return math.sqrt(d_lon**2 + d_lat**2)

def generate_graph_adjacency_list(coordinates):
    adj_list = {}
    for node_a, coord_a in coordinates.items():
        adj_list[node_a] = []
        for node_b, coord_b in coordinates.items():
            if node_a != node_b:
                distance = euclidean_distance(coord_a, coord_b)
                # Store the distance rounded to two decimal places
                adj_list[node_a].append((node_b, round(distance, 2)))
    return adj_list

# Assuming the JSON structure is stored in a file named 'data.json'
json_file_path = 'read_from_js.json'

# Read the existing data from the JSON file
with open(json_file_path, 'r') as file:
    data = json.load(file)

# Generate the graph adjacency list based on coordinates
coordinates = data["coordinates"]
graph_adj_list = generate_graph_adjacency_list(coordinates)

# Update the data with the generated graph adjacency list
data["graph"] = graph_adj_list

# Write the updated data back to the JSON file
with open(json_file_path, 'w') as file:
    json.dump(data, file, indent=4)

print("Graph adjacency list generated and written back to the JSON file.")
