import random

def display_board(marks):
	"""
	:param marks: list of marks, first item should be '#'
	:return: prints board with marks after cleaning the console
	"""
	print(f' {marks[7]} | {marks[8]} | {marks[9]}\n {marks[4]} | {marks[5]} | {marks[6]}\n {marks[1]} | {marks[2]} | {marks[3]}')


def player_input():
	"""
	:return: chosen marks for both players as a tuple.
	"""
	marker = ''
	while not (marker == 'X' or marker == 'O'):
		marker = input('Player1: Choose X or O: ').upper()
	if marker == 'X':
		return ('X', 'O')
	else:
		return ('O', 'X')


def place_marker(board, marker, position):
	board[position] = marker


def win_check(board, mark):
	return ((board[1] == mark and board[2] == mark and board[3] == mark) or
	(board[4] == mark and board[5] == mark and board[6] == mark) or
	(board[7] == mark and board[8] == mark and board[9] == mark) or
	(board[7] == mark and board[4] == mark and board[1] == mark) or
	(board[8] == mark and board[5] == mark and board[2] == mark) or
	(board[9] == mark and board[6] == mark and board[3] == mark) or
	(board[7] == mark and board[5] == mark and board[3] == mark) or
	(board[1] == mark and board[5] == mark and board[9] == mark))
	

def choose_first():
	flip = random.randint(0,1)
	if flip == 0:
		return 'Player1'
	else:
		return 'Player2'


def space_check(board, position):
	return board[position] == ' '


def full_board_check(board):
	for i in range(1,10):
		if space_check(board, i):
			return False
	return True # full board


def player_choice(board):
	position = 0
	while position not in range(1,10) or not space_check(board, position):
		position = int(input('Choose a position: (1-9) '))
	return position


def replay():
	choice = input('Play again? Enter Yes or No ')
	return choice.lower() == 'yes'


print('Welcome in the game')
while True:
	# set up the game
	the_board = [' '] * 10
	player1_marker, player2_marker = player_input()

	# choose first player
	turn = choose_first()
	print(turn + ' will go first')

	# play
	play_game = input('Ready to play? Yes or No ')
	if play_game.lower() == 'yes':
		game_on = True
	else:
		game_on = False

	while game_on:
		if turn == 'Player1':
			display_board(the_board) # show the board
			position = player_choice(the_board) # choose the position
			place_marker(the_board, player1_marker, position) # place marker on the board
			if win_check(the_board, player1_marker):
				display_board(the_board)
				print('Player1 has won!')
				game_on = False
			else:
				if full_board_check(the_board):
					display_board(the_board)
					print('Tie game.')
					game_on = False
				else:
					turn = 'Player2'
		else:
			display_board(the_board) # show the board
			position = player_choice(the_board) # choose the position
			place_marker(the_board, player2_marker, position) # place marker on the board
			if win_check(the_board, player2_marker):
				display_board(the_board)
				print('Player2 has won!')
				game_on = False
			else:
				if full_board_check(the_board):
					display_board(the_board)
					print('Tie game.')
					game_on = False
				else:
					turn = 'Player1'

	# stop the game
	if not replay():
		break


test_board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
display_board(test_board)
place_marker(test_board, '$', 8)
display_board(test_board)
