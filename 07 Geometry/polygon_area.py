
def shoelace(poly): 
    N = len(poly)
    fw = sum(poly[i - 1][0] * poly[i][1] for i in range(N))
    poly = list(reversed(poly))
    bw = sum(poly[i - 1][0] * poly[i][1] for i in range(N))
    return abs(fw - bw) / 2.0


def cw_ccw(points):
    direction = 0
    for i in range(len(points)-1):
        cross_product = (points[i+1][0] - points[i][0]) * (points[i+1][1] + points[i][1])
        direction += cross_product
    if direction > 0:
        return "cw"
    elif direction < 0:
        return "ccw"

num_points = int(input())

while num_points != 0: 
    points = []
    for _ in range(num_points):
        points.append([int(el) for el in input().split()])
    points.append(points[0])

    area = shoelace(points)
    print(f'{cw_ccw(points)} {round(area, 1)}')
    
    num_points = int(input())

