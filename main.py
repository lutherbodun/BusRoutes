from queue import PriorityQueue

def a_star_search_with_cost_and_traversal(graph, heuristic, start, goal):
    open_set = PriorityQueue()
    open_set.put((heuristic[start], 0, start, [start]))
    cost_so_far = {start: 0}
    traversal_path = []  # tracking the order of node exploration

    while not open_set.empty():
        _, current_cost, current, path = open_set.get()

        if current not in traversal_path:
            traversal_path.append(current)

        if current == goal:
            return path, traversal_path, current_cost  # return path, traversal path, and total path cost

        for next, next_cost in graph.get(current, []):
            new_cost = current_cost + next_cost
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + heuristic[next]
                open_set.put((priority, new_cost, next, path + [next]))
    
    return "Path not found", traversal_path, 0

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

path, traversal_path, path_cost = a_star_search_with_cost_and_traversal(graph, heuristic, 's', 'g')
print("A* Path:", path)
print("Traversal Path:", traversal_path)
print("Path Cost:", path_cost)
