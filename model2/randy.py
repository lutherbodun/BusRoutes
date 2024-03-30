import json
import random

# Function to generate random population density values
def generate_random_population_density(nodes, max_density=10):
    # Return negative population densities
    return {node: -random.randint(1, max_density) for node in nodes}

# Function to generate random heuristic values
def generate_random_heuristics(graph, population_density, scale_factor=1):
    heuristics = {}
    for node in graph:
        # The heuristic is a random value; it does not use population density in this case.
        heuristics[node] = round(random.uniform(1, scale_factor), 2)
    return heuristics

# Path to the JSON file
file_path = 'test.json'

# Read 'graph' from the JSON file
try:
    with open(file_path, 'r') as file:
        data = json.load(file)
        graph = data.get("graph", {})
except FileNotFoundError as e:
    print(f"An error occurred while reading the file: {e}")
else:
    # Generate random population density
    population_density = generate_random_population_density(graph.keys())

    # Generate random heuristic values based on the randomly generated population density
    heuristics = generate_random_heuristics(graph, population_density, scale_factor=10)

    # Print the random negative population density and heuristics
    print("Random Negative Population Density:")
    print(json.dumps(population_density, indent=4))
    print("\nRandom Heuristics:")
    print(json.dumps(heuristics, indent=4))

    # Optionally, save the generated data back to the JSON file
    data["population_density"] = population_density
    data["heuristic"] = heuristics
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)
