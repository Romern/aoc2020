import sys
data = open(sys.argv[1]).read().split("\n")
if data[-1] == "":
	data = data[:-1]

for i in range(len(data)):
	data[i] = int(data[i])

def part1():
	for i in range(len(data)):
		for j in range(len(data)):
			if i == j:
				continue
			if data[i]+data[j] == 2020:
				return data[i]*data[j]
	return None
print("Part 1 result:")
print(f"{part1()}==2020")

def part2():
	for i in range(len(data)):
		for j in range(len(data)):
			for k in range(len(data)):
				if len({i,j,k}) != 3:
					continue
				if data[i]+data[j]+data[k] == 2020:
					return data[i]*data[j]*data[k]
	return None
print("Part 2 result:")
print(f"{part2()}==2020")
