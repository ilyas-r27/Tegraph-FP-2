# GROUP 2


| Name           | NRP        | Kelas     |
| ---            | ---        | ----------|
| Kenzie Maheswara | 5025241001 | IUP |
| Palpal Yalmialam | 5025241002 | IUP |
| Muhammad Ilyas Rusdi | 5025241007 | IUP |
| M. Arifathan Mahardika | 5025241013 | IUP |



### Adjacency Matrix (Track Distances)

```python
inf = float('inf')

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

```

# Shortest Path Algorithms on the Java Railway Station Dataset

This document explains three Python programs that use **Dijkstra**, **Floyd–Warshall**, and **BFS** on the same railway network dataset (26 stations in East, Central, and West Java).  
All three programs use the **same set of stations** and almost the same connections, but they answer *slightly different questions*.

---

## 1. Dataset Overview

### 1.1 Station List (`nodes` / `stations`)

Both Dijkstra, BFS, and Floyd–Warshall use the same 26 stations:

```python
nodes = [
    "SGU", "WO", "SDA", "BG", "LW", "ML", "MR", "KTS", "KD", "BL",  
    "CN", "PWT", "KRO", "KLG", "YGY", "SOL", "SRW", "MDN", "NGK", "SMG", 
    "PK", "TGL", "CKR", "PSE", "BDG", "KTG" 
]
```

Each string is a **station code**, for example:

- **SGU** – Stasiun Surabaya Gubeng  
- **WO** – Stasiun Wonokromo  
- **SDA** – Stasiun Sidoarjo  
- **BG** – Stasiun Bangil  
- **LW** – Stasiun Lawang  
- **ML** – Stasiun Malang  
- **MR** – Stasiun Mojokerto  
- **KTS** – Stasiun Kertosono  
- **KD** – Stasiun Kediri  
- **BL** – Stasiun Blitar  
- **CN** – Stasiun Cirebon  
- **PWT** – Stasiun Purwokerto  
- **KRO** – Stasiun Kroya  
- **KLG** – Stasiun Kutoarjo  
- **YGY** – Stasiun Yogyakarta  
- **SOL** – Stasiun Solo (Surakarta)  
- **SRW** – Stasiun Sragen  
- **MDN** – Stasiun Madiun  
- **NGK** – Stasiun Nganjuk  
- **SMG** – Stasiun Semarang  
- **PK** – Stasiun Pekalongan  
- **TGL** – Stasiun Tegal  
- **CKR** – Stasiun Cikarang  
- **PSE** – Stasiun Pasar Senen (Jakarta)  
- **BDG** – Stasiun Bandung
- **KTG** – Stasiun Ketapang (Banyuwangi)
  

### 1.2 Adjacency Matrix (`graph`)

In Dijkstra and BFS, the network is stored as a **26 × 26 adjacency matrix**:

```python
graph = [
    #      SGU  WO    SDA   BG    LW    ML    MR    KTS   KD    BL   ...
    [ 0.0,  5.8,  inf,  inf,  inf,  inf,  inf,  inf,  inf,  inf, ...],  # SGU
    [ 5.8,  0.0, 17.6,  inf,  inf,  inf, 38.0,  inf,  inf,  inf, ...],  # WO
    ...
]
```

- `graph[i][j]` = distance (in km) from station `nodes[i]` to `nodes[j]`.
- `0.0` on the diagonal means **distance from a station to itself**.
- `inf` (infinity) means **no direct railway track** between those two stations.
- The matrix is **symmetric** (undirected graph):  
  if there is a track from `A` to `B`, then `graph[A][B] == graph[B][A]`.

Example:

- `graph[SGU][WO] = 5.8` and `graph[WO][SGU] = 5.8`  
  → There is a 5.8 km railway segment between Surabaya Gubeng (SGU) and Wonokromo (WO).

### 1.3 Edge List (`edges`) in Floyd–Warshall

The Floyd–Warshall version uses an **edge list** instead of a full matrix:

```python
edges = [
    ("SGU", "WO", 5.8),
    ("WO", "SDA", 17.6),
    ("SDA", "BG", 21.5),
    ...
    ("KTG", "SGU", 300.6)
]
```

Each triple `(a, b, w)` means:

- There is an **undirected railway track** between station `a` and `b`.
- The length of that segment is `w` km.

These edges are then inserted into the `dist` matrix:

```python
dist[i][j] = w
dist[j][i] = w
```

---

## 2. Dijkstra’s Algorithm Code

The Dijkstra code answers:

> **“What is the shortest total distance (in km) from a given start station (here: Solo/SOL) to every other station?”**

