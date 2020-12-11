import sys
data = open(sys.argv[1]).read().split("\n")
if data[-1] == "":
	del data[-1]
for i in range(len(data)):
	data[i] = list(data[i])

def seats_adj(i,j, data):
	return ((data[i-1][j] == "#") if (i > 0) else 0) \
	     + ((data[i-1][j-1]== "#") if (i > 0) and (j > 0) else 0) \
	     + ((data[i-1][j+1] == "#") if (i > 0) and (j < (len(data[i])-1)) else 0) \
	     + ((data[i+1][j+1] == "#") if (i < (len(data)-1)) and (j < (len(data[i])-1)) else 0) \
	     + ((data[i][j-1] == "#") if (j > 0) else 0) \
	     + ((data[i+1][j-1] == "#") if (j > 0) and (i < (len(data)-1)) else 0) \
	     + ((data[i+1][j] == "#") if (i < (len(data)-1)) else 0) \
	     + ((data[i][j+1]== "#") if (j < (len(data[i])-1)) else 0)

def occ_seats(data):
	tot = 0
	for i in range(len(data)):
		for j in range(len(data[i])):
			if data[i][j] == "#":
				tot += 1
	return tot

def one_round(data, measurement, seats_needed_for_leaving):
	new_data = []
	changed = False
	for i in range(len(data)):
		new_data.append(data[i].copy())
		for j in range(len(data[i])):
			adj_seats = measurement(i,j, data)
			if data[i][j] == "L" and adj_seats == 0:
				new_data[i][j] = "#"
				changed = True
			elif data[i][j] == "#" and adj_seats >= seats_needed_for_leaving:
				new_data[i][j] = "L"
				changed = True
	return new_data, changed

def run_until_equilibrium(data, measurement, seats_needed_for_leaving):
	changed = True
	i = 0
	while True:
		i += 1
		data, changed = one_round(data, measurement, seats_needed_for_leaving)
		if not changed:
			print(f"Round {i}: Nothing changed! Abort!")
			print(f"Amount of occupied seats: {occ_seats(data)}.")
			return data

print("Part 1 Results:")
run_until_equilibrium(data, seats_adj, 4)

def seats_in_sight(i,j,data):
	tot = 0
	it = 1
	while i+it < len(data):
		if data[i+it][j] == "#":
			tot += 1
			break
		elif data[i+it][j] == "L":
			break
		it += 1
	it = 1
	while j+it < len(data[i]):
		if data[i][j+it] == "#":
			tot += 1
			break
		elif data[i][j+it] == "L":
			break
		it += 1
	it = 1
	while i+it < len(data) and j+it < len(data[i]):
		if data[i+it][j+it] == "#":
			tot += 1
			break
		elif data[i+it][j+it] == "L":
			break
		it += 1
	it = 1
	while i-it >= 0 and j-it >= 0:
		if data[i-it][j-it] == "#":
			tot += 1
			break
		elif data[i-it][j-it] == "L":
			break
		it += 1
	it = 1
	while i-it >= 0:
		if data[i-it][j] == "#":
			tot += 1
			break
		elif data[i-it][j] == "L":
			break
		it += 1
	it = 1
	while j-it >= 0:
		if data[i][j-it] == "#":
			tot += 1
			break
		elif data[i][j-it] == "L":
			break
		it += 1
	it = 1
	while i-it >= 0 and j+it < len(data[i]):
		if data[i-it][j+it] == "#":
			tot += 1
			break
		elif data[i-it][j+it] == "L":
			break
		it += 1
	it = 1
	while i+it < len(data) and j-it >= 0:
		if data[i+it][j-it] == "#":
			tot += 1
			break
		elif data[i+it][j-it] == "L":
			break
		it += 1
	return tot

print("Part 2 results:")
run_until_equilibrium(data, seats_in_sight, 5)
