
lines = open("Day2\\Day2.txt", "r").readlines()


data = [[(s:=i.split())[0],int(s[1])] for i in lines]

depth = 0
dis = 0
aim = 0

for i in data:
    if i[0] == "forward":
        dis += i[1]
        depth += aim * i[1]
    elif i[0] == "down":
        aim += i[1]
    elif i[0] == "up":
        aim -= i[1]

print(depth, dis)
print(depth * dis)