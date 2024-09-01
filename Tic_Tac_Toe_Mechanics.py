from IPython.display import clear_output
import random

board = [" "] * 10  # Initialize a list representing the game board with 10 empty spaces.

def display_board1(board):
    # Function to display the TicTacToe board
    #clear_output()
    print(f'{board[0]} | {board[1]} | {board[2]}')
    print('---------')
    print(f'{board[3]} | {board[4]} | {board[5]}')
    print('---------')
    print(f'{board[6]} | {board[7]} | {board[8]}')

def game_choice():
    # Function to get the player's choice of opponent (human or computer)
    player = input('With Whom do you want to play the human or computer?:-').lower()

    if player == 'human':
        return player
    elif player == 'computer':
        return player
    elif player == 'q':
        quit()
    else:
        print('Invalid Input. Please Try again!')

def marker_choice():
    # Function to choose the marker (X or O) for Player 1 and Player 2
    player1 = 'none'
    player2 = 'none'

    while True:
        player1 = input("Choose your marker 'X' or 'O'?: ").upper()

        if player1 == 'X':
            player2 = 'O'
            print(f'Player1 marker is {player1}')
            print(f'Player2 marker is {player2}')
            break
        elif player1 == 'O':
            player2 = 'X'
            print(f'Player1 marker is {player1}')
            print(f'Player2 marker is {player2}')
            break
        else:
            print('Invalid Input!')
            break

    return player1, player2    

def first_start():
    # Function to randomly choose which player starts first
    start = str(random.randint(0, 2))

    if start == '1':
        return 'player1'
    else:
        return 'player2'

def check_space(board, position):
    # Function to check if a specific position on the board is empty
    if board[position] == ' ':
        return True
    else:
        return False

def check_board(board):
    # Function to check if the board is full (no empty spaces)
    for i in range(0, 9):
        if check_space(board, i):
            return False
    return True

def choice_position(board):
    # Function to get the player's chosen position for placing their marker
    while True:
        try:
            position = int(input(f'Player1 Enter the position where you want to place your marker: '))

            if position in range(9) and check_space(board, position):
                return position
            else:
                print('Invalid or place already used!')
        except ValueError:
            print('Invalid position choice. Please try again!')

def place_marker(board, choice, position):
    # Function to place a player's marker on the board at the specified position
    board[position] = choice

def check_winner(board, choice):
    # Function to check if a player has won by checking all possible winning combinations
    if (choice == board[0] == board[1] == board[2]) or (choice == board[3] == board[4] == board[5]) or (choice == board[6] == board[7] == board[8]) or (choice == board[0] == board[3] == board[6]) or (choice == board[1] == board[4] == board[7]) or (choice == board[2] == board[5] == board[8]) or (choice == board[0] == board[4] == board[8]) or (choice == board[2] == board[4] == board[6]):
        return True
    else:
        return False

def replay():
    # Function to ask the user if they want to play again
    while True:
        replay = input('Enter -yes- to play again and -no- to exit the game: ')

        if replay == 'yes':
            print('Here we go again:)')
            return True
        elif replay == 'no':
            print('Game Over!')
            return False
        else:
            print('Invalid Input, Please enter -yes- to continue the game or -no- to exit the game')

def comp_moves(board):
    # Function to get a random move for the computer in easy mode
    comp_input = random.randrange(9)

    while not check_space(board, comp_input):
        comp_input = random.randrange(9)

    return comp_input

def choice_position2(board):
    # Function to get Player 2's chosen position for placing their marker
    while True:
        try:
            position = int(input(f'Player2 Enter the position where you want to place your marker: '))

            if position in range(9) and check_space(board, position):
                return position
            else:
                print('Invalid or place already used!')
        except ValueError:
            print('Invalid position choice. Please try again!')

def minimax(board, d, isMaximizing, player1, player2):
    # Minimax algorithm to find the best move for the computer in hard mode
    if check_winner(board, player1):
        return -10 + d
    elif check_winner(board, player2):
        return 10 - d
    elif check_board(board):
        return 0 

    if isMaximizing:
        max_val = float('-inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = player2
                max_val2 = minimax(board, d+1, False, player1, player2)
                board[i] = ' '
                max_val = max(max_val, max_val2)
        return max_val
    else:
        min_val = float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = player1
                min_val2 = minimax(board, d+1, True, player1, player2)
                board[i] = ' '
                min_val = min(min_val, min_val2)
        return min_val

def find_best_move(board, player1, player2):
    # Function to find the best move for the computer using the minimax algorithm
    best_move = -1 
    best_val = float('-inf')

    for i in range(9):
        if board[i] == ' ':
            board[i] = player2
            next_val = minimax(board, 0, False, player1, player2)
            board[i] = ' '
            if next_val > best_val:
                best_val = next_val
                best_move = i
    return best_move

def comp_move1(board, player2, player1):
    # Function to get the computer's move in medium mode based on simple heuristics
    poss_move = [x for x, letter in enumerate(board) if letter == ' ' ]
    move = 0

    for l in [player2, player1]:
        for i in poss_move:
            b1 = board[:]
            b1[i] = l
            if check_winner(b1, l):
                move = i
                return move
                
    corner = []
    for i in poss_move:
        if i in [0, 2, 6, 8]:
            corner.append(i)
                
    if len(corner) > 0:
        move = random.choice(corner)
        return move

    if 4 in poss_move:
        move = 4
        return move

    edge = []
    for i in poss_move:
        if i in [1, 3, 5, 7]:
            edge.append(i)

    if len(edge) > 0:
        move = random.choice(edge)

    return move 

def choose_difficulty():
    # Function to choose the difficulty level of the game
    difficulty = input('Choose the difficulty between -Hard- or -Medium- or -Easy- here: ').lower()

    if difficulty == 'hard':
        return difficulty
        
    if difficulty == 'medium':
        return difficulty

    if difficulty == 'easy':
        return difficulty
