import sys
data = open(sys.argv[1]).read().split("\n")
if data[-1] == "":
	data = data[:-1]

def parse(d):
	min_p, max_p = d.split(": ")[0].split(" ")[0].split("-")
	symbol = d.split(": ")[0].split(" ")[1]
	pw = d.split(": ")[1]
	return min_p, max_p, symbol, pw

def is_valid_old(d):
	min_p, max_p, symbol, pw = parse(d)
	amount = len([p for p in pw if p == symbol])
	if not (amount >= int(min_p) and amount <= int(max_p)):
		return False
	return True

def part1():
	res = 0
	for d in data:
		if is_valid_old(d):
			res += 1
	print(f"{res} passwords are valid!")

print("Part 1 result:")
part1()

def is_valid_new(d):
	first_p, second_p, symbol, pw = parse(d)
	print(parse(d))
	first = 1 if (pw[int(first_p)-1] == symbol) else 0
	second = 1 if (pw[int(second_p)-1] == symbol) else 0
	return (first + second) == 1

def part2():
	res = 0
	for d in data:
		if is_valid_new(d):
			res += 1
	print(f"{res} passwords are valid!")

print("Part 2 result:")
part2()
