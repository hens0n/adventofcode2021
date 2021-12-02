file1 = open('input', 'r')
Lines = file1.readlines()

previous_line=0
current_line=0
increased=0
decreased=0

for line in Lines:
	current_line=int(line.strip())
	if previous_line and current_line:
		if previous_line > current_line:
			decreased += 1
			print("{} (decreased)".format(line.strip()))
		if previous_line < current_line:
			increased += 1
			print("{} (increased)".format(line.strip()))		
	else:
		if len(line.strip())>0:
			print("{} (N/A - no previous measurement)".format(line.strip()))	

	previous_line=int(line.strip())

print("increased:{}, decreased:{} ".format(increased,decreased))	