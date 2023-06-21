from collections import defaultdict
num_tb = int(input())

def next_id(): 
    return len(buildings)

parent = {}
size = defaultdict(lambda:1)            #Når alltid seg selv
buildings = defaultdict(next_id)        #Ny bygning får ID len(av bygg som var der)


def find(node): 
    current_parent = node

    while current_parent in parent:
        current_parent = parent[current_parent]

    return current_parent


def union(node1, node2): 
    parent1 = find(node1)
    parent2 = find(node2)

    if parent1 == parent2:
        return max(size[parent1], size[parent2])
    
    if size[parent1] > size[parent2]:
        parent[parent2] = parent1
        size[parent1] += size[parent2]

    else: 
        parent[parent1] = parent2
        size[parent2] += size[parent1]
    
    return max(size[parent1], size[parent2])


for _ in range(num_tb): 
    b1, b2 = (i for i in input().split())

    node1 = buildings[b1]
    node2 = buildings[b2]

    print(union(node1, node2))

