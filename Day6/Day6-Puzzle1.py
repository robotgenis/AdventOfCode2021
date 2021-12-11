

fish = list(map(int,open("Day6\\Day6.txt", "r").readlines()[0].split(",")))

dic = {}

for i in range(9):
    dic[i] = 0

for i in fish:
    dic[i] += 1

for i in range(80):
    repro = dic[0]
    
    for i in range(8):
        dic[i] = dic[i + 1]
    
    dic[8] = repro
    dic[6] += repro


print(sum(dic.values()))
