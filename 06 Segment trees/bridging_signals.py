from math import ceil, log2
num_bridges = int(input())

bridges = []

for _ in range(num_bridges): 
    bridges.append(int(input())-1)

#Creating Segment tree
def nearest_larger_power_of_2(x):
    n = ceil(log2(x))
    return 2**n

num_leaves = nearest_larger_power_of_2(num_bridges)
max_non_corssings  = [0]*(2*num_leaves)             #The three


#func_left = lambda i : 2*i 
#func_right = lambda i : 2*i +1 
#func_parent = lambda i : i //2 
#func_index = lambda T, i : len(T) // 2+i 


def update(tree, index, value, op=max):
    index = len(tree) // 2 + index
    # index = func_index(tree, index)
    tree[index] = value                                               # sykt smart (bare tenk)
    while (index := index//2):                                        # så lenge den ikke er null så går den 
        tree[index] = op([tree[2*index], tree[2*index +1]])


def query_(tree, l, r):
    l = len(tree) //  2 + l
    r = len(tree) // 2 + (r+1) 
    # l = func_index(tree, l)
    # r = func_index(tree, r+1)              #fordi den er ikke-inklusiv r
    #yield tree[l]                          # [l, r]
    maxen = tree[l]
    while r-l > 1:
        if l % 2 == 0:                  # left goes right
            maxen = max(maxen, tree[l+1])             # ... collect subtree       tree[func_right(pl)] = tree[l+1]
        if r % 2 == 1:                  # right goes left
            maxen = max(maxen, tree[r-1])             # ... collect subtree       tree[func_left(pr)] = tree[r-1]
        l,r = l //2, r//2                    # go up

    return maxen

def query(tree, l, r):
    return query_(tree, l, r)

# end segment tree


for bridge in bridges: 
    max_crossing = query(max_non_corssings, 0, bridge) + 1 
    update(max_non_corssings, bridge, max_crossing)

print(max(max_non_corssings))