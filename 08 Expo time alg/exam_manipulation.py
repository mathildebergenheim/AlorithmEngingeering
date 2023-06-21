n, q = (int(i) for i in input().split())

min_max_error = q           # The maximum number of errors is q

questions = [input().replace('T', '1').replace('F', '0') for _ in range(n)]                 # Convert to binary string

for ans in range(2**q):                 # 2^q is the number of possible answers
    max_error = 0
    for question in questions:
        error = ans ^ int(question, 2)                      # se onenote for forklaring
        max_error = max(max_error, bin(error).count('1'))   # se onenote for forklaring

    min_max_error = min(min_max_error, max_error)

print(q - min_max_error)        # The minimum number of correct answers is q - max_error

