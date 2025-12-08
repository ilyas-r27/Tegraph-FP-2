import sys
from collections import deque 

# Use float('inf') to represent infinity
inf = float('inf')

# 1. INPUT DATASET
nodes = [
    "SGU", "WO", "SDA", "BG", "LW", "ML", "MR", "KTS", "KD", "BL",  
    "CN", "PWT", "KRO", "KLG", "YGY", "SOL", "SRW", "MDN", "NGK", "SMG", 
    "PK", "TGL", "CKR", "PSE", "BDG", "KTG" 
]

# 26x26 Adjacency Matrix
graph = [
    [ 0.0,  5.8,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf, 300.6], # 0 SGU
    [ 5.8,  0.0, 17.6,  inf,  inf,  inf, 38.0,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf], # 1 WO
    [ inf, 17.6,  0.0, 21.5,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf], # 2 SDA
    [ inf,  inf, 21.5,  0.0, 40.5,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf], # 3 BG
    [ inf,  inf,  inf, 40.5,  0.0, 18.6,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf], # 4 LW
    [ inf,  inf,  inf,  inf, 18.6,  0.0,  inf,  inf,  inf, 58.2,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf], # 5 ML
    [ inf, 38.0,  inf,  inf,  inf,  inf,  0.0, 42.9,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf], # 6 MR
    [ inf,  inf,  inf,  inf,  inf,  inf, 42.9,  0.0, 25.2,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf, 30.1,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf], # 7 KTS
    [ inf,  inf,  inf,  inf,  inf,  inf,  inf, 25.2,  0.0, 54.8,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf], # 8 KD
    [ inf,  inf,  inf,  inf,  inf, 58.2,  inf,  inf, 54.8,  0.0,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf], # 9 BL
    [ inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  0.0, 100.8,  inf,  inf,  inf,  inf,  inf,  inf,  inf, 200.7,  inf,  inf,  inf, 220.5,  inf,  inf], # 10 CN
    [ inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf, 100.8,  0.0,  40.1,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf], # 11 PWT
    [ inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  40.1,  0.0,  60.5,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf], # 12 KRO
    [ inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  60.5,  0.0,  50.2,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf], # 13 KLG
    [ inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  50.2,  0.0,  60.4,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf, 480.3,  inf], # 14 YGY
    [ inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  60.4,  0.0,  45.3,  inf,  inf, 110.3,  inf,  inf,  inf,  inf,  inf,  inf], # 15 SOL
    [ inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  45.3,  0.0, 105.1,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf], # 16 SRW
    [ inf,  inf,  inf,  inf,  inf,  inf,  inf, 30.1,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf, 105.1,  0.0,  40.9,  inf,  inf,  inf,  inf,  inf,  inf,  inf], # 17 MDN
    [ inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  40.9,  0.0,  inf,  inf,  inf,  inf,  inf,  inf,  inf], # 18 NGK
    [ inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf, 200.7,  inf,  inf,  inf,  inf, 110.3,  inf,  inf,  inf,  0.0,  60.8,  inf,  inf,  inf,  inf,  inf], # 19 SMG
    [ inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  60.8,  0.0,  45.5,  inf,  inf,  inf,  inf], # 20 PK
    [ inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  45.5,  0.0,  inf,  inf,  inf,  inf], # 21 TGL
    [ inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  0.0,  60.3,  inf,  inf], # 22 CKR
    [ inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf, 220.5,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  60.3,  0.0, 143.2,  inf], # 23 PSE
    [ inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf, 480.3,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf, 143.2,  0.0,  inf], # 24 BDG
    [ 300.6, inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  0.0]  # 25 KTG
]

# --- ALGORITMA BFS (Breadth-First Search) ---
def bfs(graph, start_node_index):
    """
    Mencari jalur dengan JUMLAH STASIUN (Hops) paling sedikit.
    """
    num_nodes = len(graph)
    visited = [False] * num_nodes
    previous_nodes = [-1] * num_nodes
    
    # Queue: (node_index)
    queue = deque([start_node_index])
    visited[start_node_index] = True
    
    # Menyimpan jumlah transit/hops
    hops = [inf] * num_nodes
    hops[start_node_index] = 0
    
    while queue:
        u = queue.popleft()
        
        for v in range(num_nodes):
            # Cek jika ada jalur dan belum dikunjungi
            if graph[u][v] != inf and graph[u][v] != 0.0 and not visited[v]:
                visited[v] = True
                hops[v] = hops[u] + 1
                previous_nodes[v] = u
                queue.append(v)
                
    return hops, previous_nodes

def get_path_bfs(previous_nodes, node_names, start_index, end_index):
    path = []
    current_index = end_index
    while current_index != -1:
        path.append(node_names[current_index])
        current_index = previous_nodes[current_index]
    
    path.reverse()
    if len(path) > 0 and path[0] == node_names[start_index]:
        return " -> ".join(path)
    else:
        return "No path"


# --- EKSEKUSI PROGRAM ---
start_station = "SOL"  # Silakan ganti titik awal
start_index = nodes.index(start_station)

hops_bfs, prev_nodes_bfs = bfs(graph, start_index)

print(f"========= BFS ALGORITHM =========")
print(f"Start Station (Source): {start_station}")
print(f"{'Destination':<16} | {'Stops':<10} | {'Rute'}")
print("-" * 60)

for i in range(len(nodes)):
    if i == start_index: continue
    
    h = hops_bfs[i]
    if h != inf:
        path = get_path_bfs(prev_nodes_bfs, nodes, start_index, i)
        print(f"{nodes[i]:<16} | {h:<10} | {path}")
    else:
        print(f"{nodes[i]:<16} | {'-':<10} | Tidak Terjangkau")
