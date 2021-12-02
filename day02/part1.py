input_file = open('input.txt', 'r')
Lines = input_file.readlines()

horizontal = 0 
depth = 0

for line in Lines:
	move=line.strip().split(" ")
	if move[0]=="up":
		depth-= int(move[1])
	if move[0]=="down":
		depth+= int(move[1])
	if move[0]=="forward":
		horizontal+= int(move[1])

print("horizontal:{}, depth:{} ".format(horizontal,depth))	
print("total:{}".format(horizontal*depth))	