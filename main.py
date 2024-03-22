import json
from queue import PriorityQueue

# Read data from JSON file
with open('read_from_js.json', 'r') as file:
    data = json.load(file)

# Assign values from JSON
graph = data["graph"]
heuristic = data["heuristic"]
population_density = data["population_density"]

def a_star_search_with_population(graph, heuristic, population_density, start, goal):
    open_set = PriorityQueue()
    # Initialize the open set with the start node, incorporating population density into the priority calculation
    open_set.put((0, 0, start, [start], 0))  # Last zero is the initial cumulative population density
    cost_so_far = {start: 0}
    population_so_far = {start: 0}  # Start with zero and accumulate population density along the path

    while not open_set.empty():
        _, current_cost, current, path, current_population = open_set.get()

        if current == goal:
            # Return the path, the traversal order, total path cost, and total population along the path
            return path, current_cost, current_population

        for next_node, travel_cost in graph.get(current, []):
            new_cost = current_cost + travel_cost
            new_population = current_population + population_density[next_node]  # Accumulate population density
            if next_node not in cost_so_far or new_cost < cost_so_far[next_node]:
                cost_so_far[next_node] = new_cost
                population_so_far[next_node] = new_population
                # Adjust the priority calculation to include population density
                priority = new_cost + heuristic[next_node] - new_population  # Example adjustment
                open_set.put((priority, new_cost, next_node, path + [next_node], new_population))

    return "Path not found", 0, 0

# Execute the A* search with consideration for population density
path, path_cost, total_population = a_star_search_with_population(graph, heuristic, population_density, 's', 'g')
print("A* Path considering population:", path)
print("Path Cost:", path_cost)
print("Total Population along path:", total_population)
