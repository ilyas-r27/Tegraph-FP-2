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

# Explanation – BFS, Dijkstra, and Floyd–Warshall  
*(Based on the Java Station Dataset, starting from Solo – `SOL`)*

---

## 1. Shared Data Model (Station Dataset)

### 1.1 Station List

<img width="613" height="288" alt="image" src="https://github.com/user-attachments/assets/e3aaedca-396a-4afd-a89d-8897e3e7606c" />


```python
nodes = [
    "SGU", "WO", "SDA", "BG", "LW", "ML", "MR", "KTS", "KD", "BL",
    "CN", "PWT", "KRO", "KLG", "YGY", "SOL", "SRW", "MDN", "NGK", "SMG",
    "PK", "TGL", "CKR", "PSE", "BDG", "KTG"
]
```

---

### 1.2 Adjacency Matrix (BFS & Dijkstra)

In **BFS.py** and **DIJKSTRA.py**:

```python
inf = float('inf')

# 26 x 26 adjacency matrix
graph = [
    # row 0 = SGU, row 1 = WO, ..., row 15 = SOL, etc.
    [0.0, 5.8, inf, ... ],
    [5.8, 0.0, 17.6, ... ],
    ...
]
```

- `graph[i][j]` = **distance in km** between `nodes[i]` and `nodes[j]`.
- `0.0` on the diagonal = distance from a station to itself.
- `inf` means **there is no direct railway connection** between those two stations.
- The matrix is **symmetric** (undirected graph):  
  if `graph[i][j] = 40.5`, then `graph[j][i]` is also `40.5`.

For **BFS**, these weights are ignored (only “is there a connection or not?” matters).  
For **Dijkstra**, these weights are the **edge costs**.

---

### 1.3 Edge List (Floyd–Warshall)

In **FLOYD–WARSHALL.py**, the same network is defined as an **edge list**:

```python
INF = float('inf')
dist      = [[INF] * n for _ in range(n)]
next_node = [[None] * n for _ in range(n)]

for i in range(n):
    dist[i][i] = 0
    next_node[i][i] = i

edges = [

    # EAST JAVA
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

    ("SRW", "MDN", 105.1),
    ("MDN", "NGK", 40.9),

    # CENTRAL JAVA
    ("CN", "PWT", 100.8),
    ("CN", "SMG", 200.7),
    ("PWT", "KRO", 40.1),
    ("KRO", "KLG", 60.5),
    ("KLG", "YGY", 50.2),
    ("YGY", "SOL", 60.4),
    ("SOL", "SRW", 45.3),
    ("NGK", "SMG", 110.3),
    ("SMG", "PK", 60.8),
    ("PK", "TGL", 45.5),

    # WEST JAVA
    ("CN", "KTG", 220.5),
    ("KTG", "CKR", 168.0),
    ("CKR", "PSE", 26.8),
    ("PSE", "BDG", 137.1),
    ("BDG", "KTG", 205.6)
]
```

Then each edge is inserted into the matrices:

```python
for a, b, w in edges:
    i = stations.index(a)
    j = stations.index(b)
    dist[i][j] = w
    dist[j][i] = w            # undirected
    next_node[i][j] = j
    next_node[j][i] = i
```

So `dist` starts as the **direct distances**, and Floyd–Warshall will turn it into **shortest distances between every pair of stations**.

---

## 2. BFS.py – Breadth-First Search (Minimum Hops)

### 2.1 Purpose

- BFS here is used to find the path from **Solo (`SOL`) to all other stations** that has the **minimum number of stops / edges (hops)**.
- It **ignores the kilometers** and only cares about connectivity.

---

### 2.2 `bfs(graph, start_node_index)`

