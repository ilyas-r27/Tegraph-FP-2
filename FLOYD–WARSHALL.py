import math


#   STATION LIST (26 stations)

stations = [
    "SGU", "WO", "SDA", "BG", "LW", "ML", "MR", "KTS", "KD", "BL",
    "CN", "PWT", "KRO", "KLG", "YGY", "SOL", "SRW",
    "MDN", "NGK", "SMG", "PK", "TGL", "CKR", "PSE", "BDG", "KTG"
]

n = len(stations)
INF = float('inf')

# initialize distance matrix
dist = [[INF] * n for _ in range(n)]
next_node = [[None] * n for _ in range(n)]

# distance to itself = 0
for i in range(n):
    dist[i][i] = 0
    next_node[i][i] = i


#   ADD EDGES BASED ON DATASET
edges = [
    # East Java segment (your previous data)
    ("SGU", "WO", 5.8),
    ("WO", "SDA", 17.6),
    ("SDA", "BG", 21.5),
    ("BG",  "LW", 40.5),
    ("LW",  "ML", 18.6),
    ("WO",  "MR", 38),
    ("MR",  "KTS", 42.9),
    ("KTS", "KD", 25.2),
    ("KD",  "BL", 54.8),
    ("BL",  "ML", 58.2),

    # Central + West Java region (from your large matrix)
    ("CN", "PWT", 100.8),
    ("PWT", "KRO", 40.1),
    ("KRO", "KLG", 60.5),
    ("KLG", "YGY", 50.2),
    ("YGY", "SOL", 60.4),
    ("SOL", "SRW", 45.3),
    ("SRW", "MDN", 105.1),
    ("MDN", "NGK", 40.9),
    ("NGK", "SMG", 110.3),
    ("SMG", "PK", 60.8),
    ("PK", "TGL", 45.5),
    ("TGL", "CKR", 60.3),
    ("CKR", "PSE", 143.2),
    ("PSE", "BDG", 480.3),

    # Long-distance connection
    ("KTG", "SGU", 300.6)
]

# fill adjacency matrix
for (a, b, w) in edges:
    i = stations.index(a)
    j = stations.index(b)
    dist[i][j] = w
    dist[j][i] = w
    next_node[i][j] = j
    next_node[j][i] = i


#   FLOYD–WARSHALL ALGORITHM

for k in range(n):
    for i in range(n):
        for j in range(n):
            if dist[i][k] + dist[k][j] < dist[i][j]:
                dist[i][j] = dist[i][k] + dist[k][j]
                next_node[i][j] = next_node[i][k]


#   PATH RECONSTRUCTION

def get_path(start, end):
    if next_node[start][end] is None:
        return None
    path = [start]
    while start != end:
        start = next_node[start][end]
        path.append(start)
    return path


#   TEST: SGU → BDG (example)


start = stations.index("SGU")
end = stations.index("BDG")

path_idx = get_path(start, end)
path_names = [stations[i] for i in path_idx]

print("Shortest path SGU -> BDG:")
print(" -> ".join(path_names))
print("Distance:", dist[start][end])
