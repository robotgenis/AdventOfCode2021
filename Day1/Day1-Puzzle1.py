


inc = list(map(int, open("Day1\\Day1.txt", "r").readlines()))

count = 0

for i in range(len(inc) - 1):
    if inc[i] < inc[i + 1]:
        count += 1
        

print(count)