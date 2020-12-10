import time

# counts the amount of path from cur to target in a DAG (why isnt this in networkx?)
def count_paths(cur, data, amount_of_paths):
	if cur in amount_of_paths:
		return amount_of_paths[cur]
	total = 0
	for i in range(cur+1,len(data)):
		if data[i] > data[cur] + 3:
			break
		total += count_paths(i, data, amount_of_paths)
	amount_of_paths[cur] = total
	return total

start_time = time.time()

data = []
with open("input.txt","r") as file:
	for i in file:
		if i:
			data.append(int(i))
data_sorted = sorted(data)
data = [0] + data_sorted + [data[-1] + 3]
res = count_paths(0, data, {len(data)-1 : 1})

end_time = time.time()

print(f"Part 2 result: {res}. Total time: {end_time-start_time} seconds")
