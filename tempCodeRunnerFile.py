from queue import PriorityQueue
import json

def a_star_search_with_time_cost_and_traversal(graph, heuristic, start, goal):
    open_set = PriorityQueue()
    # Initial node has a heuristic value, cost of 0, the start node, an empty path, and time cost of 0
    open_set.put((heuristic[start], 0, start, [start], 0))  # Added initial time cost as 0
    cost_so_far = {start: 0}
    time_so_far = {start: 0}  # Tracks time cost so far
    traversal_path = []  # Tracking the order of node exploration

    while not open_set.empty():
        _, current_cost, current, path, current_time_cost = open_set.get()

        if current not in traversal_path:
            traversal_path.append(current)

        if current == goal:
            return path, traversal_path, current_cost, current_time_cost

        for next, next_info in graph.get(current, []):
            next_cost, next_time_cost = next_info
            new_cost = current_cost + next_cost
            total_time_cost = current_time_cost + next_time_cost  # Calculate total time spent
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                time_so_far[next] = total_time_cost
                priority = new_cost + heuristic[next]
                open_set.put((priority, new_cost, next, path + [next], total_time_cost))
    
    return "Path not found", traversal_path, 0, 0

# Example graph with added average time spent at each node and coordinates
graph = {
    's': [('a', (2, 3)), ('b', (3, 2))],  # (cost, time)
    'a': [('d', (4, 5))],
    'b': [('d', (5, 2)), ('e', (1, 3))],
    'd': [('g', (7, 8))],
    'e': [('g', (4, 2))],
    'g': []  # Goal node
}

heuristic = {
    's': 10,
    'a': 8,
    'b': 6,
    'd': 7,
    'e': 4,
    'g': 0
}

path, traversal_path, path_cost, total_time_cost = a_star_search_with_time_cost_and_traversal(graph, heuristic, 's', 'g')
print("A* Path:", path)
print("Traversal Path:", traversal_path)
print("Path Cost:", path_cost)
print("Total Time Cost:", total_time_cost)

# Sample JSON data generation
node_data = {
    's': {'coordinates': {'lon': -79.39, 'lat': 43.70}, 'average_time': 3, 'population_density': 1},
    'a': {'coordinates': {'lon': -79.38, 'lat': 43.71}, 'average_time': 5, 'population_density': 2},
    'b': {'coordinates': {'lon': -79.37, 'lat': 43.72}, 'average_time': 2, 'population_density': 9},
    'd': {'coordinates': {'lon': -79.36, 'lat': 43.73}, 'average_time': 8, 'population_density': 3},
    'e': {'coordinates': {'lon': -79.35, 'lat': 43.74}, 'average_time': 2, 'population_density': 4},
    'g': {'coordinates': {'lon': -79.34, 'lat': 43.75}, 'average_time': 0, 'population_density': 0},
}

with open('node_data.json', 'w') as json_file:
    json.dump(node_data, json_file, indent=4)

print("JSON data for nodes saved to 'node_data.json'.")
