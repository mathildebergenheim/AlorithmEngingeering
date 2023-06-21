from collections import defaultdict


num_relations = int(input())
company_tree = defaultdict(lambda:[])
speeds = {}
inputs = []


dp_in = {}              #Hvor mange par kan dannes under denne noden om denne noden er med i paret
dp_out = {}             #Hvor mange par kan dannes under denne noden om denne noden ikke er med i paret
dp_in_max = {}          
dp_out_max = {}     

#Leser inn input:
for relation in range(num_relations):
    employee, speed, supervisor = (input().split())
    speed = float(speed)
    speeds[employee] = speed                            #Lagrer hastigheten til hver ansatt

    inputs.append([employee, speed, supervisor])

    dp_in[employee] = 0                                     
    dp_out[employee] = 0                                
    dp_in_max[employee] = 0
    dp_out_max[employee] = 0

#Lager treet:
#company_tree[sjef] = [[undersått, hastighet], [undersått, hastighet], ...]
for relation in inputs: 
    employee, speed, supervisor = relation
    speed = float(speed)

    if supervisor != 'CEO': 
        company_tree[supervisor].append([employee, min(speeds[employee], speeds[supervisor])])   #Legger til barnet og hastigheten til den tregeste

    else: 
        ceo = employee                         #Lagrer CEO-en

#Starting to solve problem: 


#maksimal kardinal matching
def dfs(node): 
    for child, speed in company_tree[node]:                                         
        dfs(child)                                                                  #Går gjennom alle barna til barna til noden

    for child, speed in company_tree[node]:                                         #Regner ut hva største matching er om vi ikke bruker 'node' til noe, 
        dp_out[node] += max(dp_in[child], dp_out[child])                            #og dermed ikke setter krav til om barna kan brukes                          

    for child, speed in company_tree[node]: 
        sum_without_child = dp_out[node] - max(dp_out[child],dp_in[child])          # Fjerner barnet som den parres med

        dp_in[node] = max(dp_in[node],                                              # Det som allerede er der
                          sum_without_child + dp_out[child] + 1)                    # Hvis du parrer denne noden med dette barnet 

dfs(ceo)

# maksimal kardinal matching med hastighet
def find_max_speed(node): 

    best_sum_with = -10000

    for child, speed in company_tree[node]: 
        find_max_speed(child)                                                           #Går gjennom alle barna til noden   

    for child, speed in company_tree[node]:
        if dp_out[child] > dp_in[child]:            #hvis barnet ikke er med i paret                                        
            dp_out_max[node] += dp_out_max[child]   #Legger til det der barnet ikke er med 

        elif dp_out[child] < dp_in[child]:          #hvis barnet er med i paret
            dp_out_max[node] += dp_in_max[child]    #Legger til det der barnet er med

        else: 
            dp_out_max[node] += max(dp_out_max[child], dp_in_max[child])    #Hvis de er like, så legger vi til det som er størst
    
    for child, speed, in company_tree[node]:
        if dp_out[child] + 1 - max(dp_in[child], dp_out[child]) >= 0:                               #hvis det er en gyldig matching 
            best_sum_with = max(best_sum_with, speed -                                              #Finner den beste hastigheten
                                max(dp_in_max[child], dp_out_max[child]) + dp_out_max[child])       

    dp_in_max[node] = dp_out_max[node] + best_sum_with


find_max_speed(ceo)


#dp_in[ceo] = antall par som kan dannes om ceo-en er med 
#dp_out[ceo] = antall par som kan dannes om ceo-en ikke er med

if dp_out[ceo] < dp_in[ceo]:       
    num_pair = dp_in[ceo]
    speed = dp_in_max[ceo]

elif dp_out[ceo] > dp_in[ceo]: 
    num_pair = dp_out[ceo]
    speed = dp_out_max[ceo]

else: 
    num_pair = dp_in[ceo]
    speed = max(dp_in_max[ceo], dp_out_max[ceo])

print(num_pair, speed/num_pair)