import sys
data = open(sys.argv[1]).read().split("\n")
if data[-1] == "":
	data = data[:-1]

for i in range(len(data)):
	data[i] = int(data[i])
data.sort()

def part1():
	rated_joltage = max(data) + 3
	last = 0
	cur = None
	diff = 0
	one_jolt = 0
	three_jolt = 0
	while last + 3 != rated_joltage:
		cur = [v for v in data if v > last and v <= last + 3][0]
		diff = (cur - last)
		if diff == 1:
			one_jolt += 1
		elif diff == 3:
			three_jolt += 1
		last = cur
	three_jolt += 1
	print(one_jolt, "*", three_jolt, "=", (one_jolt*three_jolt))

print("Part 1 results:")
part1()


total_arrangements = 0

amount_of_paths = dict()

# graph is a DAG, topological sort is given, count the paths backwards
def part2():
	global data
	import networkx as nx
	data = [0] + data + [max(data) + 3]
	G = nx.DiGraph()
	G.add_edges_from([(i,j) for c,i in enumerate(data[:-1]) for j in data[c+1:] if j <= i + 3 and j > i])
	amount_of_paths[data[-1]] = 1
	print(count_paths(G, data[0], data[-1]))

# counts the amount of path from cur to target in a DAG (why isnt this in networkx?)
def count_paths(G, cur, target):
	if cur in amount_of_paths:
		return amount_of_paths[cur]
	total = 0
	for i in G.successors(cur):
		total += count_paths(G, i, target)
	amount_of_paths[cur] = total
	return total

part2()
"""
def part2():
	global data
	import networkx as nx
	data = [0] + data + [max(data) + 3]
	G = nx.DiGraph()
	G.add_edges_from([(i,j) for c,i in enumerate(data[:-1]) for j in data[c+1:] if j <= i + 3 and j > i])
	total = 0
	for path in nx.all_simple_paths(G, source=data[0], target=data[-1]):
		total += 1
	print(total)
# build graph where each node has a neighbor if it in range 0,+3
# get all pathes starting in node 0
# ultra inefficient
part2()
"""
