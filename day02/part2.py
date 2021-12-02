input_file = open('input.txt', 'r')
Lines = input_file.readlines()

horizontal = 0 
depth = 0
aim=0

for line in Lines:
	move=line.strip().split(" ")
	if move[0]=="up":
		aim-= int(move[1])
	if move[0]=="down":
		aim+= int(move[1])
	if move[0]=="forward":
		horizontal+= int(move[1])
		depth= depth + (aim * int(move[1]))

print("horizontal:{}, depth:{}, aim:{} ".format(horizontal,depth,aim))	
print("total:{}".format(horizontal*depth))	