
lines = open("Day5\\Day5.txt", "r").readlines()


data = [[list(map(int,(a:=i.split(" -> "))[0].split(","))),list(map(int,a[1].split(",")))] for i in lines]


maxX = 0
maxY = 0

for i in data:
    if i[0][0] > maxX:
        maxX = i[0][0]
    if i[1][0] > maxX:
        maxX = i[1][0]
    if i[0][1] > maxY:
        maxY = i[0][1]
    if i[1][1] > maxY:
        maxY = i[1][1]

maxX += 1
maxY += 1

grid = [[0 for x in range(maxX)] for y in range(maxY)]



for i in data:
    if i[0][0] == i[1][0]:
        s = min(i[0][1], i[1][1])
        e = max(i[0][1], i[1][1])
        for y in range(s, e + 1, 1):
            grid[y][i[0][0]] += 1
    if i[0][1] == i[1][1]:
        s = min(i[0][0], i[1][0])
        e = max(i[0][0], i[1][0])
        for x in range(s, e + 1, 1):
            grid[i[0][1]][x] += 1


total = 0
for x in range(maxX):
    for y in range(maxY):
        if grid[y][x] >= 2:
            total += 1

print(total)