```python
from collections import deque

def bfs(graph, start_node_index):
    """
    Mencari jalur dengan JUMLAH STASIUN (Hops) paling sedikit.
    """
    num_nodes = len(graph)
    visited = [False] * num_nodes
    previous_nodes = [-1] * num_nodes

    queue = deque([start_node_index])
    visited[start_node_index] = True

    hops = [inf] * num_nodes
    hops[start_node_index] = 0

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

Step-by-step:

- `visited[i]`: whether station `i` has already been discovered.
- `previous_nodes[i]`: the **parent station** on the BFS tree (used to reconstruct the route).
- `queue`: BFS frontier, starting from the index of `"SOL"`.
- `hops[i]`: the **minimum number of edges** from `SOL` to station `i`.

Inside the loop:

- Take station `u` from the queue.
- Scan all stations `v`:
  - If `graph[u][v]` is not `inf` and not `0.0`, there is a **direct track** from `u` to `v`.
  - If `v` has not been visited:
    - Mark `v` as visited.
    - Set `hops[v] = hops[u] + 1` (one more hop than `u`).
    - Set `previous_nodes[v] = u` (we reached `v` from `u`).
    - Push `v` into the queue.

The result:

- `hops`: minimal number of transfers from Solo to every station.
- `previous_nodes`: information to reconstruct each path.

---

### 2.3 `get_path_bfs(previous_nodes, node_names, start_index, end_index)`

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

- Start from the destination index (`end_index`).
- Follow `previous_nodes` backwards until `-1` (no parent).
- Reverse the list to get `start → ... → end`.
- Returns a string like: `"SOL -> SRW -> MDN -> NGK"`.

---

### 2.4 Main Program

```python
start_station = "SOL"
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
```

- Sets **Solo** as the source.
- Runs BFS once.
- Prints, for every destination:
  - Station code.
  - Number of **stops/hops** from Solo.
  - Path (sequence of station codes).

BFS is basically answering:  
> “From Solo, what is the route with the **fewest station transitions**, no matter how far it is in km?”

---

## 3. DIJKSTRA.py – Dijkstra’s Algorithm (Shortest Distance from Solo)

### 3.1 Purpose

- This implementation finds the **shortest total distance (in km)** from **Solo (`SOL`)** to **all other stations** using the same adjacency matrix `graph`.
- Now the numeric values in `graph[i][j]` are crucial as edge weights.

---

### 3.2 `dijkstra(graph, start_node_index)`

```python
def dijkstra(graph, start_node_index):
    """
    Implementation of Dijkstra's Algorithm using an Adjacency Matrix.
    """
    num_nodes = len(graph)

    distances = [inf] * num_nodes
    visited = [False] * num_nodes
    previous_nodes = [-1] * num_nodes

    distances[start_node_index] = 0

    for _ in range(num_nodes):
        # 1. Pick the unvisited node with smallest current distance
        min_dist = inf
        u = -1
        for i in range(num_nodes):
            if not visited[i] and distances[i] < min_dist:
                min_dist = distances[i]
                u = i

        if u == -1:
            break   # no more reachable nodes

        # 2. Mark node u as visited
        visited[u] = True

        # 3. Relax edges from u
        for v in range(num_nodes):
            # if there is a connection and v not visited
            if graph[u][v] > 0 and not visited[v]:
                new_dist = distances[u] + graph[u][v]
                if new_dist < distances[v]:
                    distances[v] = new_dist
                    previous_nodes[v] = u

    return distances, previous_nodes
```

Key ideas:

- `distances[i]`: current best known **distance in km** from Solo to station `i`.
- `visited[i]`: whether the shortest path to `i` is already finalized.
- In each iteration:
  1. Choose unvisited node `u` with minimal `distances[u]`.
  2. Mark it visited.
  3. For each neighbor `v`, try to improve `distances[v]` using the edge `u → v`:
     - `new_dist = distances[u] + graph[u][v]`.
     - If `new_dist` is smaller, update `distances[v]` and set `previous_nodes[v] = u`.

This is the classic **single-source shortest path** algorithm for non-negative weights.

---

### 3.3 `get_path(previous_nodes, node_names, start_index, end_index)`

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

Exactly the same idea as in BFS, but now the `previous_nodes` came from **Dijkstra’s relaxation**.

---

### 3.4 Main Program

```python
start_station = "SOL"
start_index = nodes.index(start_station)

distances, prev_nodes = dijkstra(graph, start_index)

