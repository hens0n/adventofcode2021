
input_file = open('input.txt', 'r')
Lines = input_file.readlines()

def generate_2d(h, w):
    return [[0 for x in range(w)] for y in range(h)]

grid = generate_2d(1000, 1000)

for line in Lines:
	# print(line.strip())
	xyxy = line.strip().split(' -> ')
	min = 0
	max = 0
	x1,y1= (int(i) for i in xyxy[0].split(','))
	x2,y2= (int(i) for i in xyxy[1].split(','))
	if x1==x2 :
		if y1 < y2:
			min=y1
			max=y2
		else:
			min=y2
			max=y1
		for y in range(min,max+1):
			grid[y][x1] += 1

	elif y1==y2:
		if x1 < x2:
			min=x1
			max=x2
		else:
			min=x2
			max=x1
		for x in range(min,max+1):
			grid[y1][x] += 1
	else:
		grid[y1][x1] += 1
		diagonalx = 1
		diagonaly = 1
		if x1 > x2:
			diagonaly = -1
		if y1 > y2:
			diagonalyy = -1
		
		while (x1, y1) != (x2, y2):
			x1 += diagonalx
			y1 += diagonaly
			grid[y1][x1] += 1
		
avoid = 0
for y in grid:
	# print(y)
	for x in y:
		if x > 1:
			avoid+=1
print(avoid)