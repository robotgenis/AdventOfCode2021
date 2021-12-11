
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
    sx = i[0][0]
    sy = i[0][1]
    ex = i[1][0]
    ey = i[1][1]
    
    deltaX = ex - sx
    if deltaX == 0:
        dirX = 0
    else:
        dirX = deltaX // abs(deltaX)
    
    deltaY= ey - sy
    if deltaY == 0:
        dirY = 0
    else:
        dirY = deltaY // abs(deltaY)
    
    for a in range(0, max(abs(deltaX), abs(deltaY)) + 1, 1):
        dx = a * dirX
        dy = a * dirY
        grid[sy + dy][sx + dx] += 1
    



total = 0
for x in range(maxX):
    for y in range(maxY):
        if grid[y][x] >= 2:
            total += 1

print(total)