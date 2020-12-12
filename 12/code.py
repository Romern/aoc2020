import sys
import re

data = re.findall("([A-Z]{1})([0-9]+)",open(sys.argv[1]).read())

def doInstructions_part1(dir_rotation):
	x = 0
	y = 0
	for dir,amount in data:
		amount = int(amount)
		if dir == "N":
			y -= amount
		elif dir == "S":
			y += amount
		elif dir == "E":
			x += amount
		elif dir == "W":
			x -= amount
		elif dir == "L":
			dir_rotation = (dir_rotation - amount) % 360
		elif dir == "R":
			dir_rotation = (dir_rotation + amount) % 360
		elif dir == "F":
			if dir_rotation == 0:
				y -= amount
			elif dir_rotation == 90:
				x += amount
			elif dir_rotation == 180:
				y += amount
			elif dir_rotation == 270:
				x -= amount
	manhatten = abs(x) + abs(y)
	return x, y, manhatten

print("Part 1 results:")
print(doInstructions_part1(90))

def doInstructions_part2(wp_x,wp_y):
	x = 0
	y = 0
	for dir,amount in data:
		amount = int(amount)
		if dir == "N":
			wp_y += amount
		elif dir == "S":
			wp_y -= amount
		elif dir == "E":
			wp_x += amount
		elif dir == "W":
			wp_x -= amount
		elif dir == "L":
			for i in range(int(amount/90)):
				temp_wp_x, temp_wp_y = wp_x,wp_y
				wp_x = -temp_wp_y
				wp_y = temp_wp_x
		elif dir == "R":
			for i in range(int(amount/90)):
				temp_wp_x, temp_wp_y = wp_x,wp_y
				wp_x = temp_wp_y
				wp_y = -temp_wp_x
		elif dir == "F":
			x += wp_x * amount
			y += wp_y * amount
#		print(f"After {dir}{amount}:",x,y,wp_x,wp_y)
	manhatten = abs(x) + abs(y)
	return x, y, manhatten

print("Part 2 results:")
print(doInstructions_part2(10,1))
