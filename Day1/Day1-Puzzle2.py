


inc = list(map(int, open("Day1\\Day1.txt", "r").readlines()))

count = 0

for i in range(len(inc) - 3):
    if inc[i] < inc[i + 3]:
        count += 1
        

print(count)