
from collections import deque
n, m , c = (int(i) for i in input().split(' '))
# n = lengden til sekvensen 
# m = kravet til lengden på stillheten 
# c = max lyd for "stille" 

sounds = [int(i) for i in input().split(' ')]

max_queue = deque()
min_queue = deque()

max_indices = deque()
min_indices = deque()

if m == 1:                   # Special case, er lengden 1 er det ikke noe forskjell på støy 
    for i in range(n):
        print(i+1)
    exit()

is_silence = False

for i in range( n):     

    # Setter inn det nye elementet i max og min queue 

    if len(max_queue) == 0 or max_queue[0] < sounds[i]:      
        max_queue = deque([sounds[i]])
        max_indices = deque([i])
        
    else: 
        while max_queue[-1] < sounds[i]: 
            max_queue.pop()
            max_indices.pop()
        
        max_queue.append(sounds[i])
        max_indices.append(i)
    
    if len(min_queue) == 0 or min_queue[0] > sounds[i]: 
        min_queue = deque([sounds[i]])
        min_indices = deque([i])
        
    else: 
        while min_queue[-1] > sounds[i]: 
            min_queue.pop()
            min_indices.pop()
        
        min_queue.append(sounds[i])
        min_indices.append(i)

    # Fjerner elementer som går ut av slidingvinduet 

    if i-m >= max_indices[0]: 
        max_indices.popleft()
        max_queue.popleft()
    
    if i-m >= min_indices[0]: 
        min_indices.popleft()
        min_queue.popleft()

    # Sjekker om det er stille eller ikke 

    if i +1>= m and max_queue[0] - min_queue[0] <= c: 
        is_silence = True 
        print(i-m+2)

if not is_silence: 
    print('NONE')