### 2.1 Function `dijkstra(graph, start_node_index)`

```python
def dijkstra(graph, start_node_index):
    """Implementation of Dijkstra's Algorithm using an Adjacency Matrix."""
    num_nodes = len(graph)

    distances = [inf] * num_nodes
    visited = [False] * num_nodes
    previous_nodes = [-1] * num_nodes

    distances[start_node_index] = 0
```

- `num_nodes` = number of stations (26).
- `distances[i]` = current **best-known distance** from the start station to station `i`.
- `visited[i]` = whether station `i` has already been “finalized”.
- `previous_nodes[i]` = parent of node `i` in the shortest path tree  
  (used later to reconstruct the path).
- Distance from the start station to itself is `0`.

#### Main Loop: Selecting the closest unvisited station

```python
    for _ in range(num_nodes):
        min_dist = inf
        u = -1

        for i in range(num_nodes):
            if not visited[i] and distances[i] < min_dist:
                min_dist = distances[i]
                u = i

        if u == -1:
            break

        visited[u] = True
```

- For each iteration, the algorithm picks the **unvisited station** with the **smallest distance**.
- `u` becomes the index of that station.
- If all reachable stations have been visited, `u` stays `-1` and the loop ends.

#### Relaxation: Updating distances of neighbors

```python
        for v in range(num_nodes):
            if graph[u][v] > 0 and not visited[v]:
                new_dist = distances[u] + graph[u][v]
                if new_dist < distances[v]:
                    distances[v] = new_dist
                    previous_nodes[v] = u
```

For every station `v`:

- Check if there is a direct track from `u` to `v`:  
  `graph[u][v] > 0` (ignores `inf` and the `0` diagonal).
- Compute the **candidate distance** via `u`:  
  `new_dist = distance(start → u) + distance(u → v)`.
- If this `new_dist` is shorter than the current `distances[v]`,  
  update `distances[v]` and record `previous_nodes[v] = u`.

At the end, the function returns:

```python
    return distances, previous_nodes
```

- `distances[i]` = shortest distance from start (SOL) to station `nodes[i]`.
- `previous_nodes` = used to reconstruct the actual route.

### 2.2 Function `get_path(previous_nodes, node_names, start_index, end_index)`

This helper reconstructs the **route** from the start station to a chosen destination.

```python
def get_path(previous_nodes, node_names, start_index, end_index):
    path = []
    current_index = end_index

    while current_index != -1:
        path.append(node_names[current_index])
        current_index = previous_nodes[current_index]

    path.reverse()

    if path[0] == node_names[start_index]:
        return " -> ".join(path)
    else:
        return "No path"
```

How it works:

1. Start from `end_index` (e.g., `SMG`).
2. Move backwards using `previous_nodes` until `-1` (no parent).
3. Collect the station names along the way.
4. Reverse the path so it goes from **start → … → end**.
5. If the first station is not the start, there was no valid path.

Example result:

- From `SOL` to `SMG`, you might get:  
  `SOL -> SRW -> MDN -> NGK -> SMG` (depending on edge weights).

### 2.3 Main Program (Using `SOL` as Start)

```python
start_station = "SOL"
start_index = nodes.index(start_station)

distances, prev_nodes = dijkstra(graph, start_index)

print(f"========= DIJKSTRA'S ALGORITHM RESULTS =========\n")
print(f"Start Station (Source): {start_station}\n")
print(f"{'Destination':<16} | {'Shortest Distance (km)':<22} | {'Shortest Path':<40}")
print("-" * 80)
```

For each station:

```python
for i in range(len(nodes)):
    if i == start_index:
        continue

    distance = distances[i]

    if distance == inf:
        print(f"{nodes[i]:<16} | {'Not Reachable':<22} | -")
    else:
        path_str = get_path(prev_nodes, nodes, start_index, i)
        print(f"{nodes[i]:<16} | {distance:<22.1f} | {path_str}")
```

- If `distance == inf`, there is **no route** from Solo to that station.
- Otherwise, the program prints:
  - Destination station code
  - Shortest distance from `SOL` (in km)
  - Full route (sequence of station codes)

---

## 3. Floyd–Warshall Algorithm Code

The Floyd–Warshall code answers:

> **“What is the shortest total distance between *every* pair of stations, and what is the path?”**

Instead of running from one start station at a time, it precomputes **all-pairs shortest paths**.

### 3.1 Initialization of `dist` and `next_node`

```python
n = len(stations)
INF = float('inf')

dist = [[INF] * n for _ in range(n)]
next_node = [[None] * n for _ in range(n)]

for i in range(n):
    dist[i][i] = 0
    next_node[i][i] = i
```

