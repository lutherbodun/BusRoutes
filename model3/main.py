import turtle
import json
import auxi
from queue import PriorityQueue

# # tob extract the coordinates from csv file dbms
with open('extract.py', 'r') as file:
    exec(file.read())

# to create graph from coordinates
with open('adj.py', 'r') as file:
    exec(file.read())

# to create node pos for UI
with open('pass.py', 'r') as file:
    exec(file.read())

# to create heuristics and population data
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


from queue import PriorityQueue

def a_star_search_with_population(graph, heuristic, population_density, start, goal):
    open_set = PriorityQueue()
    open_set.put((0, start, [start], 0))  # Priority, current node, path, cumulative population density
    cost_so_far = {start: 0}
    population_so_far = {start: population_density[start]}  # Initialize with the starting node's population density

    while not open_set.empty():
        _, current, path, current_population = open_set.get()

        if current == goal:
            return path, cost_so_far[current], current_population / cost_so_far[current] if cost_so_far[current] else float('inf')

        for next_node, travel_cost in graph.get(current, []):
            new_cost = cost_so_far[current] + travel_cost
            new_population = current_population + population_density[next_node]
            new_ratio = new_population / new_cost if new_cost else float('inf')

            if next_node not in cost_so_far or new_cost < cost_so_far[next_node] or new_ratio < (population_so_far[next_node] / cost_so_far[next_node] if next_node in population_so_far else float('inf')):
                cost_so_far[next_node] = new_cost
                population_so_far[next_node] = new_population
                priority = new_cost + heuristic[next_node] - new_ratio  # Adjusting priority calculation to consider heuristic and population density
                open_set.put((priority, next_node, path + [next_node], new_population))

    return "Path not found", 0, 0

# Example usage with the provided data structures...

# Assuming turtle setup and draw functions are defined as before
# Turtle setup
turtle.setup(width=600, height=600)
t = turtle.Turtle()
t.speed('fast')

# Function to draw nodes as circles with labels
def draw_nodes(t, node_positions):
    for node, (x, y) in node_positions.items():
        t.penup()
        t.goto(x, y - 20)  # Position the turtle below the node center
        t.pendown()
        t.circle(30)  # Draw a circle for the node
        t.penup()
        t.goto(x, y - 5)  # Position the turtle to write the label
        t.write(node, align="center", font=("Arial", 16, "bold"))

# Function to draw edges as lines between nodes


def draw_edges_with_costs(t, graph, node_positions):
    for node, edges in graph.items():
        for edge, cost in edges:
            # Calculate the midpoint for the cost label
            start_pos = node_positions[node]
            end_pos = node_positions[edge]
            midpoint = ((start_pos[0] + end_pos[0]) / 2, (start_pos[1] + end_pos[1]) / 2)
            
            # Draw the edge
            t.penup()
            t.goto(start_pos)
            t.pendown()
            t.goto(end_pos)
            
            # Draw the cost label near the midpoint in bold
            t.penup()
            t.goto(midpoint[0], midpoint[1] - 10)  # Adjust as needed for visibility
            t.pendown()
            t.write(str(cost), align="center", font=("Arial", 8, "bold"))  # Font style set to bold



# Main execution
screen = turtle.Screen()
screen.title("A* Path Considering Population Density")
draw_nodes(t, node_positions)
draw_edges_with_costs(t, data['graph'], node_positions)

# Perform A* search
search_results = a_star_search_with_population(
    data['graph'], data['heuristic'], data['population_density'], 'Transit Terminal & Chatham', 'Canada Customs & Duty Free')

# Execute the modified A* search
path, path_cost, total_population_ratio = a_star_search_with_population(
    graph, heuristic, population_density, 'Transit Terminal & Chatham', 'Canada Customs & Duty Free')
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
