import sys
data = open(sys.argv[1]).read().rstrip("\n").split("\n")

# parse data into a dict for easier coordinates for now
new_data = dict()
new_data[0] = dict()
for i in range(len(data)):
	new_data[0][i] = dict()
	for j in range(len(data[i])):
		new_data[0][i][j] = data[i][j]
data = new_data

def active_neighbors(i,j,k,data):
	res = 0
	for i1 in [i,i+1,i-1]:
		for j1 in [j,j+1,j-1]:
			for k1 in [k,k+1,k-1]:
				if i1 not in data or j1 not in data[i1] or k1 not in data[i1][j1]:
					continue
				res += 1 if data[i1][j1][k1] == "#" and not (i1==i and j1==j and k1==k) else 0
	return res


def part1(cycles=3):
	ilen = len(data.keys())
	jlen = len(data[0].keys())
	klen = len(data[0][0].keys())
	for c in range(cycles):
		ilen += 1
		jlen += 1
		klen += 1
		# copy prev data
		prev_data = dict()
		for i in range(-ilen-1,ilen+1):
			if i not in data:
				data[i] = dict()
			prev_data[i] = dict()
			for j in range(-jlen-1,jlen+1):
				if j not in data[i]:
					data[i][j] = dict()
				prev_data[i][j] = dict()
				for k in range(-klen-1,klen+1):
					if k not in data[i][j]:
						data[i][j][k] = "."
					prev_data[i][j][k] = data[i][j][k]
		# do run
		for i in data.keys():
			for j in data[i].keys():
				for k in data[i][j].keys():
					act = active_neighbors(i,j,k,prev_data)
					if prev_data[i][j][k] == "#":
						if act == 2 or act == 3:
							data[i][j][k] = "#"
						else:
							data[i][j][k] = "."
					elif prev_data[i][j][k] == "." and act == 3:
						data[i][j][k] = "#"
					else:
						data[i][j][k] = "."
#		print("ääääääääääääääääääääääääääääää")
#		print(f"Cycle #{c}:")
#		print_data(data)
	return len([True for i in data for j in data[i] for k in data[i][j] if data[i][j][k] == "#"])

def print_data(data):
	for i in sorted(list(data.keys())):
		print("\nz =",i)
		for j in sorted(list(data[i].keys())):
			print()
			for k in sorted(list(data[i][j].keys())):
				print(data[i][j][k],end="")
	print()
print("Part 1 results:")
#print_data(data)
print(part1(cycles=6))
