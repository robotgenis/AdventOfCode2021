import math



data = list(map(int,open("Day7\\Day7.txt", "r").readlines()[0].split(",")))

minimum = 0
maximum = 0

for i in data:
    if i < minimum:
        minimum = i
    if i > maximum:
        maximum = i

print(minimum, maximum)

fact = [0]

for i in range(1, maximum-minimum+1):
    fact.append(fact[-1] +  i)

fact[0] = 0

print(fact)


bestResult = 10000000000000
for i in range(minimum, maximum+1):
	total = sum([fact[abs(i-k)] for k in data])
	if total < bestResult:
		bestResult = total

print(bestResult)
