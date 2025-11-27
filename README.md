# GROUP 2


| Name           | NRP        | Kelas     |
| ---            | ---        | ----------|
| Kenzie Maheswara | 5025241001 | IUP |
| Palpal Yalmialam | 5025241002 | IUP |
| Muhammad Ilyas Rusdi | 5025241007 | IUP |
| M. Arifathan Mahardika | 5025241013 | IUP |



<img width="902" height="509" alt="image" src="https://github.com/user-attachments/assets/4527e28e-77c9-471f-abe6-db14de46e760" />


# Shortest Path of Surabaya–Malang Train Stations (Dijkstra)

This project uses **Dijkstra’s Algorithm** to find the shortest distance from  
**St. Gubeng (SGU)** to all other stations in the railway map.

The code works on the station network shown in the visualization:

- **SGU** – St. Gubeng  
- **WO** – St. Wonokromo  
- **SDA** – St. Sidoarjo  
- **BG** – Bangil  
- **LW** – St. Lawang  
- **ML** – St. Malang  
- **MR** – St. Mojokerto  
- **KTS** – St. Kertosono  
- **KD** – St. Kediri  
- **BL** – St. Blitar  

Each black line in the picture is a **track segment** between two stations, and the
number next to it is the **distance in kilometers** (edge weight).

---

## 1. How the Map Is Translated Into Code

### 1.1 Nodes (Stations)

```python
nodes = ["SGU", "WO", "SDA", "BG", "LW", "ML", "MR", "KTS", "KD", "BL"]
```

This list stores all **station codes**.  
The **index** of each element is the ID of that station in the graph:

- `0 -> SGU`, `1 -> WO`, `2 -> SDA`, …, `9 -> BL`.

So, whenever the algorithm says “node 0”, it actually means **St. Gubeng**.

---

### 1.2 Adjacency Matrix (Track Distances)

```python
inf = float('inf')

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
```

- `graph[i][j]` = distance from station `nodes[i]` to `nodes[j]`.
- `0` on the diagonal means **distance from a station to itself is 0**.
- `inf` means **there is no direct track** between those two stations.
- The numbers (5.8, 17.6, 40.5, etc.) come directly from the map in the visualisation.

Example:

- `graph[0][1] = 5.8`  
  → distance SGU → WO is 5.8 km (matches the “5.8” label on the picture).
- `graph[1][6] = 38.0`  
  → direct track from WO to MR is 38.0 km (vertical line on the left branch).
- `graph[5][9] = 58.2`  
  → track from ML to BL is 58.2 km (bottom-right branch).

This matrix is the **“digital version” of your station map**.

---

## 2. Dijkstra’s Algorithm Function

### 2.1 `dijkstra(graph, start_node_index)`

```python
def dijkstra(graph, start_node_index):
    """
    Implementation of Dijkstra's Algorithm using an Adjacency Matrix.
    """
    num_nodes = len(graph)
    
    # Initialize "memory" arrays
    distances = [inf] * num_nodes
    visited = [False] * num_nodes
    previous_nodes = [-1] * num_nodes

    distances[start_node_index] = 0
``

- `num_nodes` = total number of stations.
- `distances[i]` = **current best known distance** from the start station to station `i`.
- `visited[i]` = True if station `i` has already been “finalized” by the algorithm.
- `previous_nodes[i]` = **parent station** on the shortest path to `i`.
- Distance from start station to itself is 0.

#### Main Loop

```python
    for _ in range(num_nodes):
        # 1. Pick the unvisited node with smallest distance
        min_dist = inf
        u = -1

        for i in range(num_nodes):
            if not visited[i] and distances[i] < min_dist:
                min_dist = distances[i]
                u = i

        if u == -1:
            break

        # 2. Mark that node as visited
        visited[u] = True
```
## Overview

This function is the core of Dijkstra’s algorithm that works on a **graph represented as an adjacency matrix** and a given **start node** (start station). It computes the shortest path distances from the start node to all other nodes.

---

## Variable Initialization

- `num_nodes = len(graph)`  
  Counts how many nodes (stations) there are in the graph.

- `distances = [inf] * num_nodes`  
  Creates an array that stores the **current shortest known distance** from the start node to every other node.  
  At the beginning, all values are set to infinity (`inf`) because no paths are known yet.

- `visited = [False] * num_nodes`  
  Keeps track of which nodes have been **“finalized”** by the algorithm (i.e., nodes whose shortest distance has already been confirmed).

- `previous_nodes = [-1] * num_nodes`  
  Stores the **previous node** on the shortest path for each node.  
  This is later used to reconstruct the actual path (by backtracking from the destination back to the start).

- `distances[start_node_index] = 0`  
  The distance from the start node to itself is **0**, so this becomes our starting point.

### 1. Iteration Over All Nodes

The outer loop `for _ in range(num_nodes):` runs up to `num_nodes` times.  
In each iteration, the algorithm tries to **finalize one more node** (confirm its shortest distance).

### 2. Selecting the Next Node `u`

Inside the loop, we search for the node `u` that:

- has **not** been visited yet (`not visited[i]`), and  
- has the **smallest current distance** in the `distances` array (`distances[i] < min_dist`).

This is done by scanning all nodes and keeping track of the smallest distance found so far.

If, after checking all nodes, no suitable node is found (`u == -1`), it means **there are no more reachable unvisited nodes**. In that case, the algorithm stops early with `break`.

  

---
#### Relaxation Step (Updating Neighbors)

```python
        # 3. Relax neighbors of u
        for v in range(num_nodes):
            if graph[u][v] > 0 and not visited[v]:
                new_dist = distances[u] + graph[u][v]
                if new_dist < distances[v]:
                    distances[v] = new_dist
                    previous_nodes[v] = u
