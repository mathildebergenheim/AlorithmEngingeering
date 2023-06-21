from math import ceil, log2
n, k = (int(i) for i in input().split())

def nearest_larger_power_of_2(x):
    n = ceil(log2(x))
    return 2**n

num_leaves = nearest_larger_power_of_2(n)
tree = [0]*(2*num_leaves)


func_left = lambda i : 2*i 
func_right = lambda i : 2*i +1 
func_parent = lambda i : i //2 
func_index = lambda T, i : len(T) // 2+i 


def update(tree, index, op=sum):
    index = func_index(tree, index)
    tree[index] = 1 - tree[index]                                       #sykt smart (bare tenk): hvis den er 0 -> 1-0=1... hvis den er 1 -> 1-1=0 
    while (index := func_parent(index)):                                     # så lenge den ikke er null så går den 
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

def query(tree, l, r, op=sum):
    return op(query_(tree, l, r))


for _ in range(k): 
    do = input().split()
    if do[0] == 'F': 
        i = int(do[1])
        update(tree, i)
    else:
        l = int(do[1])
        r = int(do[2]) 
        print(query(tree, l, r))
