import heapq
from queue import Queue
import time


def read_maze(maze_str):
    maze = [list(row) for row in maze_str.split('\n')]
    return maze


def print_maze(maze):
    for row in maze:
        print(''.join(row))
    print()


def find_symbol(maze, symbol):
    for i, row in enumerate(maze):
        for j, cell in enumerate(row):
            if cell == symbol:
                return i, j


def is_valid(maze, i, j):
    return 0 <= i < len(maze) and 0 <= j < len(maze[0]) and maze[i][j] != '+'


def bfs(maze, start, goal):
    queue = Queue()
    visited = set()
    came_from = {}  # Agregar esta línea
    queue.put(start)
    visited.add(start)

    while not queue.empty():
        current = queue.get()
        i, j = current

        if current == goal:
            return reconstruct_path(start, goal, came_from)  # Corregir aquí

        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = i + di, j + dj
            neighbor = (ni, nj)

            if is_valid(maze, ni, nj) and neighbor not in visited:
                queue.put(neighbor)
                visited.add(neighbor)
                came_from[neighbor] = current


def dfs(maze, start, goal):
    stack = []
    visited = set()
    came_from = {}  # Agregar esta línea
    stack.append(start)
    visited.add(start)

    while stack:
        current = stack.pop()
        i, j = current

        if current == goal:
            return reconstruct_path(start, goal, came_from)  # Corregir aquí

        neighbors = [(i + di, j + dj) for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)] if
                     is_valid(maze, i + di, j + dj)]

        for neighbor in neighbors:
            if neighbor not in visited:
                stack.append(neighbor)
                visited.add(neighbor)
                came_from[neighbor] = current


def ucs(maze, start, goal):
    heap = [(0, start, [])]
    visited = set()

    while heap:
        cost, current, path = heapq.heappop(heap)
        i, j = current

        if current == goal:
            return path + [current]

        if current not in visited:
            visited.add(current)

            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ni, nj = i + di, j + dj
                neighbor = (ni, nj)

                if is_valid(maze, ni, nj) and neighbor not in visited:
                    heapq.heappush(heap, (cost + 1, neighbor, path + [current]))


def astar(maze, start, goal):
    heap = [(heuristic(start, goal), 0, start, [])]
    visited = set()

    while heap:
        _, cost, current, path = heapq.heappop(heap)
        i, j = current

        if current == goal:
            return path + [current]

        if current not in visited:
            visited.add(current)

            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ni, nj = i + di, j + dj
                neighbor = (ni, nj)

                if is_valid(maze, ni, nj) and neighbor not in visited:
                    heapq.heappush(heap, (cost + 1 + heuristic(neighbor, goal), cost + 1, neighbor, path + [current]))


def idastar(maze, start, goal):
    threshold = heuristic(start, goal)
    path = [start]

    while True:
        result, new_threshold = idastar_search(maze, start, goal, threshold, path, set())
        if result is not None:
            return result
        threshold = new_threshold


def idastar_search(maze, current, goal, threshold, path, visited):
    i, j = current
    cost = len(path) - 1 + heuristic(current, goal)

    if cost > threshold:
        return None, cost

    if current == goal:
        return path, threshold

    min_cost = float('inf')
    visited.add(current)

    for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        ni, nj = i + di, j + dj
        neighbor = (ni, nj)

        if is_valid(maze, ni, nj) and neighbor not in visited:
            result, new_threshold = idastar_search(maze, neighbor, goal, threshold, path + [neighbor], visited)
            if result is not None:
                return result, threshold
            min_cost = min(min_cost, new_threshold)

    visited.remove(current)
    return None, min_cost


def heuristic(current, goal):
    return abs(current[0] - goal[0]) + abs(current[1] - goal[1])


def reconstruct_path(start, goal, came_from):
    current = goal
    path = []

    while current != start:
        path.insert(0, current)
        current = came_from[current]

    return path


maze_str = """++++++++++++++++++++++
+ O +   ++ ++        +
+     +     +++++++ ++
+ +    ++  ++++ +++ ++
+ +   + + ++         +
+          ++  ++  + +
+++++ + +      ++  + +
+++++ +++  + +  ++   +
+          + +  + +  +
+++++ +  + + +     X +
++++++++++++++++++++++"""

maze = read_maze(maze_str)
start = find_symbol(maze, 'O')
goal = find_symbol(maze, 'X')

print("Laberinto:")
print_maze(maze)

print("Solución usando BFS:")
bfs_path = bfs(maze, start, goal)
print(bfs_path)
start_time = time.time()
bfs_path = bfs(maze, start, goal)
end_time = time.time()
print("Tiempo de ejecución de BFS:", end_time - start_time)

print("\nSolución usando DFS:")
dfs_path = dfs(maze, start, goal)
print(dfs_path)
start_time = time.time()
dfs_path = dfs(maze, start, goal)
end_time = time.time()
print("Tiempo de ejecución de DFS:", end_time - start_time)

print("\nSolución usando Costo Uniforme:")
ucs_path = ucs(maze, start, goal)
print(ucs_path)
start_time = time.time()
ucs_path = ucs(maze, start, goal)
end_time = time.time()
print("Tiempo de ejecución de DFS:", end_time - start_time)

print("\nSolución usando A*:")
astar_path = astar(maze, start, goal)
print(astar_path)
start_time = time.time()
astar_path = astar(maze, start, goal)
end_time = time.time()
print("Tiempo de ejecución de DFS:", end_time - start_time)

print("\nSolución usando IDA*:")
idastar_path = idastar(maze, start, goal)
print(idastar_path)
start_time = time.time()
idastar_path = idastar(maze, start, goal)
end_time = time.time()
print("Tiempo de ejecución de DFS:", end_time - start_time)
