import sys

# read input

data = open(sys.argv[1]).read().split("\n")
if data[-1] == "":
	data = data[:-1]
for i in range(len(data)):
	data[i] = int(data[i])

preemble_length = int(sys.argv[2])

def gen_allowed_numbers(input):
	output = []
	for counter, i in enumerate(input):
		for j in input[counter:]:
			output.append(i+j)
	return output

def part1(data):
	allowed_numbers = gen_allowed_numbers(data)
	for counter, i in enumerate(data[preemble_length:]):
		allowed_numbers = gen_allowed_numbers(data[counter:counter+preemble_length])
		if i not in allowed_numbers:
			print(f"Error, {i} is not allowed!") #Current allowed_number: {allowed_numbers}")
			return False
print("Part 1 results:")
part1(data)

def find_contiguos_set(data, number):
	# Find data[i:j] such that sum(data[i:j]) == number
	for i in range(len(data)):
		for j in range(i,len(data)):
			#print(f"{i}:{j}={data[i:j]} summed={sum(data[i:j])}")
			if sum(data[i:j]) == number:
				return i, j
	print("Didn't find set!")
	return None, None

def part2(data):
	allowed_numbers = gen_allowed_numbers(data)
	for counter, i in enumerate(data[preemble_length:]):
		allowed_numbers = gen_allowed_numbers(data[counter:counter+preemble_length])
		if i not in allowed_numbers:
			print(f"Error, {i} is not allowed! Finding contiguos set...")
			res = find_contiguos_set(data, i)
			print(f"Found set, {res}={data[res[0]:res[1]]}, max={max(data[res[0]:res[1]])}, min={min(data[res[0]:res[1]])}, max+min={max(data[res[0]:res[1]])+min(data[res[0]:res[1]])}")
			return False
print("Part 2 results:")
part2(data)
