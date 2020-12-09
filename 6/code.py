import sys
inputset = sys.argv[1]

# data processing

groups = open(inputset).read()
while groups[-1] == "\n":
    groups = groups[:-1]
groups = groups.split("\n\n")


def part1():
	all = 0
	for g in groups:
	    all += len({d for d in g if d != "\n"})
	print(all)
print("Part 1 result:")
part1()

def part2():
	all = 0
	buchstaben = "abcdefghijklmnopqrstuvwxyz"
	for g in groups:
		data = g.split("\n")
		for b in buchstaben:
			temp = len({i for i,d in enumerate(data) if b in d})
			if temp == len(data):
				all += 1
	print(all)
print("Part 2 result:")
part2()
