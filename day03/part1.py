def split(word):
    return [char for char in word]

input_file = open('input.txt', 'r')
Lines = input_file.readlines()

array_length = len(Lines[0].strip())
line_count= len(Lines)
half_count = line_count/2
bit_counts = []
bit_counts = [0 for i in range(array_length)] 

for line in Lines:
	report = split(line.strip())
	for i in range(array_length):
		bit_counts[i] += int(report[i])
 
gamma = ""
for bit in bit_counts:
	# print(bit)
	if int(bit)> half_count:
		gamma+="1"
	else:
		gamma+="0"

gamma_int = int(gamma,2)

xor_string = ""
for i in range(array_length):
	xor_string += "1"
	
xor = int(xor_string,2)
epsilon_int = gamma_int^xor

print(int(gamma,2))
power = gamma_int*epsilon_int

print("gamma:{}, epsilon:{}, power consumption:{} ".format(gamma_int,epsilon_int,power))	