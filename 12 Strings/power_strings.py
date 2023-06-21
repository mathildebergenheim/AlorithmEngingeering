from math import sqrt

def find_divisors(n):                   #Finner alle divisorer til n
    divisors = []                   
    for i in range(1, int(sqrt(n)+1)):
        if n % i == 0:
            divisors.append(i)
            divisors.append(n//i)

    divisors.sort()
    return divisors

def power_strings(s):
    divisors = find_divisors(len(s))                #Finner alle mulige lengdene til en substring/powerstring
    for divisor in divisors:                        #Går gjennom alle mulige lengder
        if s[-divisor:] * (len(s) // divisor) == s: #Sjekker om substringen er en powerstring, kortere å lage en substring bakfra enn forfra
            power = len(s) // divisor               #Hvis den er det, returnerer vi antall ganger substrengen går opp i s
            return power
     

s = input()
while s != ".":
    print(power_strings(s))
    s = input()
