
def isLowPoint(data, x, y):
    val = data[y][x]
    works = True
    w = len(data)
    h = len(data[0])
    if y + 1 < h and val >= data[y+1][x]:
        works = False
    if y - 1 >= 0 and val >= data[y-1][x]:
        works = False
    if x + 1 < w and val >= data[y][x+1]:
        works = False
    if x - 1 >= 0 and val >= data[y][x-1]:
        works = False
    return works

lines = open("Day9\\Day9.txt", "r").readlines()

data = [[int(n) for n in row[:-1]] for row in lines]

total = 0
for y in range(len(data)):
    for x in range(len(data[0])):
        if isLowPoint(data, x, y):
            total += data[y][x] + 1
print(total)