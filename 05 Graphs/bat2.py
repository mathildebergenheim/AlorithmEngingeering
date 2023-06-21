
parent = []
rank = []
buildings = []

def find(node): 
    current_parent = node

    while current_parent != parent[node]:
        current_parent = parent[current_parent]

    return current_parent


def union(node1, node2): 
    parent1 = find(node1)
    parent2 = find(node2)

    if parent1 == parent2:
        return 0
    
    if rank[parent1] > rank[parent2]:
        parent[parent2] = parent1
        rank[parent1] += rank[parent2]

    else: 
        parent[parent1] = parent2
        rank[parent2] += rank[parent1]

    
    return max(rank[parent1], rank[parent2])

