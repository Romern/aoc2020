import sys
from tqdm import tqdm
import math

data = open(sys.argv[1]).read().split("\n")
if data[-1] == "":
	del data[-1]

def print_timetable(data,ts,amount=10):
	print("time\t","\t".join([f"bus {i}" for i in data]))
	for t in range(ts,ts+amount):
		print(f"{t}\t", "\t".join([("D" if ((t % d) == 0) else ".") if d != "x" else "x" for d in data]))

def part1(earliest_ts, data):
	shuttle_ids = [(d,earliest_ts % int(d) ) for d in data if d != "x"]
	res =  max(shuttle_ids,key=lambda item:item[1])
	return res[0] * (res[0] - res[1]), res

shuttle_data = [int(d) if d != "x" else "x" for d in data[1].split(",")]
print("Part 1 results:")
print(part1(int(data[0]), shuttle_data))

def part2_inefficient(data):
	table = []
	t = 0
	data_no_x = [d for d in data if d != "x"]
	precalc_inc = 1
	while True:
		if all(((t+i) % d) == 0 for i,d in enumerate(data) if d != "x"):
			return t
		t += precalc_inc
	return False

def part2(data):
	start = 0
	step = data[0]
	for i, d in enumerate(data):
		if i==0 or d == "x":
			continue
		x = 0
		while (start + step * x + i) % d != 0:
			 x += 1

		start += x * step
		step *= d
	return start

print("Part 2 results:")
print(part2(shuttle_data))
print_timetable([d for d in shuttle_data if d != "x"], part2(shuttle_data))
