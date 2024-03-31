import json
import random

# Given JSON data
with open('read_from_js.json', 'r') as file:
    data = json.load(file)


# Generate random heuristic values
# Assuming the goal is to minimize the heuristic, and 'goal' has a heuristic of 0
def generate_random_heuristics(nodes, goal_node='goal'):
    heuristics = {node: random.randint(1, 10) for node in nodes}
    heuristics[goal_node] = 0  # The heuristic value for the goal is always 0
    return heuristics

# Generate random population density
# Assuming a population density range from 1 to 5


def generate_random_population_density(nodes):
    return {node: random.randint(1, 5) for node in nodes}


# Retrieve the list of nodes from the graph
nodes = list(data['coordinates'].keys())

# Add random heuristics and population densities to the data
data['heuristic'] = generate_random_heuristics(nodes)
data['population_density'] = generate_random_population_density(nodes)

# Print the new sections of the data
print("Random Heuristics:")
print(json.dumps(data['heuristic'], indent=4))
print("\nRandom Population Density:")
print(json.dumps(data['population_density'], indent=4))

# Now, let's write the complete data back to a JSON file
json_file_path = 'read_from_js.json'
with open(json_file_path, 'w') as file:
    json.dump(data, file, indent=4)

print(f"Updated data written to {json_file_path}.")


# making population density negative
# Path to the JSON file
json_file_path = 'read_from_js.json'

# Load the existing data from the JSON file
with open(json_file_path, 'r') as file:
    data = json.load(file)

# Check if 'population_density' key exists in the data
if 'population_density' in data:
    # Iterate over each key in 'population_density' and make the value negative
    for key in data['population_density']:
        data['population_density'][key] = -abs(data['population_density'][key])

    # Write the updated data back to the JSON file
    with open(json_file_path, 'w') as file:
        json.dump(data, file, indent=4)

    print("Population density values have been made negative and saved back to the JSON file.")
else:
    print("The key 'population_density' was not found in the JSON data.")
