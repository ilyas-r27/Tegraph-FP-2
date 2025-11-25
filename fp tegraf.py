import sys

# Use float('inf') to represent infinity
inf = float('inf')

# 1. INPUT DATASET
# ----------------------------------------------------
# List of station names (Nodes)
nodes = ["SGU", "WO", "SDA", "BG", "LW", "ML", "MR", "KTS", "KD", "BL"]

# 10x10 Adjacency Matrix (Edges & Weights)
# This is the dataset the algorithm will use.
graph = [
    #      SGU,   WO,  SDA,   BG,   LW,   ML,   MR,  KTS,   KD,   BL
    [      0,  5.8,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf],  # SGU
    [    5.8,    0, 17.6,  inf,  inf,  inf, 38.0,  inf,  inf,  inf],  # WO
    [    inf, 17.6,    0, 21.5,  inf,  inf,  inf,  inf,  inf,  inf],  # SDA
    [    inf,  inf, 21.5,    0, 40.5,  inf,  inf,  inf,  inf,  inf],  # BG
    [    inf,  inf,  inf, 40.5,    0, 18.6,  inf,  inf,  inf,  inf],  # LW
    [    inf,  inf,  inf,  inf, 18.6,    0,  inf,  inf,  inf, 58.2],  # ML
    [    inf, 38.0,  inf,  inf,  inf,  inf,    0, 42.9,  inf,  inf],  # MR
    [    inf,  inf,  inf,  inf,  inf,  inf, 42.9,    0, 25.2,  inf],  # KTS
    [    inf,  inf,  inf,  inf,  inf,  inf,  inf, 25.2,    0, 54.8],  # KD
    [    inf,  inf,  inf,  inf,  inf, 58.2,  inf,  inf, 54.8,    0]   # BL  
]
# ----------------------------------------------------


def dijkstra(graph, start_node_index):
    """
    Implementation of Dijkstra's Algorithm using an Adjacency Matrix.
    """
    num_nodes = len(graph)
    
    # Initialize "memory" arrays
    # distances: Stores the shortest distance from 'start' to every node
    # visited: Marks nodes that have been processed
    # previous_nodes: Stores the "parent" of a node in the shortest path
    distances = [inf] * num_nodes
    visited = [False] * num_nodes
    previous_nodes = [-1] * num_nodes  # -1 means no parent

    # Distance from the start node to itself is 0
    distances[start_node_index] = 0

    # Main algorithm: loop for each node
    for _ in range(num_nodes):
        
        # 1. Select the 'unvisited' node with the 'smallest distance'
        min_dist = inf
        u = -1  # u is the index of the current smallest node

        for i in range(num_nodes):
            if not visited[i] and distances[i] < min_dist:
                min_dist = distances[i]
                u = i

        # If no reachable node is left, 'u' will remain -1. Break.
        if u == -1:
            break
            
        # 2. Mark node 'u' as 'visited'
        visited[u] = True

        # 3. "Relaxation" process: Update distances of 'u's neighbors
        for v in range(num_nodes):
            # Check if 'v' is a neighbor (distance > 0) and not yet visited
            if graph[u][v] > 0 and not visited[v]:
                
                # Calculate the new distance: distance to 'u' + distance from 'u' to 'v'
                new_dist = distances[u] + graph[u][v]
                
                # If the new distance is shorter than the one in 'memory'
                if new_dist < distances[v]:
                    # Update the 'memory'
                    distances[v] = new_dist
                    previous_nodes[v] = u  # Record that the shortest path to 'v' is now via 'u'

    return distances, previous_nodes


def get_path(previous_nodes, node_names, start_index, end_index):
    """
    Helper function to reconstruct the path from the 'previous_nodes' array.
    """
    path = []
    current_index = end_index
    
    # Trace back from 'end' to 'start'
    while current_index != -1:
        path.append(node_names[current_index])
        current_index = previous_nodes[current_index]
    
    # The resulting path will be reversed (e.g., [ML, LW, BG, SDA, WO, SGU])
    path.reverse()
    
    # Check if the path is valid (starts with the start node)
    if path[0] == node_names[start_index]:
        return " -> ".join(path)
    else:
        return "No path"

# --- PROGRAM EXECUTION ---

# Define the starting station (source)
start_station = "SGU"
start_index = nodes.index(start_station)

# Run Dijkstra's Algorithm
distances, prev_nodes = dijkstra(graph, start_index)

# Print the results in a clean table format
print(f"========= DIJKSTRA'S ALGORITHM RESULTS =========\n")
print(f"Start Station (Source): {start_station}\n")
print(f"{'Destination':<16} | {'Shortest Distance (km)':<22} | {'Shortest Path':<40}")
print("-" * 80)

for i in range(len(nodes)):
    if i == start_index:
        continue  # Skip the start station

    distance = distances[i]
    
    if distance == inf:
        # Node is not reachable
        print(f"{nodes[i]:<16} | {'Not Reachable':<22} | -")
    else:
        # Reconstruct and print the path
        path_str = get_path(prev_nodes, nodes, start_index, i)
        print(f"{nodes[i]:<16} | {distance:<22.1f} | {path_str}")