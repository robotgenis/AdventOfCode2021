
def isLowPoint(data, x, y):
    val = data[y][x]
    works = True
    h = len(data)
    w = len(data[0])
    if y + 1 < h and val >= data[y+1][x]:
        works = False
    if y - 1 >= 0 and val >= data[y-1][x]:
        works = False
    if x + 1 < w and val >= data[y][x+1]:
        works = False
    if x - 1 >= 0 and val >= data[y][x-1]:
        works = False
    return works

def spreadStopAtNine(data, x, y, used):
    w = len(data[0])
    h = len(data)
    points = []
    if y + 1 < h and 9 > data[y+1][x]:
        p = (x, y+1)
        if not(p in used):
            points.append(p)
    if y - 1 >= 0 and 9 > data[y-1][x]:
        p = (x, y-1)
        if not(p in used):
            points.append(p)
    if x + 1 < w and 9 > data[y][x+1]:
        p = (x+1, y)
        if not(p in used):
            points.append(p)
    if x - 1 >= 0 and 9 > data[y][x-1]:
        p = (x-1, y)
        if not(p in used):
            points.append(p)
    return points

lines = open("Day9\\Day9.txt", "r").readlines()

data = [[int(n) for n in row[:-1]] for row in lines]

basinBottoms = []
for y in range(len(data)):
    for x in range(len(data[0])):
        # print(x, y)
        if isLowPoint(data, x, y):
            basinBottoms.append((x, y))


sizes = []
for i in basinBottoms:
    points = [i]
    used = [i]
    s = 1
    while len(points) > 0:
        newPoints = []
        for i in points:
            add = spreadStopAtNine(data, i[0], i[1], used)
            s += len(add)
            used.extend(add)
            newPoints.extend(add)
        points = newPoints
    sizes.append(s)
sizes.sort()
print(sizes)

print(sizes[-1]*sizes[-2]*sizes[-3])