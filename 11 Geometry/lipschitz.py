num_points = int(input())

points = []

for _ in range(num_points):                     #Leser inn alle punktene
    x, y = (eval(i) for i in input().split())
    points.append((x,y))

points.sort()                                   #Sorterer punktene etter x-koordinat

L = 0 

for i in range(num_points-1):                   #Går gjennom alle punktene og finner den største stigningstallet
    x0, y0 = points[i]
    x1, y1 = points[i+1]

    L = max(L, abs(y1-y0)/(x1-x0))              #Finner stigningstallet mellom punktene og sammenligner med L

print(L)