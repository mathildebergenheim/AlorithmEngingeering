n, m , c = (int(i) for i in input().split(' '))

sounds = [int(i) for i in input().split(' ')]

check = sounds[:m]

for i in range(m, n):
    element_remove = check.pop(0)
    check.append(sounds[i])
    min_el = min(check)
    max_el = max(check)  

    if max_el - min_el <= c: 
        print(i-m+2)
