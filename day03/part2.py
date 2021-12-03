input_file = open('input.txt', 'r')
Lines = input_file.readlines()

def split(word):
    return [char for char in word]

def get_common(list, column):
	line_count= len(list)
	half_count = line_count/2
	bit_counts = 0

	for line in list:
		report = split(line.strip())
		bit_counts += int(report[column])

	if bit_counts >= half_count:
		return 1
	else:
		return 0

def filter_list(list,column,filter):
	filtered_list = []
	for line in list:
		report = split(line.strip())
		value  = int(report[column])
		if value == filter:
			filtered_list.append(line.strip())
	return filtered_list


columns = len(Lines[0].strip())

oxygen_list = Lines
co2_list = Lines
for i in range(columns):
	if len(oxygen_list) > 1:
		common = get_common(oxygen_list,i)
		oxygen_list = filter_list(oxygen_list,i,common)


	#CO2 scrubber rating
	if len(co2_list) > 1:
		common = get_common(co2_list,i)
		if common:
			common = 0
		else:
			common = 1
		co2_list = filter_list(co2_list,i,common)

int(oxygen_list[0],2)
print("Oxygen generator rating:{}({})".format(oxygen_list[0],int(oxygen_list[0],2)))	
print("CO2 scrubber rating:{}({})".format(co2_list[0],int(co2_list[0],2)))
print("life support rating:{}".format(int(oxygen_list[0],2)*int(co2_list[0],2)))		