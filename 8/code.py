import sys


# data processing
data = open(sys.argv[1]).read().split("\n")
if data[-1] == "":
	del data[-1]
instructions = []
for d in data:
	temp = d.split(" ")
	instructions.append({ "op": temp[0], "arg": temp[1] })

# code

def run_program(instructions):
	visited = dict()
	pos = 0
	acc = 0
	while pos < len(instructions):
		#print(f'{instructions[pos]["op"]} {instructions[pos]["arg"]}')
		if visited.get(pos,False):
			print(f"Instruction {pos} executed a second time. Accumulator: {acc}")
			return False
		visited[pos] = True
		if instructions[pos]["op"] == "acc":
			acc += int(instructions[pos]["arg"])
			pos += 1
		elif instructions[pos]["op"] == "jmp":
			pos += int(instructions[pos]["arg"])
		elif instructions[pos]["op"] == "nop":
			pos += 1
	print(f"Program quit normally. Accumulator: {acc}")
	return True

def part1():
	run_program(instructions)
print("Part 1 results:")
part1()

def part2():
	for i in range(len(instructions)):
		if instructions[i]["op"] == "jmp":
			temp = instructions.copy()
			temp_ins = dict(temp[i])
			temp_ins["op"] = "nop"
			temp[i] = temp_ins
			if run_program(temp):
				print(f"Found right instruction, instruction[{i}] = \"jmp\" --> \"nop\"!")
				exit()
		elif instructions[i]["op"] == "nop":
			temp = instructions.copy()
			temp_ins = dict(temp[i])
			temp_ins["op"] = "jmp"
			temp[i] = temp_ins
			if run_program(temp):
				print(f"Found right instruction, instruction[{i}] = \"nop\" --> \"jmp\"!")
				exit()
print("Part 2 results:")
part2()
