
num_inputs = int(input())

for _ in range(num_inputs): 
    inputs = [float(i) for i in input().split()]
    x, y, w, h, r = inputs[:5]


    m = int(inputs[5])
    index = 6 

    for num_points in range(m):
        px = inputs[index]
        py = inputs[index + 1]
        index += 2

        #Inside box1
        if px >= x+r and px <= x+r + w-2*r and py >= y and py <= y + h:
            print('inside')
        #Inside box2
        elif px >= x and px <= x + w and py >= y + r and py <= y + r + h - 2*r:
            print('inside')

        #Inside cir1
        elif (px - (x+r))**2 + (py - (y+r))**2 <= r**2: 
            print('inside')
        #Inside cir2
        elif (px - (x+r))**2 + (py - (y+h-r))**2 <= r**2: 
            print('inside')
        #Inside cir3
        elif (px - (x+w-r))**2 + (py - (y+r))**2 <= r**2: 
            print('inside')
        #Inside cir4
        elif (px - (x+w-r))**2 + (py - (y+h-r))**2 <= r**2:  
            print('inside')
        else: 
            print('outside')
    
    print()