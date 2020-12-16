import sys
data = open(sys.argv[1]).read().rstrip("\n").split(",")

def run_puzzle(run_until):
	seen = dict()

	for i,d in enumerate(data):
		seen[int(d)] = {"times_seen": 1, "last_time": i, "before_that": None}

	cur_res = int(d)
	i = len(data)
	while i<run_until:
		if seen[cur_res]["times_seen"] <= 1:
			cur_res = 0
			seen[cur_res]["times_seen"] += 1
			seen[cur_res]["before_that"] = seen[cur_res]["last_time"]
			seen[cur_res]["last_time"] = i
		else:
			cur_res = seen[cur_res]["last_time"] - seen[cur_res]["before_that"]
			if cur_res not in seen:
				seen[cur_res] = {"times_seen": 1, "last_time": i, "before_that": None}
			else:
				seen[cur_res]["times_seen"] += 1
				seen[cur_res]["before_that"] = seen[cur_res]["last_time"]
				seen[cur_res]["last_time"] = i

		i += 1
	return cur_res
print("Part 1 results:")
print(run_puzzle(2020))

print("Part 2 results:")
print(run_puzzle(30000000))

