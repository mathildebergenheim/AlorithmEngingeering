from collections import deque

H = deque([int(i) for i in input().split()])
num_H = H.popleft()

B = deque([int(i) for i in input().split()])
num_B = B.popleft()

inf = float('inf')

#Initlialzing num_pakcs_H

total_sum_H = sum(H)          
dp_H = [inf]*(total_sum_H+1)
dp_H[0] = 0

for i in range(len(H)):                                # For hver pakke     
    for j in range(total_sum_H, H[i]-1, -1):              # Går bakover og ned til antallet i pakken (index)
        if H[i-1] <= j:                                     # Dersom innholde i pakken er større mindre enn j (indexen vi er på)
            dp_H[j] = min(dp_H[j], dp_H[j - H[i]] +1)       # Sjekker om det blir færre pakker om man tar denne pakken eller ikke
                                                            # gjøres ved å se hvor mange pakker som trengs på denne indeksen minus 
                                                            # antall pakker vi har i pakke #i, og sjekker det antallet pluss + 1 (med denne pakken)

# Initlialzing num_pakcs_B

total_sum_B = sum(B)          
dp_B = [inf]*(total_sum_B+1)
dp_B[0] = 0

for i in range(1, len(B)+1): 
    for j in range(total_sum_B, B[i-1]-1, -1): 
        if B[i-1] <= j: 
            dp_B[j] = min(dp_B[j], dp_B[j- B[i-1]] +1)
            

#Search for solution: 

is_possible = False
smallest_amount_of_packs = inf

for i in range(1, min(total_sum_H, total_sum_B)+1):         # Sjekker kun opp til minste av summen til innholde i pakkene 
    is_possible = True                                      # ^^ (finnes ikke noe svar mellom der og summen til innholde med mest)
    if dp_H[i] != inf and dp_B[i] != inf:                   
        smallest_amount_of_packs = min(dp_H[i]+dp_B[i], smallest_amount_of_packs) # summerer antall pakker som trengs for å nå antallet pølser og brød 


if is_possible:
    print(smallest_amount_of_packs)
else:
    print('impossible')