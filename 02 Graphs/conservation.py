# first line
num_cases = int(input())

# first line in each test case
# n - the number of conservation stages
# m - the number of dependencies between them

# second line in each test case

def solve(graph, indegree, lab, is_in_lab_0, L_0, L_1): 
    swaps = 0
    while not (len(L_0) == 0 and len(L_1) == 0):        # Så lenge du ikke har gjort alle oppgavene 

        if is_in_lab_0 and len(L_0) == 0:               # Hvis du er i den ene laben og ikke har noen oppgaver å gjøre:
            swaps += 1                                  # bytt til den andre labben å gjøre oppgaver der
            is_in_lab_0 = False 

        
        elif not is_in_lab_0 and len(L_1) == 0:         # samme som over
            swaps += 1
            is_in_lab_0 = True

        node = L_0.pop() if is_in_lab_0 else L_1.pop()  # Ta neste oppgave i den laben du er i
        for m in graph[node]:                           # Fjern at du har oppgaver igjen å gjøre før den neste 
            indegree[m] -= 1
            if indegree[m] == 0:                        # Hvis du har jobber som kan gjøres legg de til 
                if lab[m] == 0:
                    L_0.append(m)                       
                else: 
                    L_1.append(m)
        
    return swaps                                        # Returner antall bytter når du er feridg med alle oppgavene 


for case in range(num_cases):
    n, e = (int(i) for i in input().split(' '))

    lab = [(int(i) - 1) for i in input().split(' ')]

    graph = [[] for key in range(n)]
    indegree = [0] * n

    for edge in range(e):
        start, end = (int(i) - 1 for i in input().split(' '))
        graph[start].append(end)
        indegree[end] += 1 

    L_0 = []
    L_1 = []

    for node in range(n):
        if indegree[node] == 0 and lab[node] == 0:
            L_0.append(node)
        elif indegree[node] == 0 and lab[node] == 1: 
            L_1.append(node)
    

  
    swaps_if_start_lab_0 = solve(graph, indegree.copy(), lab, True, L_0.copy(), L_1.copy())  
    swaps_if_start_lab_1 = solve(graph, indegree.copy(), lab, False, L_0.copy(), L_1.copy())


    print(min(swaps_if_start_lab_0, swaps_if_start_lab_1))
