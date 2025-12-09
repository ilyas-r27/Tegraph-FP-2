import sys

# Use float('inf') to represent infinity
inf = float('inf')

# 1. INPUT DATASET
nodes = [
    "SGU", "WO", "SDA", "BG", "LW", "ML", "MR", "KTS", "KD", "BL",  
    "CN", "PWT", "KRO", "KLG", "YGY", "SOL", "SRW", "MDN", "NGK", "SMG", 
    "PK", "TGL", "CKR", "PSE", "BDG", "KTG" 
]

# 26x26 Adjacency Matrix (Edges & Weights)
# Distances are in kilometers (km) and the graph is UNDIRECTED (A->B = B->A).
graph = [
#      SGU  WO    SDA   BG    LW    ML    MR    KTS   KD    BL    CN    PWT   KRO   KLG   YGY   SOL   SRW   MDN   NGK   SMG   PK    TGL   CKR   PSE   BDG   KTG
    [ 0.0,  5.8,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf, 300.6], # 0 SGU
    [ 5.8,  0.0, 17.6,  inf,  inf,  inf, 38.0,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf], # 1 WO
    [ inf, 17.6,  0.0, 21.5,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf], # 2 SDA
    [ inf,  inf, 21.5,  0.0, 40.5,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf], # 3 BG
    [ inf,  inf,  inf, 40.5,  0.0, 18.6,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf], # 4 LW
    [ inf,  inf,  inf,  inf, 18.6,  0.0,  inf,  inf,  inf, 58.2,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf], # 5 ML
    [ inf, 38.0,  inf,  inf,  inf,  inf,  0.0, 42.9,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf], # 6 MR
    [ inf,  inf,  inf,  inf,  inf,  inf, 42.9,  0.0, 25.2,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf, 30.1,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf], # 7 KTS (Key link to Central Java via MDN)
    [ inf,  inf,  inf,  inf,  inf,  inf,  inf, 25.2,  0.0, 54.8,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf], # 8 KD
    [ inf,  inf,  inf,  inf,  inf, 58.2,  inf,  inf, 54.8,  0.0,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf], # 9 BL
    [ inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  0.0, 100.8,  inf,  inf,  inf,  inf,  inf,  inf,  inf, 200.7,  inf,  inf,  inf, 220.5,  inf,  inf], # 10 CN (Cirebon)
    [ inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf, 100.8,  0.0,  40.1,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf], # 11 PWT (Purwokerto)
    [ inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  40.1,  0.0,  60.5,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf], # 12 KRO (Kroya)
    [ inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  60.5,  0.0,  50.2,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf], # 13 KLG (Kutoarjo)
    [ inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  50.2,  0.0,  60.4,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf, 480.3,  inf], # 14 YGY (Yogyakarta)
    [ inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  60.4,  0.0,  45.3,  inf,  inf, 110.3,  inf,  inf,  inf,  inf,  inf,  inf], # 15 SOL (Solo)
    [ inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  45.3,  0.0, 105.1,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf], # 16 SRW (Sragen)
    [ inf,  inf,  inf,  inf,  inf,  inf,  inf, 30.1,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf, 105.1,  0.0,  40.9,  inf,  inf,  inf,  inf,  inf,  inf,  inf], # 17 MDN (Madiun)
    [ inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  40.9,  0.0,  inf,  inf,  inf,  inf,  inf,  inf,  inf], # 18 NGK (Nganjuk)
    [ inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf, 200.7,  inf,  inf,  inf,  inf, 110.3,  inf,  inf,  inf,  0.0,  60.8,  inf,  inf,  inf,  inf,  inf], # 19 SMG (Semarang)
    [ inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  60.8,  0.0,  45.5,  inf,  inf,  inf,  inf], # 20 PK (Pekalongan)
    [ inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  45.5,  0.0,  inf,  inf,  inf,  inf], # 21 TGL (Tegal)
    [ inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  0.0,  60.3,  inf,  inf], # 22 CKR (Cikarang)
    [ inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf, 220.5,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  60.3,  0.0, 143.2,  inf], # 23 PSE (Jakarta)
    [ inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf, 480.3,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf, 143.2,  0.0,  inf], # 24 BDG (Bandung)
    [ 300.6, inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  0.0]  # 25 KTG
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
start_station = "SOL"
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
