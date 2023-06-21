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
max_non_corssings  = [0]*(2*num_leaves)


func_left = lambda i : 2*i 
func_right = lambda i : 2*i +1 
func_parent = lambda i : i //2 
func_index = lambda T, i : len(T) // 2+i 


def update(tree, index, value, op=max):
    index = func_index(tree, index)
    tree[index] = value                                               # sykt smart (bare tenk)
    while (index := func_parent(index)):                                        # så lenge den ikke er null så går den 
        tree[index] = op([tree[func_left(index)], tree[func_right(index)]])


def query_(tree, l, r):
    l = func_index(tree, l)
    r = func_index(tree, r+1)              #fordi den er ikke-inklusiv r
    
    yield tree[l]                          # [l, r]
    while True:
        pl = func_parent(l)
        pr = func_parent(r)
        if pl == pr:                    # pointers meet here
            return 0
        if l % 2 == 0:                  # left goes right
            yield tree[func_right(pl)]          # ... collect subtree
        if r % 2 == 1:                  # right goes left
            yield tree[func_left(pr)]           # ... collect subtree
        l,r = pl, pr                    # go up


def query(tree, l, r, op=max):
    return op(query_(tree, l, r))


# end segment tree


for bridge in bridges: 
    max_crossing = query(max_non_corssings, 0, bridge) + 1 
    update(max_non_corssings, bridge, max_crossing)

print(max(max_non_corssings))