import sys
import json

# data processing
rules, your_ticket, nearby_tickets = open(sys.argv[1]).read().rstrip("\n").split("\n\n")
rules = rules.split("\n")
your_ticket = [int(i) for i in your_ticket.split("\n")[1].split(",")]
nearby_tickets = nearby_tickets.split("\n")[1:]

for r in range(len(rules)):
	name, rest = rules[r].split(": ")
	lengths = rest.split(" or ")
	for l in range(len(lengths)):
		from_, to_ = lengths[l].split("-")
		lengths[l] = (int(from_),int(to_))
	rules[r] = {"name": name, "lengths": lengths}

for n in range(len(nearby_tickets)):
	fields = nearby_tickets[n].split(",")
	for f in range(len(fields)):
		fields[f] = int(fields[f])
	nearby_tickets[n] = fields

def part1():
	# Not valid for any field
	invalid_tickets = []
	ticket_scanning_error_rate = 0
	for i,n in enumerate(nearby_tickets):
		for field in n:
			any_valid = next((True for r in rules for f in r["lengths"] if f[0] <= field and f[1] >= field),False)
			if not any_valid:
				invalid_field = field
				break
		if not any_valid:
#			print(f"Ticket {n}: Is invalid: {invalid_field}")
			invalid_tickets.append(i)
			ticket_scanning_error_rate += invalid_field
	return invalid_tickets, ticket_scanning_error_rate
print("Part 1 results:")
invalid_tickets, ticket_scanning_error_rate = part1()
print(ticket_scanning_error_rate)


#discard those tickets entirely
for i in reversed(invalid_tickets):
	del nearby_tickets[i]

def part2():
	valid_fields = dict()
	for i in range(len(nearby_tickets[0])):
		valid_fields[i] = dict()
	# get number of possible fields
	for i, n in enumerate(nearby_tickets):
		for j, field in enumerate(n):
			for valid_field in [r["name"] for r in rules for f in r["lengths"] if f[0] <= field and f[1] >= field]:
				if valid_field not in valid_fields[j]:
					valid_fields[j][valid_field] = 0
				valid_fields[j][valid_field] += 1
	# filter not possible fields
	for k in valid_fields:
		for f in list(valid_fields[k].keys()):
			if valid_fields[k][f] != len(nearby_tickets):
				del valid_fields[k][f]
	# filter the fields with 1 possibility in the others
	one_pos_fields = [i for i in valid_fields if len(valid_fields[i])==1]
	while len(one_pos_fields)<len(valid_fields):
		for k in valid_fields:
			delete_names = [field for f in one_pos_fields for field in valid_fields[f]  if f != k and field in valid_fields[k]]
			for name in delete_names:
				del valid_fields[k][name]
		one_pos_fields = [i for i in valid_fields if len(valid_fields[i])==1]
	for k in valid_fields:
		valid_fields[k] = list(valid_fields[k].keys())[0]
	# calculate result
	res = 1
	amount = 0
	for i in valid_fields:
		if "departure" in valid_fields[i]:
			res *= int(your_ticket[i])
			amount += 1
	return valid_fields, res, amount

print("Part 2 results:")
print(json.dumps(part2(),indent=4))
