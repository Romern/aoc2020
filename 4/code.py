import sys
import re
data = open(sys.argv[1]).read().split("\n\n")
for i in range(len(data)):
	data[i] = data[i].replace("\n", " ").split(" ")
	if data[i][-1] == "":
		print(data[i])
		data[i] = data[i][:-1]
	temp = dict()
	for d in data[i]:
		k,v = d.split(":")
		temp[k] = v
	data[i] = temp

required_keys = {"ecl","pid","eyr","hcl","byr","iyr","hgt"}
required_keys_plus = {"ecl","pid","eyr","hcl","byr","iyr","hgt", "cid"}

def check_if_contains_all_needed_fields(passport):
	if (set(passport.keys()) == required_keys) or (set(passport.keys()) == required_keys_plus):
		return True
	return False

def part1():
	res = 0
	for d in data:
		if check_if_contains_all_needed_fields(d):
			res += 1
	print(res)
print("Part 1 results:")
part1()

def check_if_valid(passport):
	if not (re.match("^[0-9]{4}$",passport["byr"]) and int(passport["byr"]) >= 1920 and int(passport["byr"]) <= 2002):
		return False
	if not (re.match("^[0-9]{4}$",passport["iyr"]) and int(passport["iyr"]) >= 2010 and int(passport["iyr"]) <= 2020):
		return False
	if not (re.match("^[0-9]{4}$",passport["eyr"]) and int(passport["eyr"]) >= 2020 and int(passport["eyr"]) <= 2030):
		return False
	if re.match("^[0-9]+(cm|in)$",passport["hgt"]):
		ein = passport["hgt"][-2:]
		hgt = int(passport["hgt"][:-2])
		if ein == "cm" and (hgt < 150 or hgt > 193):
			return False
		if ein == "in" and (hgt < 59 or hgt > 76):
			return False
	else:
		return False
	if not re.match("^#[0-9a-f]{6}$",passport["hcl"]):
		return False
	if not (passport["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]):
		return False
	if not re.match("^[0-9]{9}$",passport["pid"]):
		return False
	return True

def part2():
	res = 0
	for i, p in enumerate(data):
		if check_if_contains_all_needed_fields(p) and check_if_valid(p):
			res += 1
	print(res)
print("Part 2 results:")
part2()
