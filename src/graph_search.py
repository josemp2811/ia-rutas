"""
Construye grafo y aplica Dijkstra o A* (si hay coords).
"""
import heapq
import math

class Graph:
    def __init__(self):
        self.adj = {}

    def add_edge(self, u, v, w):
        self.adj.setdefault(u, []).append((v, w))
        self.adj.setdefault(v, []).append((u, w))  # bidireccional

    def neighbors(self, u):
        return self.adj.get(u, [])

def dijkstra(graph, start, goal):
    pq = [(0, start, None)]
    dist = {start: 0}
    parent = {start: None}
    visited = set()

    while pq:
        d, node, _ = heapq.heappop(pq)
        if node in visited:
            continue
        visited.add(node)
        if node == goal:
            break
        for neigh, w in graph.neighbors(node):
            nd = d + w
            if nd < dist.get(neigh, float('inf')):
                dist[neigh] = nd
                parent[neigh] = node
                heapq.heappush(pq, (nd, neigh, node))

    if goal not in parent:
        return None, float('inf')
    # reconstruir camino
    path = []
    cur = goal
    while cur:
        path.append(cur)
        cur = parent[cur]
    path.reverse()
    return path, dist[goal]

def heuristic_coords(a, b, coords):
    (lon1, lat1) = coords.get(a, (0,0))
    (lon2, lat2) = coords.get(b, (0,0))
    # Euclidian approx (no proyectada) — suficiente para heurística
    return math.hypot(lon1 - lon2, lat1 - lat2)

def astar(graph, start, goal, coords):
    open_set = [(0 + heuristic_coords(start, goal, coords), 0, start, None)]
    gscore = {start: 0}
    parent = {start: None}
    closed = set()

    while open_set:
        f, g, node, _ = heapq.heappop(open_set)
        if node in closed:
            continue
        if node == goal:
            break
        closed.add(node)
        for neigh, w in graph.neighbors(node):
            tentative_g = g + w
            if tentative_g < gscore.get(neigh, float('inf')):
                gscore[neigh] = tentative_g
                parent[neigh] = node
                fscore = tentative_g + heuristic_coords(neigh, goal, coords)
                heapq.heappush(open_set, (fscore, tentative_g, neigh, node))

    if goal not in parent:
        return None, float('inf')
    path = []
    cur = goal
    while cur:
        path.append(cur)
        cur = parent[cur]
    path.reverse()
    return path, gscore[goal]
