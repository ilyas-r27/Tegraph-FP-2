import heapq
import math


#  HEURISTIC FUNCTION
def heuristic(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)



#  A* ALGORITHM
def a_star(graph, coordinates, start, goal):
    open_set = []
    heapq.heappush(open_set, (0, start))

    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0

    f_score = {node: float('inf') for node in graph}
    f_score[start] = heuristic(coordinates[start], coordinates[goal])

    came_from = {node: None for node in graph}

    while open_set:
        current = heapq.heappop(open_set)[1]

        if current == goal:
            return reconstruct_path(came_from, current), g_score[current]

        for neighbor, cost in graph[current]:
            tentative_g = g_score[current] + cost

            if tentative_g < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f_score[neighbor] = tentative_g + heuristic(coordinates[neighbor], coordinates[goal])
                heapq.heappush(open_set, (f_score[neighbor], neighbor))

    return None, float('inf')



#  RECONSTRUCT PATH
def reconstruct_path(came_from, current):
    path = [current]
    while came_from[current] is not None:
        current = came_from[current]
        path.append(current)
    path.reverse()
    return path



#  UPDATED GRAPH (from your image)
graph = {
    "Gubeng": [("Wonokromo", 5.9)],
    "Wonokromo": [("Gubeng", 5.9), ("Sidoarjo", 17.6), ("Mojokerto", 38)],
    "Sidoarjo": [("Wonokromo", 17.6), ("Bangil", 21.5)],
    "Bangil": [("Sidoarjo", 21.5), ("Lawang", 40.5)],
    "Lawang": [("Bangil", 40.5), ("Malang", 18.6)],
    "Malang": [("Lawang", 18.6)],

    # Jalur bawah
    "Mojokerto": [("Wonokromo", 38), ("Kertosono", 42.9)],
    "Kertosono": [("Mojokerto", 42.9), ("Kediri", 25.2)],
    "Kediri": [("Kertosono", 25.2), ("Blitar", 54.8)],
    "Blitar": [("Kediri", 54.8), ("Malang", 59.2)]
}


#  ESTIMATED COORDINATES (for heuristic)

coordinates = {
    "Gubeng": (0, 0),
    "Wonokromo": (1, -1),
    "Sidoarjo": (5, -2),
    "Bangil": (9, -2.5),
    "Lawang": (14, -3),
    "Malang": (16, -4),

    "Mojokerto": (1, -5),
    "Kertosono": (4, -7),
    "Kediri": (8, -9),
    "Blitar": (12, -11),
}


#  RUN A*
start = "Gubeng"
end = "Malang"

path, distance = a_star(graph, coordinates, start, end)

print("Best route using A*:")
print(" -> ".join(path))
print(f"Total distance: {distance}")
