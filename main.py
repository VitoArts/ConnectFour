#Connect four has 7 columns (Horizontal) and 6 rows (Vertical)
column_1 = ['#', '#', '#', '#', '#', '#']
column_2 = ['#', '#', '#', '#', '#', '#']
column_3 = ['#', '#', '#', '#', '#', '#']
column_4 = ['#', '#', '#', '#', '#', '#']
column_5 = ['#', '#', '#', '#', '#', '#']
column_6 = ['#', '#', '#', '#', '#', '#']
column_7 = ['#', '#', '#', '#', '#', '#']
board = [column_1, column_2, column_3, column_4, column_5, column_6, column_7]
game_state = 'play'
player_turn = 1

def print_board():
    print("This is the current board: ")
    for column in board:
        print(column)

def check_for_victory(drop_location, player_turn):
    return False

if __name__ == '__main__':
    #The game will run until the global state_variable is set to 'false'
    while game_state == 'play':
        print_board()
        print("It's player " + str(player_turn) +"'s turn")
        dropped_state = 'false'
        drop_location = input("Enter the row you'd like to drop (int from 1-7): ")
        for column in reversed(board):
            if column[int(drop_location)-1] == '#':
                if player_turn == 1:
                    column[int(drop_location)-1] = '0'
                    dropped_state = 'true'
                    break
                elif player_turn == 2:
                    column[int(drop_location) - 1] = 'X'
                    dropped_state = 'true'
                    break

        #Using a state to check if a peg has been dropped or not
        if dropped_state == 'false':
            print("Can't drop in this column. It's already full")
            player_turn -= 1

        if check_for_victory(drop_location, player_turn):
            print ("Game over. Player " + player_turn + " wins")
            game_state = 'stop'

        #Player turn assignment
        player_turn += 1
        if player_turn > 2:
            player_turn = 1