def mark_draw(board,draw):
	for i, item in enumerate(board):
	   if draw == item:
	       board[i] = "*{}*".format(board[i])
	return board

def print_board(board):
	rtn = ""
	for i, item in enumerate(board,start = 1):
		rtn += item.rjust(6)
		if i%5 == 0:
			rtn += "\n"
	return rtn

def bingo(board):
	if "*" in board[0] and "*" in board[1] and "*" in board[2]and "*" in board[3] and "*" in board[4]:
		return True
	if "*" in board[5] and "*" in board[6] and "*" in board[7]and "*" in board[8] and "*" in board[9]:
		return True
	if "*" in board[10] and "*" in board[11] and "*" in board[12]and "*" in board[13] and "*" in board[14]:
		return True
	if "*" in board[15] and "*" in board[16] and "*" in board[17]and "*" in board[18] and "*" in board[19]:
		return True
	if "*" in board[20] and "*" in board[21] and "*" in board[22]and "*" in board[23] and "*" in board[24]:
		return True

	if "*" in board[0] and "*" in board[5] and "*" in board[10]and "*" in board[15] and "*" in board[20]:
		return True
	if "*" in board[1] and "*" in board[6] and "*" in board[11]and "*" in board[16] and "*" in board[21]:
		return True
	if "*" in board[2] and "*" in board[7] and "*" in board[12]and "*" in board[17] and "*" in board[22]:
		return True
	if "*" in board[3] and "*" in board[8] and "*" in board[13]and "*" in board[18] and "*" in board[23]:
		return True
	if "*" in board[4] and "*" in board[9] and "*" in board[14]and "*" in board[19] and "*" in board[24]:
		return True
	return False


def calulate_score(board):
	rtn = 0
	for item in board:
		if not "*" in item:
			rtn+= int(item)
	return rtn

bingo_boards = []

input_file = open('input.txt', 'r')
Lines = input_file.readlines()
index = 0
board_row = 0
board_index = 0

temp_board = []
for line in Lines:
	if index == 0:
		draws = line.strip().split(',')
	else:
		row_list = line.strip().replace('  ',' ').split(' ')

		if len(row_list)==5:
			board_row+=1
			temp_board += row_list
		if board_row == 5:
			board_row=0
			board_index+=1
			bingo_boards.append((temp_board))
			temp_board = []
	index +=1


bingo_check = False
for draw in draws:

	for j, board in enumerate(bingo_boards):
	    bingo_boards[j] = mark_draw(board,draw)
	    if bingo(bingo_boards[j]):
	    	print(print_board(bingo_boards[j]))
	    	bingo_check = True
	    	board_sum = calulate_score(bingo_boards[j])
	    	print("Board Sum: {}".format(board_sum))
	    	print("Won on: {}".format(draw))
	    	print("Score: {}".format(board_sum*int(draw)))

	    # print(bingo(bingo_boards[j]))
	if bingo_check:
		break
