# python3 -m pip install numpy
import numpy as np
file1 = open('part1_input.txt', 'r')
Lines = file1.readlines()

previous_window=0
current_window=0
increased=0
decreased=0

line_array = np.array(Lines)
for i in range(len(line_array)-2):
	current_window=int(line_array[i].strip())+int(line_array[i+1].strip())+int(line_array[i+2].strip())

	if previous_window and current_window:
		if previous_window > current_window:
			decreased += 1
			print("{} (decreased)".format(current_window))
		if previous_window < current_window:
			increased += 1
			print("{} (increased)".format(current_window))		
	else:
		if current_window>0:
			print("{} (N/A - no previous measurement)".format(current_window))	

	previous_window=current_window

print("increased:{}, decreased:{} ".format(increased,decreased))	