- `dist[i][j]` = current best-known distance from station `i` to `j`.
- `next_node[i][j]` = the **next station** to go to if we start from `i` towards `j`.
- Initially:
  - Distance to itself = `0`.
  - All other pairs = `INF` (unknown).

### 3.2 Inserting Edges

```python
for a, b, w in edges:
    i = stations.index(a)
    j = stations.index(b)
    dist[i][j] = w
    dist[j][i] = w
    next_node[i][j] = j
    next_node[j][i] = i
```

- For every physical track (e.g., `("YGY", "SOL", 60.4)`):
  - Set the direct distance in both directions.
  - Set `next_node[i][j]` = `j`, meaning:  
    to go from `i` to `j`, the *next* node is directly `j`.

### 3.3 Core Floyd–Warshall Triple Loop

```python
for k in range(n):
    for i in range(n):
        for j in range(n):
            if dist[i][k] + dist[k][j] < dist[i][j]:
                dist[i][j] = dist[i][k] + dist[k][j]
                next_node[i][j] = next_node[i][k]
```

Logic:

- For every possible **intermediate station `k`**:
  - Check if going from `i` → `k` → `j` is shorter than current `i` → `j`.
- If shorter, update:
  - `dist[i][j]` to the new shorter distance.
  - `next_node[i][j]` to the **first step** on the route from `i` to `j`, which is the same as the first step from `i` to `k`.

After this loop:

- `dist[i][j]` contains the shortest distance (like Dijkstra, but for all pairs).
- `next_node[i][j]` allows us to reconstruct the route.

### 3.4 Path Reconstruction: `get_path(start, end)`

```python
def get_path(start, end):
    if next_node[start][end] is None:
        return None
    path = [start]
    while start != end:
        start = next_node[start][end]
        path.append(start)
    return path
```

- If there is no path (`next_node[start][end]` is `None`), return `None`.
- Otherwise, repeatedly move `start` to `next_node[start][end]` until you reach `end`.
- `path` contains the **indices** of stations on the route.

To print station names:

```python
" -> ".join(stations[i] for i in path_idx)
```

### 3.5 Printing All Shortest Paths from `SOL`

```python
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
```

Finally, it runs:

```python
print_all_shortest_paths("SOL")
```

Same idea as the Dijkstra output table, but **distances come from the all-pairs computation**.

---

## 4. BFS Algorithm Code

The BFS code answers a different question:

> **“From Solo (SOL), what route uses the *fewest number of stations* (fewest hops), ignoring distance?”**

So:

- Dijkstra & Floyd–Warshall → minimize **total kilometers**.
- BFS → minimize **number of edges/stations passed**.

### 4.1 BFS Function

```python
def bfs(graph, start_node_index):
    """Mencari jalur dengan JUMLAH STASIUN (Hops) paling sedikit."""
    num_nodes = len(graph)
    visited = [False] * num_nodes
    previous_nodes = [-1] * num_nodes

    queue = deque([start_node_index])
    visited[start_node_index] = True

    hops = [inf] * num_nodes
    hops[start_node_index] = 0
```

- `visited[i]` to avoid revisiting stations.
- `previous_nodes[i]` = parent station to reconstruct the path.
- `hops[i]` = minimum number of **edges** (segments) from start to station `i`.
- Use a queue (`deque`) for the BFS wave.

#### BFS Loop

```python
    while queue:
        u = queue.popleft()

        for v in range(num_nodes):
            if graph[u][v] != inf and graph[u][v] != 0.0 and not visited[v]:
                visited[v] = True
                hops[v] = hops[u] + 1
                previous_nodes[v] = u
                queue.append(v)

    return hops, previous_nodes
```

For each station `u` taken from the queue:

- Look at all possible neighbors `v`.
- A neighbor exists if:
  - `graph[u][v] != inf` (there is a track), and
  - `graph[u][v] != 0.0` (ignore the self-loop).
- If `v` has not been visited:
  - Set `hops[v] = hops[u] + 1`.
  - Set `previous_nodes[v] = u`.
  - Push `v` to the queue.

This guarantees:

- The first time we reach station `v`, we have used the **fewest possible segments** from the start.

### 4.2 Path Reconstruction for BFS

```python
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
```

Same idea as Dijkstra’s `get_path`, but using the BFS `previous_nodes` and focusing on hops rather than distance.

### 4.3 Main Program for BFS (Start from `SOL`)

```python
start_station = "SOL"
start_index = nodes.index(start_station)

hops_bfs, prev_nodes_bfs = bfs(graph, start_index)

print(f"========= BFS ALGORITHM =========")
print(f"Start Station (Source): {start_station}")
print(f"{'Destination':<16} | {'Stops':<10} | {'Rute'}")
print("-" * 60)
```