print(f"========= DIJKSTRA'S ALGORITHM RESULTS =========
")
print(f"Start Station (Source): {start_station}
")
print(f"{'Destination':<16} | {'Shortest Distance (km)':<22} | {'Shortest Path':<40}")
print("-" * 80)

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

Now the output table shows, for each station:

- The **shortest distance in km** from Solo.
- The **shortest path** in terms of that distance.

So Dijkstra is answering:  
> “From Solo, what is the **shortest-distance route** to every other station?”

---

## 4. FLOYD–WARSHALL.py – Floyd–Warshall (All-Pairs Shortest Paths)

### 4.1 Purpose

- Instead of just Solo → all, Floyd–Warshall computes the **shortest paths between every pair of stations**.
- The code then prints one “row” of this result: **all shortest paths starting from Solo (`SOL`)**.

---

### 4.2 Initialization of `dist` and `next_node`

```python
n = len(stations)
INF = float('inf')

dist      = [[INF] * n for _ in range(n)]
next_node = [[None] * n for _ in range(n)]

for i in range(n):
    dist[i][i] = 0
    next_node[i][i] = i
```

- `dist[i][j]`: current best known **shortest distance** between `stations[i]` and `stations[j]`.
- `next_node[i][j]`: the **next node to go to** from `i` on the shortest path to `j`.

After this, the code inserts all **direct edges** (see section 1.3).

---

### 4.3 Floyd–Warshall Core Algorithm

```python
for k in range(n):
    for i in range(n):
        for j in range(n):
            if dist[i][k] + dist[k][j] < dist[i][j]:
                dist[i][j] = dist[i][k] + dist[k][j]
                next_node[i][j] = next_node[i][k]
```

Interpretation:

- Try every station `k` as a possible **intermediate hub** between `i` and `j`.
- If route `i → k → j` is shorter than the current `i → j`, update:
  - `dist[i][j]` to this new smaller value.
  - `next_node[i][j]` to the first step on the path to `k`.

After this triple loop:

- `dist` holds **shortest distances between every pair of stations**.
- `next_node` allows reconstructing **any shortest path**.

---

### 4.4 Path Reconstruction – `get_path(start, end)`

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

- Input: `start`, `end` are **indices** in the `stations` list.
- If `next_node[start][end]` is `None`, there is **no path**.
- Otherwise, repeatedly jump from `start` to `next_node[start][end]` until `end` is reached.
- Returns a list like `[15, 16, 17, 18]` which corresponds to e.g. `["SOL", "SRW", "MDN", "NGK"]`.

---

### 4.5 Printing All Shortest Paths from Solo – `print_all_shortest_paths`

```python
def print_all_shortest_paths(start_station):

    start = stations.index(start_station)
    print(f"Start Station (Source): {start_station}
")

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

At the bottom:

```python
print_all_shortest_paths("SOL")
```

So in this run, Floyd–Warshall is basically used to answer:  
> “What are the shortest distances and routes from Solo to all other stations,  
> **assuming we already computed shortest paths for all pairs**?”

---

## 5. Overall Conclusion – Which Algorithm is Most Effective?

Based on the **same station dataset** and **start node Solo (`SOL`)**:

1. **BFS**  
   - Uses the adjacency matrix but treats every track as **equal cost**.  
   - It returns routes with the **minimum number of stations (hops)**.  
   - Good when the goal is **minimize transfers**, not distance.  
   - Not suitable if you care about **km or travel time**.

2. **Dijkstra**  
   - Uses the same adjacency matrix, but now fully uses the **distance values (km)**.  
   - Computes the **shortest-distance routes from Solo to all other stations** in one run.  
   - Time complexity with adjacency matrix: about `O(V²)`, which is very efficient for 26 stations.  
   - This is the most **practical and effective algorithm** for a **Solo-centric routing app**.

3. **Floyd–Warshall**  
   - Builds on an edge list but represents the same railway network.  
   - Computes **shortest distances for every possible pair of stations** (all-pairs shortest paths) in `O(V³)`.  
   - More expensive than Dijkstra for one source, but very powerful for **global analysis**: any station can be origin or destination without re-running an algorithm.

---

- For this project where the main task is:  
  **“Find the best routes from Solo to all stations in the network”**,  
  **Dijkstra’s algorithm is the most effective and appropriate choice** (distance-based, reasonably fast, and directly matches the passenger’s need).
- **BFS** is useful as a complementary view when you want **routes with minimum transfers**.
- **Floyd–Warshall** is best reserved for scenarios where you need **all-pairs shortest path information** (e.g., network planning, timetable optimization, or simulation), not just paths from Solo.
