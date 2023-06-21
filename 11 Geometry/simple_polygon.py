def cross_product(p1, p2):
    cross = p1[0]*p2[1] - p1[1]*p2[0]
    return cross

def simple_polygon(points):

    # sorteer basert på x-koordinater, dersom de er like er det den minste y-verdien som kommer først
    sorted_points = sorted(points)

    p1 = sorted_points[0]                   #Finner det punktet med minst x-koordinat
    p2 = sorted_points[-1]                  #Finner det punktet med størst x-koordinat
    mid_line = (p2[0]-p1[0], p2[1]-p1[1])   #Finner linjen mellom de to punktene

    above_midline = []
    on_midline = []
    below_midline = []

    for point in sorted_points[1:-1]:           #Går gjennom alle punktene og finner hvilken side av linjen de er på
        cross = cross_product(mid_line, (point[0]-p1[0], point[1]-p1[1]))
        if cross < 0 :
            above_midline.append(point)
        elif cross == 0: 
            on_midline.append(point)
        else:
            below_midline.append(point)

    
    if len(on_midline) > 0:                             #Dersom det er punkter på linjen: sjekker hvilken side det er flest punkter på 
        if len(above_midline) > len(below_midline):     #Legger til punktene på linjen på den siden det er flest punkter 
            below_midline += on_midline                 
            below_midline = sorted(below_midline)       #Sorterer punktene på den siden

        else:
            above_midline += on_midline
            above_midline = sorted(above_midline)       #Sorterer punktene på den siden
        
    below_midline.reverse()                             #Reverserer punktene under linjen slik at de går med klokka

    polygon = []

    polygon.append(points_dict[p1])                 #legger til punktet lengst til venstre

    for point in above_midline:                     #legger til punktene over linjen
        polygon.append(points_dict[point])

    polygon.append(points_dict[p2])                 #legger til det punket lengst til høyre

    for point in below_midline: 
        polygon.append(points_dict[point])          #legger til punktene under linjen

    return polygon



num_problems = int(input())

for _ in range(num_problems):
    inp = [int(i) for i in input().split()]
    num_points = inp.pop(0)
    index = 0 

    points_dict = {}
    points_list = []

    for n in range(num_points): 
        x = inp[index]
        y = inp[index+1]
        points_list.append((x, y))
        points_dict[(x, y)] = n
        index += 2
    
    poly = [str(e) for e in simple_polygon(points_list)]
    print(' '.join(poly))
