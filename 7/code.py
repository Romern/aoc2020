import sys
import json

# import input data
data = open(sys.argv[1]).read().split("\n")
if data[-1] == "":
	data = data[:-1]

bags = dict()
for l in data:
	bag_from, bags_to = l.replace(".","").replace("bags","bag").split(" contain ")
	bags_to = [(b.split(" ")[0], b[len(b.split(" ")[0])+1:]) for b in bags_to.split(", ")]
	if bags_to[0][0] != "no":
		bags[bag_from] = bags_to
	else:
		bags[bag_from] = []
	#print(bag_from, bags_to)

def amount_can_contain(target, can_contain_this_color):
	amount = 0
	for bag in bags[target]:
		if bag[1] == can_contain_this_color:
			amount += int(bag[0])
		else:
			amount += amount_can_contain(bag[1], can_contain_this_color)
	return amount

def part1():
	result = 0
	for b in bags:
		if amount_can_contain(b,"shiny gold bag")>0:
#			print(f"{b} can contain it.")
			result += 1
	print(result)

print("Part 1 results:")
part1()

def amount_must_contain(target_color):
	amount = 1
	for bag in bags[target_color]:
		amount += int(bag[0])*amount_must_contain(bag[1])
	return amount

def part2():
	print(amount_must_contain("shiny gold bag")-1) # without the bag itself

print("Part 2 results:")
part2()
