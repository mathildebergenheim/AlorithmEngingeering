import sys 
from math import sqrt

"From EK"

from collections import deque 

edges = lambda p: zip(p, p[1:])         # zip([1,2,3], [4,5,6]) -> [(1,4), (2,5), (3,6)]

def create_path(parent, s, t):          # create a path from s to t using the parent dictionary
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
            if u in parent: # seen it before
                continue 
            if res_graph[v][u] <= 0: # vu saturated
                continue 
            parent[u] = v # add v as the parent of u
            q.append(u) # add u to the queue
            if u == t:  # if we have reached t
                return create_path(parent, s, t)

def maxflow(res_graph, s, t):
    flow = 0
    while P := bfs(res_graph, s, t):                        # while there is a path from s to t
        F = min(res_graph[v][u] for (v, u) in edges(P))     # find the minimum capacity of the path
        flow += F                                           # add the flow to the total flow
        for i in range(1, len(P)):                          # for each edge in the path
            v, u = P[i - 1], P[i]                           # get the nodes of the edge
            res_graph[v][u] -= F                            # subtract the flow from the capacity
            res_graph[u][v] += F                            # add the flow to the reverse edge
    return flow

"End EK"


while line:= sys.stdin.readline().split():      # while there is a line to read
    n, m, s, v = (int(i) for i in line)         # n = antall gophers, m = antall gopherhull, s = tid til angrep, v = fart til gopher

    max_distance = v*s      # max distance a gopher can run in s seconds

    gophers = []
    holes = []

    for _ in range(n): 
        gophers.append([float(el) for el in input().split()])
    
    for _ in range(m): 
        holes.append([float(el) for el in input().split()])

    s = 0                                                       # source
    t = n+m +1                                                  # sink

    res_graph = [[0]*(n+m+2) for _ in range(n+m+2)]             # residual graph

    for g in range(n): 

        res_graph[s][g+1] = 1                               # add an edge from the source to the gopher

        for h in range(m): 

            res_graph[h+n+1][t] = 1                         # add an edge from the hole to the sink

            gx, gy = gophers[g]
            hx, hy = holes[h]

            dist = sqrt( (gx-hx)**2 + (gy-hy)**2)

            if dist <= max_distance:                    # if the gopher can reach the hole in time

                res_graph[g+1][h+n+1] = 1               # add an edge from the gopher to the hole


    num_savede = maxflow(res_graph, s, t)
    print(n - num_savede)
