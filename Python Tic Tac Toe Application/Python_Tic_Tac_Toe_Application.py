class Game:
	
	def play(self):
		board = [ ' ',' ',' ',' ',' ',' ',' ',' ',' ' ]
		counter = 1
		print('Welcome to your new game!')
		print(f" {board[0]} | {board[1]} | {board[2]} \n" + "---+---+--- \n"
	   + f" {board[3]} | {board[4]} | {board[5]} \n" + "---+---+--- \n"
	   + f" {board[6]} | {board[7]} | {board[8]} ")
		while counter < 10:
			if counter % 2 == 0:
				move = 'O'
			else:
				move = 'X'
			user_move = input('Make your move')
			if user_move == '1':
				if board[0] == ' ':
					board[0] = move
					counter += 1
				else:
					print('This option has already been used. Please choose a valid option')
					continue
			elif user_move == '2':
				if board[1] == ' ':
					board[1] = move
					counter += 1
				else:
					print('This option has already been used. Please choose a valid option')
					continue
			elif user_move == '3':
				if board[2] == ' ':
					board[2] = move
					counter += 1
				else:
					print('This option has already been used. Please choose a valid option')
					continue
			elif user_move == '4':
				if board[3] == ' ':
					board[3] = move
					counter += 1
				else:
					print('This option has already been used. Please choose a valid option')
					continue
			elif user_move == '5':
				if board[4] == ' ':
					board[4] = move
					counter += 1
				else:
					print('This option has already been used. Please choose a valid option')
					continue
			elif user_move == '6':
				if board[5] == ' ':
					board[5] = move
					counter += 1
				else:
					print('This option has already been used. Please choose a valid option')
					continue
			elif user_move == '7':
				if board[6] == ' ':
					board[6] = move
					counter += 1
				else:
					print('This option has already been used. Please choose a valid option')
					continue
			elif user_move == '8':
				if board[7] == ' ':
					board[7] = move
					counter += 1
				else:
					print('This option has already been used. Please choose a valid option')
					continue
			elif user_move == '9':
				if board[8] == ' ':
					board[8] = move
					counter += 1
				else:
					print('This option has already been used. Please choose a valid option')
					continue
			else:
				print('Please input a number from 1 to 9')
				continue
			print(f" {board[0]} | {board[1]} | {board[2]} \n" + "---+---+--- \n"
	   + f" {board[3]} | {board[4]} | {board[5]} \n" + "---+---+--- \n"
	   + f" {board[6]} | {board[7]} | {board[8]} ")
			if counter == 10:
				print('This is a draw')
			elif ((board[0] !=' ' and board[0] == board[1] == board[2]) 
			or (board[0] !=' ' and board[0] == board[4] == board[8])
			or (board[0] !=' ' and board[0] == board[3] == board[6])
			or (board[1] !=' ' and board[1] == board[4] == board[7])
			or (board[2] !=' ' and board[2] == board[5] == board[8])
			or (board[2] !=' ' and board[2] == board[4] == board[6])
			or (board[3] !=' ' and board[3] == board[4] == board[5])
			or (board[7] !=' ' and board[7] == board[6] == board[8])):
				print(f'{move} won the game')
				break

print('Welcome to a Python Tic Tac Toe Game')
menu = ('Press 1 for game menu \n' + 'Press 2 for info about the programmer of this app \n' + 
	  'Press 3 to quit: ')
user_quit = False
while user_quit == False:
	print(menu)
	choice = input('What do you want to do?: ')
	print(choice)
	if choice == '1':
		making_choice = True
		while making_choice == True:
			print('1. New game \n' + '2. Game Instructions \n' + '3. Main Menu')
			game_choice = input('Choice:')
			if game_choice == '1':
					tic_tac_toe = Game()
					tic_tac_toe.play()
					press_enter = input('Press enter to return to game menu')
			elif game_choice == '2':
				print('Use the keyboard characters from numbers 1 to 9. \n' 
		  + ' Each of these characters is placed on the board as shown below \n'
		  + ' 1 | 2 | 3 \n' + '---+---+--- \n' + ' 4 | 5 | 6 \n' + '---+---+--- \n' + ' 7 | 8 | 9 \n' )
				press_enter = input('Press enter to return to game menu')
			elif game_choice == '3':
					break
			else:
					print('Invalid input. Please follow the instructions below')
					continue
	elif choice == '2':
		print('Raymond is a programmer who can program in Python, C#, SQL and Javascript')
	elif choice == '3':
		user_quit = True

