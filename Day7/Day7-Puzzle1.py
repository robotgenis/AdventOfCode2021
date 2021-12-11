

data = list(map(int,open("Day7\\Day7.txt", "r").readlines()[0].split(",")))

minimum = 0
maximum = 0

for i in data:
    if i < minimum:
        minimum = i
    if i > maximum:
        maximum = i

print(minimum, maximum)

bestResult = 1000000000
for i in range(minimum, maximum+1):
	total = sum([abs(i-k) for k in data])
	if total < bestResult:
		bestResult = total

print(bestResult)
