from queue import PriorityQueue

def a_star_search_with_max_pop(graph, heuristic, population_density, start, goal):
    open_set = PriorityQueue()
    # Adding total population to the stored data in the priority queue
    open_set.put((heuristic[start], 0, start, [start], 0))  # Initial total population is 0
    cost_so_far = {start: 0}
    max_pop_so_far = {start: population_density[start]}  # Track max population for each path
    traversal_path = []  # tracking the order of node exploration

    while not open_set.empty():
        _, current_cost, current, path, current_pop = open_set.get()

        if current not in traversal_path:
            traversal_path.append(current)

        if current == goal:
            return path, traversal_path, current_cost, current_pop  # Also return total population along the path

        for next, next_cost in graph.get(current, []):
            new_cost = current_cost + next_cost
            new_pop = current_pop + population_density[next]  # Update the population for the path
            if next not in cost_so_far or new_cost < cost_so_far[next] or (new_cost == cost_so_far[next] and new_pop > max_pop_so_far.get(next, 0)):
                cost_so_far[next] = new_cost
                max_pop_so_far[next] = new_pop  # Update the max population for this path
                priority = new_cost + heuristic[next]
                open_set.put((priority, new_cost, next, path + [next], new_pop))
    
    return "Path not found", traversal_path, 0, 0  # Also return 0 for total population if path not found

graph = {
    's': [('a', 2), ('b', 3)],
    'a': [('d', 4)],
    'c': [('s', 1), ('e', 1)],
    'd': [('g', 7)],
    'b': [('d', 5), ('e', 1)],
    'e': [('d', 3), ('g', 4)],
    'g': []  # Goal node
}

heuristic = {
    's': 10,
    'a': 8,
    'b': 6,
    'c': 5,
    'd': 7,
    'e': 4,
    'g': 0
}
population_density = {
    's': 1,
    'a': 2,
    'b': 9,
    'c': 5,
    'd': 3,
    'e': 4,
    'g': 0
}
# Using the same graph, heuristic, and introducing population_density from the provided dictionaries.
path, traversal_path, path_cost, max_pop = a_star_search_with_max_pop(graph, heuristic, population_density, 's', 'g')
print("A* Path:", path)
print("Traversal Path:", traversal_path)
print("Path Cost:", path_cost)
print("Max Population:", max_pop)
