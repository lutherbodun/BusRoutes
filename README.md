🛣️🚌
A* Algorithm for Bus Transportation Optimization 

To run the program: 
Go to the model3 folder in the project’s directory and run the main program of the project using the command “python main.py” in the terminal (Model3->main.py).

Step 1: 
With the help of extract.py program coordinates are extracted from the CSV file of Transit Windsor Bus Stops and assigned to the read_from_js.json file.

Step 2: 
The graph data structure, which is in the form of an adjacency list is generated using adj.py program based on the coordinates data and is also assigned to the read_from_js.json file.

Step 3:
The node_positions are generated using the pass.py program based on the graph data and assigned to the read_from_js.json file so that nodes can be visible on the computer screen ratio.

Step 4:
The heuristics and population are generated using the auxi.py program and assigned to the read_from_js.json file.

Step 5:
The entire set of graph, node positions, heuristics, and population data is read from the read_from_js.json file and the A* algorithm is implemented on the set. The simulation of the optimal path is output to the screen based on specific source-destination data.

![image](https://github.com/lutherbodun/BusRoutes/assets/112750375/3fcc26b9-c3a8-4d2d-a9e8-25b6b9b5cfdb)

According to the algorithm, the population-to-path cost ratio of each node is calculated at each level of the graph, and the minimum value at each level is added to the optimal path throughout its traversal. The population data is negated initially as the minimum population-to-path cost ratio is taken into account since the algorithm is built on the generic a-star search algorithm where the minimum value should be tracked at every level of the graph and the higher population is taken into consideration at the same time because the purpose of the algorithm is to serve more people with lower path cost at the same time. 

