import sys
data = open(sys.argv[1]).read().split("\n")
if data[-1] == "":
	data = data[:-1]

def part1(right=3, down=1):
	pos_x = 0
	pos_y = 0
	res = 0
	if data[pos_y][pos_x % len(data[pos_y])] == "#":
		res += 1
	while pos_y != len(data)-1:
		pos_x += right
		pos_y += down
		if data[pos_y][pos_x % len(data[pos_y])] == "#":
			res += 1
	print(f"Encountered {res} trees.")
	return res
print("Part 1 result:")
part1()

def part2():
	try_slopes = [(1,1),(3,1),(5,1),(7,1),(1,2)]
	res = 1
	for x,y in try_slopes:
		res *= part1(x,y)
	print(f"Multiplied this results in {res}")

print("Part 2 result:")
part2()
