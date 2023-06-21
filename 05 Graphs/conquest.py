import heapq

n, e = (int(i) for i in input().split())
graph = [[] for _ in range(n)]
for _ in range(e): 
    i1, i2 = (int(i)-1 for i in input().split())
    graph[i1].append(i2)
    graph[i2].append(i1)

army_sizes = []
for _ in range(n):
    army_sizes.append(int(input()))


sp_army_size = army_sizes[0]
que = []
visited = [False]*n
visited[0] = True 

#Initilizing islands to conquest from start 
for neighbour in graph[0]:
    if not visited[neighbour]:
        heapq.heappush(que, (army_sizes[neighbour], neighbour))
        visited[neighbour] = True


while que:
    army_size, node = heapq.heappop(que)         #checking if we can attack the island with the smallest army 
    if army_size < sp_army_size: 
        sp_army_size += army_size
        for neighbour in graph[node]:           #Adding the neighbours to the island joined SP   
            if not visited[neighbour]:
                visited[neighbour] = True 
                heapq.heappush(que, (army_sizes[neighbour], neighbour))
    
    else:                                       #If not, we cant attak the bigger island either 
        break

print(sp_army_size)
                
