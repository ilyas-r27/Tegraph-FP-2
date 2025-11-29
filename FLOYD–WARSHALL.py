import math


#   STATION LIST (26 stations)


stations = [
    "SGU", "WO", "SDA", "BG", "LW", "ML", "MR", "KTS", "KD", "BL",
    "CN", "PWT", "KRO", "KLG", "YGY", "SOL", "SRW",
    "MDN", "NGK", "SMG", "PK", "TGL", "CKR", "PSE", "BDG", "KTG"
]

n = len(stations)
INF = float('inf')

# initialize dist + next node matrices
dist = [[INF] * n for _ in range(n)]
next_node = [[None] * n for _ in range(n)]

# distance to itself = 0
for i in range(n):
    dist[i][i] = 0
    next_node[i][i] = i


#   COMPLETE EDGE LIST


edges = [

    #   EAST JAVA

    ("SGU", "WO", 5.8),
    ("WO", "SDA", 17.6),
    ("SDA", "BG", 21.5),
    ("BG", "LW", 40.5),
    ("LW", "ML", 18.6),
    ("ML", "BL", 58.2),

    ("WO", "MR", 38),
    ("MR", "KTS", 42.9),
    ("KTS", "KD", 25.2),
    ("KD", "BL", 54.8),

    ("MDN", "KTS", 30.1),
    ("MDN", "NGK", 40.9),


    #   CENTRAL JAVA

    ("CN", "PWT", 100.8),
    ("CN", "SMG", 200.7),

    ("PWT", "KRO", 40.1),
    ("KRO", "KLG", 60.5),
    ("KLG", "YGY", 50.2),
    ("YGY", "SOL", 60.4),
    ("SOL", "SRW", 45.3),
    ("SRW", "MDN", 105.1),

    ("NGK", "SMG", 110.3),
    ("SMG", "PK", 60.8),
    ("PK", "TGL", 45.5),
    ("TGL", "CKR", 60.3),


    #   WEST JAVA

    ("CKR", "PSE", 143.2),
    ("PSE", "BDG", 480.3),


    #   LONG DISTANCE

    ("KTG", "SGU", 300.6)
]

#   INSERT EDGES INTO MATRIX

for a, b, w in edges:
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


#   TABLE OUTPUT (ALL DESTINATIONS)

def print_all_shortest_paths(start_station):

    start = stations.index(start_station)
    print(f"Start Station (Source): {start_station}\n")

    print(f"{'Destination':<12} | {'Shortest Distance (km)':<22} | Shortest Path")
    print("-" * 75)

    for end in range(n):
        if end == start:
            continue

        path_idx = get_path(start, end)
        if path_idx is None:
            distance = "∞"
            path_str = "No path"
        else:
            distance = round(dist[start][end], 1)
            path_str = " -> ".join(stations[i] for i in path_idx)

        print(f"{stations[end]:<12} | {distance:<22} | {path_str}")

#   RUN EXAMPLE (SGU as start)

print_all_shortest_paths("SOL")
