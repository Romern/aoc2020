import time

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

data = []
with open("input.txt","r") as file:
	for i in file:
		if i:
			data.append(int(i))
data_sorted = sorted(data)
data = [0] + data_sorted + [data_sorted[-1] + 3]

# linear
res = count_paths_lin(data)
# recursive
#res = count_paths_rec(0, data, {len(data)-1 : 1})

end_time = time.time()

print(f"Part 2 result: {res}. Total time: {end_time-start_time} seconds")
