import sys
from collections import deque
sys.setrecursionlimit(10**4)

# Leser input 

n, e = (int(i) for i in input().split())

graph = [[] for _ in range(n)]
back_graph =  [[] for _ in range(n)]

for edge in range(e): 
    start, finish = (int(i)-1 for i in input().split())
    graph[start].append(finish)
    back_graph[finish].append(start)


def find_reachable(start, graph):                #BFS
    is_reachable_from_two = [False]*n
    queue = deque()
    queue.append(start)
    is_reachable_from_two[start] = True
    
    while len(queue) > 0: 
        node = queue.popleft()
        for neighbour in graph[node]: 
            if not is_reachable_from_two[neighbour]:
                is_reachable_from_two[neighbour] = True
                queue.append(neighbour)
    
    return is_reachable_from_two

is_reachable_from_two = find_reachable(1, back_graph)



visited = [False]*n
stack = [False]*n
postorder = []

def dfs_post_order(node): 
    stack[node] = True
    visited[node] = True 
    for neighbour in graph[node]:
        if is_reachable_from_two[node]:  
            if stack[neighbour]: 
                print('inf')
                exit() #cycle 
            if not visited[neighbour]: 
                dfs_post_order(neighbour)
    
    stack[node] = False
    postorder.append(node)

dfs_post_order(0)

dp = [0]*n
dp[1] = 1       #Fra by to(1) er det en vei til by ro(1)

for node in postorder: 
    for child in graph[node]: 
        dp[node] += dp[child]


output = dp[0]      #Vil vite antall veier fra by 1 (0)
if len(str(output)) > 9: 
    print(str(output)[-9:])

else:
    print(output)