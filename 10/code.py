import sys
import time

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


# counts the amount of path from cur to target in a DAG (why isnt this in networkx?)
def count_paths_rec(cur, data, amount_of_paths):
	if cur in amount_of_paths:
		return amount_of_paths[cur]
	total = 0
	for i in range(cur+1,len(data)):
		if data[i] > data[cur] + 3:
			break
		total += count_paths_rec(i, data, amount_of_paths)
	amount_of_paths[cur] = total
	return total

def count_paths_lin(data):
	cache = [0] * data[-1] + [1]
	for i in range(len(data)-2,-1,-1):
		cache[data[i]] = cache[data[i]+1] + cache[data[i]+2] + cache[data[i]+3]
	return cache[0]

start_time = time.time()

data = [0] + data + [data[-1] + 3]

# linear
res = count_paths_lin(data)
# recursive
#res = count_paths_rec(0, data, {len(data)-1 : 1})

end_time = time.time()

print(f"Part 2 result: {res}. Total time: {end_time-start_time} seconds")
