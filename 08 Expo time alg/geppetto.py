# check if a set of vertices is an independent set
def is_IS(graph, vertices):
    for vertex in vertices:
        for neighbor in graph[vertex]:
            if neighbor in vertices:    #If any neighbor is in the set, it is not an independent set
                return False
    return True

#Counting independent sets
def num_IS(graph):
    n = len(graph)
    num_independentset = 0
    for i in range(2**n):                      #Iterate over all subsets of vertices
        subset = []                                  
        set_str = bin(i)[2:].rjust(n, '0')      #Convert i to binary string and pad with zeros to make it length n
        for j in range(n):                                  
            if set_str[j] == '1':
                subset.append(j)
        if is_IS(graph, subset):
            num_independentset += 1
    return num_independentset


# read input and creates undirected graph
num_nodes, num_edges = (int(i) for i in input().split())

graph = [[] for _ in range(num_nodes)]

for edge in range(num_edges): 
    n1, n2 = (int(i)-1 for i in input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)


print(num_IS(graph))