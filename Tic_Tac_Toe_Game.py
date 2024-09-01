from Tic_Tac_Toe_Mechanics import display_board1, game_choice, marker_choice, first_start, check_space, check_board, choice_position, check_winner, replay, place_marker, comp_moves, choice_position2, find_best_move, minimax, comp_move1, choose_difficulty

def game():

    print('----Welcome to the TicTacToe----')

    tic = True
    while tic:
        # Initialize the game board with 10 empty spaces (index 0 will be unused)
        board = [" "] * 10

        # Ask the player to choose the game mode: human vs human or human vs computer
        player_choice = game_choice()

        if player_choice == 'human':
            # Players choose their markers (X or O)
            player1, player2 = marker_choice()

            # Determine who will start first
            first_player = first_start()
            print(f'{first_player} will start first')

            game_on = True

            while game_on:
                if first_player == 'player1':
                    # Display the current game board
                    display_board1(board)
                    print("--------------")

                    # Player 1 chooses a position on the board
                    position = choice_position(board)

                    # Place the marker for Player 1 on the chosen position
                    place_marker(board, player1, position)

                    # Check if Player 1 wins
                    if check_winner(board, player1):
                        display_board1(board)
                        print('Player 1 wins Here!')
                        game_on = False
                    else:
                        # Check if the game board is full (tie)
                        if check_board(board):
                            print('ITS A TIE!')
                            break
                        else:
                            # Switch to Player 2
                            first_player = 'player2'

                else:
                    # Display the current game board
                    display_board1(board)
                    print("--------------")

                    # Player 2 chooses a position on the board
                    position = choice_position2(board)

                    # Place the marker for Player 2 on the chosen position
                    place_marker(board, player2, position)

                    # Check if Player 2 wins
                    if check_winner(board, player2):
                        display_board1(board)
                        print('Player 2 wins Here!')
                        game_on = False
                    else:
                        # Check if the game board is full (tie)
                        if check_board(board):
                            print('ITS A TIE!')
                            break
                        else:
                            # Switch to Player 1
                            first_player = 'player1'

            # Ask the players if they want to play again
            if not replay():
                break

        elif player_choice == 'computer':
            # Choose the difficulty level for the computer opponent
            mode = choose_difficulty()

            if mode == 'hard':
                player1, player2 = marker_choice()
                first_player = first_start()
                print(f'{first_player} goes first here!')

                game_in = True

                while game_in:
                    if first_player == 'player1':
                        # Player 1's turn
                        print("")
                        display_board1(board)
                        print("")
                            
                        position = choice_position(board)
                        place_marker(board, player1, position)

                        if check_winner(board, player1):
                            display_board1(board)
                            print(f'{first_player} wins here!')
                            game_in = False
                        else:
                            if check_board(board):
                                print('Its a Tie!')
                                game_in = False
                            else:
                                first_player = 'player2'
                        
                    if first_player == 'player2':
                        # Computer's turn with "hard" difficulty using the minimax algorithm
                        comp_position = find_best_move(board, player1, player2)
                        place_marker(board, player2, comp_position)

                        if check_winner(board, player2):
                            display_board1(board)
                            print(f'{first_player} wins here!')
                            game_in = False
                        else:
                            if check_board(board):
                                print('Its a Tie!')
                                game_in = False
                            else:
                                first_player = 'player1'
                            
                if not replay():
                    game_in = False

            elif mode == 'medium':
                player1, player2 = marker_choice()
                first_player = first_start()
                print(f'{first_player} goes first here!')

                game_in = True

                while game_in:
                    if first_player == 'player1':
                        # Player 1's turn
                        print("")
                        display_board1(board)
                        print("")
                            
                        position = choice_position(board)
                        place_marker(board, player1, position)

                        if check_winner(board, player1):
                            display_board1(board)
                            print(f'{first_player} wins here!')
                            game_in = False
                        else:
                            if check_board(board):
                                print('Its a Tie!')
                                game_in = False
                            else:
                                first_player = 'player2'
                        
                    else:
                        # Computer's turn with "medium" difficulty using a heuristic move
                        print("")
                        display_board1(board)
                        print("")
                        comp_position = comp_move1(board, player2, player1)
                        place_marker(board, player2, comp_position)

                        if check_winner(board, player2):
                            display_board1(board)
                            print(f'{first_player} wins here!')
                            game_in = False
                        else:
                            if check_board(board):
                                display_board1(board)
                                print('Its a Tie!')
                                game_in = False
                            else:
                                first_player = 'player1'
                            
                if not replay():
                    game_in = False

            elif mode == 'easy':
                player1, player2 = marker_choice()
                first_player = first_start()
                print(f'{first_player} goes first here!')

                game_in = True

                while game_in:
                    if first_player == 'player1':
                        # Player 1's turn
                        print("")
                        display_board1(board)
                        print("")
                            
                        position = choice_position(board)
                        place_marker(board, player1, position)

                        if check_winner(board, player1):
                            display_board1(board)
                            print(f'{first_player} wins here!')
                            game_in = False
                        else:
                            if check_board(board):
                                print('Its a Tie!')
                                game_in = False
                            else:
                                first_player = 'player2'
                        
                    if first_player == 'player2':
                        # Computer's turn with "easy" difficulty making random moves
                        comp_position = comp_moves(board)
                        place_marker(board, player2, comp_position)

                        if check_winner(board, player2):
                            display_board1(board)
                            print(f'{first_player} wins here!')
                            game_in = False
                        else:
                            if check_board(board):
                                print('Its a Tie!')
                                game_in = False
                            else:
                                first_player = 'player1'
                            
                if not replay():
                    game_in = False
            else:
                print('Invalid difficulty choice!')
        else:
            print('Invalid Choice!')

game()
