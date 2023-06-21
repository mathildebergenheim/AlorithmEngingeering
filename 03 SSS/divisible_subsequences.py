
num_cases = int(input())

for case in range(num_cases):

    d, n = (int(i) for i in input().split(' '))     #d divisor, n length of sequence 
    seq = [int(i) for i in input().split(' ')]

    list = [0]*d        #Liste over antall (i mod d)
    summ = 0 

    for num in seq: 
        summ += num

        mod = summ%d
        list[mod] += 1
    
    num_div = 0

    for i in range(1, len(list)):
        n = list[i] - 1             #|_|_| for vite strekene, men vil ha linjene 
        num_div += n*(n+1)//2       # formel funnet på nettet vte å sette inn tallrekke 1 3 6 10 15, triangluar number sequence 
    
    n = list[0]     #summ%d = 0 gir special case        _|_|_| her er linjer og streker likt antall 

    num_div += n*(n+1)//2

    print(num_div) 