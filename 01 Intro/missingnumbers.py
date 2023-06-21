
num = int(input())

last = 0
missing = False

for i in range(num):
    current = int(input())
    if current == last +1: 
        last = current
        continue
    else: 
        missing = True
        for missing in range(last +1 , current): 
            print(missing)
        last = current

if not missing: 
    print('good job')