For each station:

```python
for i in range(len(nodes)):
    if i == start_index: continue

    h = hops_bfs[i]
    if h != inf:
        path = get_path_bfs(prev_nodes_bfs, nodes, start_index, i)
        print(f"{nodes[i]:<16} | {h:<10} | {path}")
    else:
        print(f"{nodes[i]:<16} | {'-':<10} | Tidak Terjangkau")
```

- `Stops` = number of edges/hops from Solo to that station.
- `Rute` = sequence of station codes with **minimum number of stations**.

---

## 5. Effectiveness Comparison of the Three Algorithms

All three algorithms (Dijkstra, Floyd–Warshall, and BFS) run on the same 26-station Java railway network, but they optimize **different objectives** and are suitable for **different use cases**.

### 5.1 Dijkstra (Single-Source, Weighted Shortest Paths)

In our implementation, Dijkstra starts from **SOL (Solo)** and computes the shortest total distance (in kilometers) from Solo to **all other stations** using the edge weights from the adjacency matrix.

- Strengths:
  - Very suitable for **single-source** shortest path queries (e.g., “from Solo to every station”).
  - Uses actual **distance (km)** as cost, so the result makes sense for real railway planning.
  - More efficient than Floyd–Warshall when we only care about routes from **one** starting station.
- Limitations:
  - If we frequently change the start station (e.g., sometimes from SOL, sometimes from SGU, sometimes from SMG), we must rerun Dijkstra for each new source.

For this project, Dijkstra directly answers:  
> “What is the shortest-distance route from **Solo** to each station in the network?”

---

### 5.2 Floyd–Warshall (All-Pairs, Weighted Shortest Paths)

Floyd–Warshall uses the same station set but builds an **all-pairs** shortest path table. After the triple loop, we know the shortest distance between **every pair** of stations (SGU–BDG, YGY–PSE, SOL–KTG, etc.), not only from Solo.

- Strengths:
  - After one preprocessing step, we can query the shortest path between **any two stations** instantly.
  - Very useful if we need a **general routing engine** (for example, a system where the user can choose any origin and destination).
- Limitations:
  - Time complexity is \(O(n^3)\), which is heavier than Dijkstra for a single source.
  - For our dataset with only **26 stations**, this is still perfectly feasible, but it is more work than needed if we only care about routes from Solo.

In this project, Floyd–Warshall is more like a **“full network analysis tool”**: powerful, but a bit overkill if the task is only “Solo → all stations”.

---

### 5.3 BFS (Unweighted, Minimum Number of Stops)

The BFS implementation also starts from **SOL**, but it ignores actual distances in kilometers. Instead, it treats every track as if it had equal cost and finds the route with the **fewest number of edges (hops)**.

- Strengths:
  - Finds the route with the **minimum number of stations/segments**.
  - Useful when each transfer has the same “cost” (for example, when we only care about how many times the passenger changes trains or how many intermediate stops there are).
- Limitations:
  - Completely ignores real distances (5.8 km vs 300.6 km is treated the same).
  - In a railway context, the BFS route may have **shorter hops count but longer total distance** than the Dijkstra/Floyd–Warshall route.

So BFS is best when the goal is:  
> “Use as **few stations** as possible,”  
not “use the **shortest distance** in km.”

---

## 6. Conclusion: Which Algorithm Is the Most Effective Here?

Given the goal of this project:

> Find and analyze routes from **Solo (SOL)** to all other stations on the Java railway network, using **real distances (km)**,

the most effective algorithm is:

### Dijkstra’s Algorithm 

**Reasons:**

1. The problem is a **single-source shortest path** problem (Solo → all stations), which is exactly what Dijkstra is designed for.
2. It uses the real **distance values from the dataset**, so the results are realistic for travel planning or distance comparison.
3. It is **more efficient** than Floyd–Warshall for this specific need, because we do not require shortest paths between *every* pair of stations.
4. It produces both:
   - The **shortest distance (km)**, and  
   - The **exact route (sequence of station codes)** from Solo to each destination.
5. The BFS result is useful as a comparison (fewest stops), but it does **not** reflect the true railway distance, so it is less appropriate if distance is the main optimization target.

In summary:

- Use **Dijkstra (from SOL)** as the main algorithm for this project.  
- Use **Floyd–Warshall** when we want a more general tool that can answer “shortest path between any two stations” without rerunning the algorithm.  
- Use **BFS** if we want to study or compare routes based on the **minimum number of station hops**, ignoring distance.
