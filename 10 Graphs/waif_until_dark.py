
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

"End EK"

n, m, p = (int(i) for i in input().split()) # n = children, m = toys, p = categories

dim = n + m + p + 2 #2 is for s and t 

s = 0
t = n + m + p + 1

toys_without_cat = [int(i)+1 for i in range(m)]

res_graph = [[0]*dim for _ in range(dim)]

for child in range(n): 
    child_pref = [int(i) for i in input().split()]
    num_pref = child_pref.pop(0)

    res_graph[s][child+1] = 1

    for toy in child_pref:
        res_graph[child+1][toy+n] = 1             #Trenger ikke pluss en

for c in range(p): 
    cat = [int(i) for i in input().split()]
    num_in_cat = cat.pop(0)
    num_use = cat.pop()

    res_graph[c+n+m+1][t] = num_use

    for toy in cat: 
        res_graph[toy+n][c+n+m+1] = 1
        toys_without_cat.remove(toy)
    
for toy in toys_without_cat: 
    res_graph[toy+n][t] = 1

print(maxflow(res_graph, s, t))
