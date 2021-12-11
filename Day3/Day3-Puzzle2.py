

lines = open("Day3\\Day3.txt", "r").readlines()


lines1 = [i[:-1] for i in lines]

lines2 = [i[:-1] for i in lines]



for x in range(len(lines1[0])):
    if(len(lines1) == 1):
        break
    
    count0 = 0
    count1 = 0
    for row in lines1:
        if row[x] == "1":
            count1 += 1
        else:
            count0 += 1
    
    remove = "1"
    if count1 >= count0:
        #remove 0
        remove = "0"
        
    i = 0
    while i < len(lines1):
        if lines1[i][x] == remove:
            lines1.pop(i)
        else:
            i += 1


for x in range(len(lines2[0])):
    if(len(lines2) == 1):
        break
    
    count0 = 0
    count1 = 0
    for row in lines2:
        if row[x] == "1":
            count1 += 1
        else:
            count0 += 1
    
    remove = "0"
    if count1 >= count0:
        #remove 0
        remove = "1"
        
    i = 0
    while i < len(lines2):
        if lines2[i][x] == remove:
            lines2.pop(i)
        else:
            i += 1


print(int(lines1[0],2)*int(lines2[0],2))