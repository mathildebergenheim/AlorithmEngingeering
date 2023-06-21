'''
L ← Empty list that will contain the sorted elements
S ← Set of all nodes with no incoming edge

while S is not empty do
    remove a node n from S
    add n to L
    for each node m with an edge e from n to m do
        remove edge e from the graph
        if m has no other incoming edges then
            insert m into S


'''


n, e = (int(i) for i in input().split(' '))

graph = [[] for key in range(n)]
indegree = [0] * n


# Lager grafen og en oversikt over indegree 
for edge in range(e):
    start, end = (int(i) for i in input().split(' '))
    graph[start].append(end)
    indegree[end] += 1 

L = []
S = []

# Legger til alle nodene som ikke har noen noder inn til seg 
for node in range(n):
    if indegree[node] == 0:
        S.append(node) 


while len(S) > 0: 
    if len(S) > 1: 
        print('back to the lab')
        exit()
    node = S.pop()
    L.append(node)
    for m in graph[node]:
        indegree[m] -= 1
        if indegree[m] == 0:        #Hvis det da er flere noder med indegree 0, så er det ikke EN topologisk rekkefølge 
            S.append(m)

    
print(*L)

