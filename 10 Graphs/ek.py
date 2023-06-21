import sys 
from math import sqrt

"From EK"

from collections import deque 

edges = lambda p: zip(p, p[1:])

def create_path(parent, s, t):
    path = [t]
    while t != s:
        t = parent[t]
        path.append(t)
    return tuple(reversed(path))

def bfs(res_graph, s, t):
    q = deque([s])
    parent = {}
    while q:
        v = q.popleft()
        for u in range(len(res_graph)): 
            if u in parent:
                continue # seen it before
            if res_graph[v][u] <= 0:
                continue # vu saturated
            parent[u] = v
            q.append(u)
            if u == t:
                return create_path(parent, s, t)

def maxflow(res_graph, s, t):
    flow = 0
    while P := bfs(res_graph, s, t):
        F = min(res_graph[v][u] for (v, u) in edges(P))
        flow += F
        for i in range(1, len(P)):
            v, u = P[i - 1], P[i]
            res_graph[v][u] -= F
            res_graph[u][v] += F
    return flow