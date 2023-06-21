A = 3
B = 10**9 + 7
Ainvers = pow(A, B-2, B)

# Operation A** er veldig tidkrevende, så vi lager en liste med alle potensene av A:
power_of_A = [1]
for i in range(1, 10**6):
    power_of_A.append(power_of_A[i-1] * A % B)

#brukes til å gjøre om alle ordene vi får inn til tall    
#Raskere å sjekke om to tall er like enn om to strings er like:
def phash(word):
    return sum(ord(e) * (power_of_A[(i)]) for i, e in enumerate(word)) % B

n = int(input())
words = []
hashes = []

for _ in range(n): 
    word = input()
    words.append(word)
    hashes.append(phash(word))

#Raskere å sjekke set enn liste:
hashes_set = set(hashes)
words_set = set(words)

no_typos = True


for hi, hashh in enumerate(hashes):

    """Lager en liste med alle prefikshashene til ordet vi er på nå"""
    prefix_hash = []

    for char in words[hi]:
        if prefix_hash == []:               #hvis det er første bokstav i ordet, legger vi bare til hashen av den bokstaven
            prefix_hash.append(ord(char))
        else:                               #hvis det ikke er første bokstav i ordet, legger vi til hashen av bokstaven + hashen av alle bokstavene før, som er det forrige elementet i listen
            prefix_hash.append((prefix_hash[-1] + ord(char) * power_of_A[len(prefix_hash)]) % B)

    for i in range(len(words[hi])):         #går gjennom alle bokstavene i ordet
        if i == 0:                          #hvis det er første bokstav, er hashen bare hashen av alle bokstavene etter
            substring_hash = (prefix_hash[-1] - prefix_hash[i]) * Ainvers % B
        else: 
                                            # hvis det ikke er første bokstav, er hashen hashen av alle bokstavene før + hashen av alle bokstavene etter, se onenote forklaring 
            substring_hash = prefix_hash[i-1]
            substring_hash += (prefix_hash[-1] - prefix_hash[i]) * Ainvers % B     #legger til hashen av alle bokstavene etter
       
        substring_hash %= B

        if substring_hash in hashes_set:                    #sjekker om hashen er i listen med hashes
            substring = words[hi][:i] + words[hi][i+1:]     #henter ut substringen
            if substring in words_set:                      #sjekker om substringen er i listen med ord
                print(words[hi])
                no_typos = False
                break



if no_typos:
    print("NO TYPOS")