import json
from queue import PriorityQueue

# Mockup JSON data for demonstration
# Read data from JSON file
with open('read_from_js.json', 'r') as file:
    data = json.load(file)

# Replace this with reading from a file in actual implementation
# with open('read_from_js.json', 'r') as file:
#     data = json.load(file)

graph = data["graph"]
heuristic = data["heuristic"]
population_density = data["population_density"]

def a_star_search_with_population(graph, heuristic, population_density, start, goal):
    open_set = PriorityQueue()
    open_set.put((0, 0, start, [start], 0))  # Priority, cost so far, current node, path, population/cost ratio
    cost_so_far = {start: 0}
    population_ratio_so_far = {start: 0}

    while not open_set.empty():
        _, current_cost, current, path, current_ratio = open_set.get()

        if current == goal:
            return path, current_cost, current_ratio

        for next_node, travel_cost in graph.get(current, []):
            new_cost = current_cost + travel_cost
            new_ratio = (population_density[next_node] + population_density[current]) / new_cost if new_cost else float('inf')
            
            if next_node not in cost_so_far or new_ratio > population_ratio_so_far.get(next_node, 0):
                cost_so_far[next_node] = new_cost
                population_ratio_so_far[next_node] = new_ratio
                priority = new_cost + heuristic[next_node] - new_ratio  # Adjust priority based on ratio
                open_set.put((priority, new_cost, next_node, path + [next_node], new_ratio))

    return "Path not found", 0, 0

path, path_cost, total_population_ratio = a_star_search_with_population(graph, heuristic, population_density, 's', 'g')
print("A* Path considering population to cost ratio:", path)
print("Path Cost:", path_cost)
print("Total Population to Cost Ratio along path:", total_population_ratio)
