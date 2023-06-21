all_rotated = []

while True:
    n = int(input().strip('\n'))
    if n == 0: 
        break

    rows = n
    cols = 0

    asciifig = []

    for i in range(rows): 
        line = input().strip('\n')

        asciifig.append(line)
        cols = max(cols, len(line))

    rotated = ([[' ' for i in range(rows)] for i in range(cols)])

    for i in range(rows-1, -1, -1):
        for j in range(len(asciifig[rows-1-i])):
            if asciifig[rows-1-i][j] == '|':
                rotated[j][i] = '-'
            elif asciifig[rows-1-i][j] == '-':
                rotated[j][i] = '|'
            else:
                rotated[j][i] = asciifig[rows-1-i][j]

    all_rotated += rotated + [""]


if len(all_rotated) != 0: 
    for line in all_rotated[:-1]: 
        print(''.join(line).rstrip())
