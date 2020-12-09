import sys
import math

# import input data
data = open(sys.argv[1]).read().split("\n")
if data[-1] == "":
	data = data[:-1]

def decode_pass(p):
	l_row = 0
	h_row = 127

	l_col = 0
	h_col = 7

	low_row = True
	low_col = True

	for l in p:
		if l == "F":
			h_row = h_row - math.ceil((h_row-l_row) / 2)
			low_row = False
		elif l == "B":
			l_row = l_row + math.ceil((h_row-l_row) / 2)
			low_row = True
		elif l == "L":
			h_col = h_col - math.ceil((h_col-l_col) / 2)
			low_col = False
		elif l == "R":
			l_col = l_col + math.ceil((h_col-l_col) / 2)
			low_col = True
	return (l_row if low_row else h_row), (l_col if low_col else h_col), \
		(l_row if low_row else h_row)*8+(l_col if low_col else h_col)

def part1():
	print(max([decode_pass(d)[2] for d in data]))
print("Part 1 results:")
part1()

def part2():
	passes = [decode_pass(d)[2] for d in data]
	passes.sort()
	for i in range(len(passes)-1):
		if passes[i]+2 == passes[i+1]:
			print(passes[i], passes[i+1])
print("Part 2 results:")
part2()
