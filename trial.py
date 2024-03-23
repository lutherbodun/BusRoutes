from queue import PriorityQueue
# graph = {
#     's': [('a', 2), ('b', 3)],
#     'a': [('c', 2), ('d', 3)],
#     'b': [('d', 1), ('e', 4)],
#     'c': [('g', 4)],
#     'd': [('g', 2)],
#     'e': [('g', 1)],
#     'g': []
# }

# heuristic = {
#     's': 7,
#     'a': 6,
#     'b': 2,
#     'c': 4,
#     'd': 2,
#     'e': 1,
#     'g': 0
# }

# population_density = {
#     's': 1,
#     'a': 2,
#     'b': 2,
#     'c': 5,
#     'd': 2,
#     'e': 3,
#     'g': 0
# }
import json
from queue import PriorityQueue

# Read data from JSON file
with open('read_from_js.json', 'r') as file:
    data = json.load(file)

# Assign values from JSON
graph = data["graph"]
heuristic = data["heuristic"]
population_density = data["population_density"]

def a_star_search_with_population_ratio(graph, heuristic, population_density, start, goal):
    open_set = PriorityQueue()
    # Initialize with the start node; priority now considers the population density to path cost ratio
    # The ratio is initialized to be as high as possible (using negative for sorting in priority queue)
    open_set.put((-float('inf'), 0, start, [start], 0))  # Initial population density is 0
    cost_so_far = {start: 0}
    best_ratio_so_far = {start: -float('inf')}  # Using negative for best ratio initialization

    while not open_set.empty():
        current_ratio, current_cost, current, path, current_population = open_set.get()

        if current == goal:
            return path, current_cost, current_population / current_cost if current_cost > 0 else float('inf')

        for next_node, travel_cost in graph.get(current, []):
            new_cost = current_cost + travel_cost
            new_population = current_population + population_density[next_node]
            new_ratio = -new_population / new_cost if new_cost > 0 else -float('inf')  # Maintain negative for sorting
            
            if next_node not in cost_so_far or new_ratio > best_ratio_so_far[next_node]:
                cost_so_far[next_node] = new_cost
                best_ratio_so_far[next_node] = new_ratio
                priority = (new_ratio, new_cost + heuristic[next_node], next_node, path + [next_node], new_population)
                open_set.put(priority)

    return "Path not found", 0, float('inf')

# Load your graph, heuristic, and population_density from 'read_from_js.json' as before
# graph, heuristic, population_density = load_your_data()

# Execute the modified A* search
path, path_cost, population_ratio = a_star_search_with_population_ratio(graph, heuristic, population_density, 's', 'g')
print("Optimal Path considering population density to path cost ratio:", path)
print("Path Cost:", path_cost)
print("Population Density to Path Cost Ratio:", -population_ratio)  # Negating ratio for correct sign



import turtle

# Setup the window
wn = turtle.Screen()
wn.bgcolor("white")
wn.title("A* Pathfinding with Population Ratio")
wn.setup(width=700, height=700)

# Create a turtle for drawing the grid and paths
drawer = turtle.Turtle()
drawer.speed(0)  # fastest drawing speed
drawer.hideturtle()
