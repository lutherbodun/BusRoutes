import turtle
import json
import auxi
from queue import PriorityQueue


with open('auxi.py', 'r') as file:
    exec(file.read())

# Inline JSON data as an example
with open('read_from_js.json', 'r') as file:
    data = json.load(file)

# Replace this with reading from a file in actual implementation
# with open('read_from_js.json', 'r') as file:
#     data = json.load(file)

graph = data["graph"]
heuristic = data["heuristic"]
population_density = data["population_density"]
node_positions = data.get("node_positions", {})


def a_star_search_with_population(graph, heuristic, population_density, start, goal):
    open_set = PriorityQueue()
    # Priority now only for initialization, path, and cumulative population density
    open_set.put((0, start, [start], 0))
    cost_so_far = {start: 0}
    best_ratio_so_far = {start: 0}

    while not open_set.empty():
        _, current, path, current_population = open_set.get()

        if current == goal:
            return path, cost_so_far[current], current_population / cost_so_far[current]

        for next_node, travel_cost in graph.get(current, []):
            new_cost = cost_so_far[current] + travel_cost
            new_population = current_population + population_density[next_node]
            new_ratio = new_population / new_cost if new_cost else float('inf')

            if next_node not in cost_so_far or new_cost < cost_so_far[next_node]:
                cost_so_far[next_node] = new_cost
                best_ratio_so_far[next_node] = new_ratio
                priority = -new_ratio  # We negate the ratio to turn max-heap behavior into min-heap
                open_set.put((priority, next_node, path +
                             [next_node], new_population))

    return "Path not found", 0, 0


# Assuming turtle setup and draw functions are defined as before
# Turtle setup
turtle.setup(width=600, height=600)
t = turtle.Turtle()
t.speed('fast')
# node_positions = {
#     "s": (-200, 100),
#     "a": (-100, 150),
#     "b": (-100, 50),
#     "c": (0, 0),
#     "d": (100, 100),
#     "e": (50, -50),
#     "g": (200, 0)
# }


# Function to draw nodes as circles with labels
def draw_nodes(t, node_positions):
    for node, (x, y) in node_positions.items():
        t.penup()
        t.goto(x, y - 20)  # Position the turtle below the node center
        t.pendown()
        t.circle(30)  # Draw a circle for the node
        t.penup()
        t.goto(x, y - 5)  # Position the turtle to write the label
        t.write(node, align="center", font=("Arial", 12, "bold"))

# Function to draw edges as lines between nodes


def draw_edges(t, graph, node_positions):
    for node, edges in graph.items():
        for edge, _ in edges:
            t.penup()
            t.goto(node_positions[node])
            t.pendown()
            t.goto(node_positions[edge])


# Main execution
screen = turtle.Screen()
screen.title("A* Path Considering Population Density")
draw_nodes(t, node_positions)
draw_edges(t, data['graph'], node_positions)

# Perform A* search
search_results = a_star_search_with_population(
    data['graph'], data['heuristic'], data['population_density'], 's', 'g')

# Execute the modified A* search
path, path_cost, total_population_ratio = a_star_search_with_population(
    graph, heuristic, population_density, 's', 'g')
print("A* Path considering population to cost ratio:", path)
print("Path Cost:", path_cost)
# Define node positions for turtle graphics (adjusted to fit your screen and look good)
print("Population to Cost Ratio along path:", total_population_ratio)

# # Draw the final path
# path, path_cost, total_population = next(search_results)
# print("A* Path considering population:", path)
# print("Path Cost:", path_cost)
# print("Total Population along path:", total_population)

# Function to draw the final path with a different color


def draw_final_path(t, path, node_positions):
    t.pencolor('green')
    t.pensize(3)
    for i in range(len(path) - 1):
        t.penup()
        t.goto(node_positions[path[i]])
        t.pendown()
        t.goto(node_positions[path[i+1]])


draw_final_path(t, path, node_positions)

# Hide the turtle cursor and finish
t.hideturtle()
turtle.done()
