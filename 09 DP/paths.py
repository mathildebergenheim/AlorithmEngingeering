
" Reading input "
num_nodes, num_edges, num_colors = (int(i) for i in input().split())
node_colors = [int(i)-1 for i in input().split()]
graph = [[] for _ in range(num_nodes)]

for edge in range(num_edges):
    start, end = (int(i)-1 for i in input().split())
    graph[start].append(end)
    graph[end].append(start)


" Solving problem "
dp = [[-1 for _ in range(2**num_colors)] for _ in range(num_nodes)]     #use bitmask 0-2^numcolors (maks 2^5 = 32)
                                                                        #dp[node][bitmask] = antall paths fra noden med sett med farger bitmask   

num_paths = 0

def dfs(node, dp, seen_colors):         #node:int, dp:2darray, seen_colors:bitmask 
    if dp[node][seen_colors] != -1:     #Hvis vi har regnet ut antall paths fra denne noden med denne bitmasken før
        return dp[node][seen_colors]    #returner antall paths fra denne noden med denne bitmasken

    num_paths_from_node = 0             #Hvis ikke, så regner vi ut antall paths fra denne noden med denne bitmasken

    for child in graph[node]:
        if (1 << node_colors[child]) & seen_colors:   #Hvis vi har sett fargen før forsetter vi til neste barn 
            continue
        else:
            seen_colors_child = seen_colors | (1 <<  node_colors[child])    #Hvis ikke, så legger vi til fargen til bitmasken
            num_paths_from_node += dfs(child, dp, seen_colors_child) + 1    # og oppdaterer antall paths fra denne noden med denne bitmasken
    
    dp[node][seen_colors] = num_paths_from_node
    return num_paths_from_node


for node in range(len(graph)): 
    num_paths += dfs(node, dp, (1<<node_colors[node]))

print(num_paths)