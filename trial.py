import json
from queue import PriorityQueue
import matplotlib.pyplot as plt
import networkx as nx

# Inline JSON data as an example
data = {
    "graph": {
      "s": [["a", 2], ["b", 3]],
      "a": [["d", 4]],
      "c": [["s", 1], ["e", 1]],
      "d": [["g", 7]],
      "b": [["d", 5], ["e", 1]],
      "e": [["d", 3], ["g", 4]],
      "g": []
    },
    "heuristic": {
      "s": 10,
      "a": 8,
      "b": 6,
      "c": 5,
      "d": 7,
      "e": 4,
      "g": 0
    },
    "population_density": {
      "s": 1,
      "a": 2,
      "b": 1,
      "c": 5,
      "d": 3,
      "e": 2,
      "g": 2
    }
}

# A* search algorithm with population density consideration
def a_star_search_with_population(graph, heuristic, population_density, start, goal):
    open_set = PriorityQueue()
    open_set.put((0, 0, start, [start], 0))
    cost_so_far = {start: 0}
    population_so_far = {start: 0}

    while not open_set.empty():
        _, current_cost, current, path, current_population = open_set.get()

        if current == goal:
            return path, current_cost, current_population

        for next_node, travel_cost in graph.get(current, []):
            new_cost = current_cost + travel_cost
            new_population = current_population + population_density[next_node]
            if next_node not in cost_so_far or new_cost < cost_so_far[next_node]:
                cost_so_far[next_node] = new_cost
                population_so_far[next_node] = new_population
                priority = new_cost + heuristic[next_node] - new_population
                open_set.put((priority, new_cost, next_node, path + [next_node], new_population))

    return "Path not found", 0, 0

# Visualization function
def visualize_path(graph, path, population_density):
    plt.figure(figsize=(12, 8))
    G = nx.DiGraph()
    for node, edges in graph.items():
        for edge in edges:
            G.add_edge(node, edge[0], weight=edge[1])
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=False, node_color='skyblue', edge_color='gray', width=1, arrowsize=20, alpha=0.5)
    path_edges = list(zip(path, path[1:]))
    nx.draw_networkx_nodes(G, pos, nodelist=path, node_color='lightgreen', node_size=500)
    nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='green', width=3, arrowsize=30)
    node_labels = {node: node for node in G.nodes()}
    population_labels = {node: f"{pop}" for node, pop in population_density.items()}
    nx.draw_networkx_labels(G, pos, labels=node_labels, font_size=14, font_weight='bold')
    nx.draw_networkx_labels(G, pos, labels=population_labels, font_size=10, verticalalignment='bottom')
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')
    plt.title('A* Path considering population density', size=15)
    plt.axis('off')
    plt.show()

# Main execution
path, path_cost, total_population = a_star_search_with_population(data['graph'], data['heuristic'], data['population_density'], 's', 'g')
print("A* Path considering population:", path)
print("Path Cost:", path_cost)
print("Total Population along path:", total_population)

# Visualize the result
visualize_path(data['graph'], path, data['population_density'])