```

For every neighbor `v` of station `u`:

- `graph[u][v] > 0` means there is a direct track from `u` to `v`.
- The algorithm calculates a **new possible distance**:
  ```python
  new_dist = distances[u] + graph[u][v]
  ```
  (distance from start → u → v)
- If this new distance is **shorter** than the previous value in `distances[v]`,
  it **updates**:
  - `distances[v]` to `new_dist`
  - `previous_nodes[v]` to `u`, meaning:
    > “The best path to get to station `v` currently goes through station `u`.”

At the end, the function returns:

```python
    return distances, previous_nodes
```

- `distances`  → shortest distance from the start to every station.  
- `previous_nodes` → information needed to rebuild the actual routes.

---

## 3. Reconstructing Paths

### 3.1 `get_path(previous_nodes, node_names, start_index, end_index)`

```python
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
    
    path.reverse()
    
    if path[0] == node_names[start_index]:
        return " -> ".join(path)
    else:
        return "No path"
```

What this function does:

1. Start from the **destination station** (`end_index`).
2. Use `previous_nodes` to walk **backwards**:
   - from BL → ML → LW → BG → SDA → WO → SGU, for example.
3. Collect all station codes in a list `path`.
4. Reverse the list so that it becomes:
   - SGU → WO → SDA → BG → LW → ML → BL
5. Join them with `" -> "` to produce a human-readable route string:
   - `"SGU -> WO -> SDA -> BG -> LW -> ML -> BL"`

If the path does not start with the original start station, it returns `"No path"`.

This is how the code turns the algorithm’s internal memory into a clear route
that matches the lines on your station map.

---

## 4. Main Program Flow

```python
start_station = "SGU"
start_index = nodes.index(start_station)

distances, prev_nodes = dijkstra(graph, start_index)
```

- The program chooses **St. Gubeng (SGU)** as the **source station**.
- It finds the index of `"SGU"` in the `nodes` list.
- It runs `dijkstra` to compute:
  - `distances` from SGU to all other stations.
  - `prev_nodes` used later to reconstruct each route.

### 4.1 Printing the Results

```python
print(f"========= DIJKSTRA'S ALGORITHM RESULTS =========\n")
print(f"Start Station (Source): {start_station}\n")
print(f"{'Destination':<16} | {'Shortest Distance (km)':<22} | {'Shortest Path':<40}")
print("-" * 80)

for i in range(len(nodes)):
    if i == start_index:
        continue  # Skip the start station

    distance = distances[i]
    
    if distance == inf:
        print(f"{nodes[i]:<16} | {'Not Reachable':<22} | -")
    else:
        path_str = get_path(prev_nodes, nodes, start_index, i)
        print(f"{nodes[i]:<16} | {distance:<22.1f} | {path_str}")
```

For each station:

- If the distance is `inf`, there is **no route** from SGU to that station.
- Otherwise:
  - It prints the **shortest distance** (total km).
  - It calls `get_path` to show the **exact sequence of stations**.

Example of one row (conceptually):

- From SGU to ML:  
  `SGU -> WO -> SDA -> BG -> LW -> ML`  
  The total distance is the sum of all segments in the map:
  - SGU–WO (5.8)  
  - WO–SDA (17.6)  
  - SDA–BG (21.5)  
  - BG–LW (40.5)  
  - LW–ML (18.6)  
  → The algorithm adds exactly these values, just like you would by hand.

---

## 5. Relation to the Station Map

- The **nodes list** is the list of houses (stations) on the visualisation.
- The **adjacency matrix** is the table version of all the black lines and numbers.
- **Dijkstra’s algorithm** is basically a “smart traveler” starting at SGU
  and exploring the network, always expanding from the currently closest station.
- The final output table tells you, for every station on the map:
  1. how far it is from SGU in km, and  
  2. which route (sequence of stations) you should follow to get the **shortest total distance**.

---

