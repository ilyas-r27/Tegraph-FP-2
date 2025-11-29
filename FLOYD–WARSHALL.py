import math

#   NODE DEFINITIONS


stations = [
    "Gubeng",      # 0
    "Wonokromo",   # 1
    "Sidoarjo",    # 2
    "Bangil",      # 3
    "Lawang",      # 4
    "Malang",      # 5
    "Mojokerto",   # 6
    "Kertosono",   # 7
    "Kediri",      # 8
    "Blitar"       # 9
]

n = len(stations)

INF = float('inf')


#   INITIAL DISTANCE MATRIX

# Create NxN matrix initialized to INF
dist = [[INF] * n for _ in range(n)]
next_node = [[None] * n for _ in range(n)]  # for path reconstruction

# Distance to itself = 0
for i in range(n):
    dist[i][i] = 0
    next_node[i][i] = i


#   ADD EDGES (from your diagram)

edges = [
    (0, 1, 5.9),    # Gubeng - Wonokromo
    (1, 2, 17.6),   # Wonokromo - Sidoarjo
    (2, 3, 21.5),   # Sidoarjo - Bangil
    (3, 4, 40.5),   # Bangil - Lawang
    (4, 5, 18.6),   # Lawang - Malang
    
    (1, 6, 38),     # Wonokromo - Mojokerto
    (6, 7, 42.9),   # Mojokerto - Kertosono
    (7, 8, 25.2),   # Kertosono - Kediri
    (8, 9, 54.8),   # Kediri - Blitar
    (9, 5, 59.2),   # Blitar - Malang
]

# Since all connections are bidirectional, fill both ways
for (u, v, w) in edges:
    dist[u][v] = w
    dist[v][u] = w
    next_node[u][v] = v
    next_node[v][u] = u


#   FLOYD–WARSHALL ALGORITHM


for k in range(n):
    for i in range(n):
        for j in range(n):
            if dist[i][k] + dist[k][j] < dist[i][j]:
                dist[i][j] = dist[i][k] + dist[k][j]
                next_node[i][j] = next_node[i][k]   # update next hop



#   PATH RECONSTRUCTION


def get_path(start, end):
    if next_node[start][end] is None:
        return None
    
    path = [start]
    while start != end:
        start = next_node[start][end]
        path.append(start)
    return path


#   TEST


start = 0  # Gubeng
end = 5    # Malang

path_indices = get_path(start, end)
path_names = [stations[i] for i in path_indices]

print("Shortest path using Floyd–Warshall:")
print(" -> ".join(path_names))
print("Total distance:", dist[start][end])
