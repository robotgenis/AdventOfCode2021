

lines = open("Day3\\Day3.txt", "r").readlines()


lines = [i[:-1] for i in lines]

dataSize = len(lines)


gamma = ""
epsilon = ""
for x in range(len(lines[0])):
    count1 = 0
    count0 = 0
    for row in lines:
        if row[x] == "1":
            count1 += 1
        else:
            count0 += 1
    
    if count1 > count0:
        gamma += "1"
        epsilon += "0"
    else:
        gamma += "0"
        epsilon += "1"


print(int(gamma,2)*int(epsilon,2))