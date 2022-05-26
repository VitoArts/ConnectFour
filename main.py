# Connect four has 7 columns (Horizontal) and 6 rows (Vertical)
row_1 = ['#', '#', '#', '#', '#', '#', '#']
row_2 = ['#', '#', '#', '#', '#', '#', '#']
row_3 = ['#', '#', '#', '#', '#', '#', '#']
row_4 = ['#', '#', '#', '#', '#', '#', '#']
row_5 = ['#', '#', '#', '#', '#', '#', '#']
row_6 = ['#', '#', '#', '#', '#', '#', '#']
board = [row_1, row_2, row_3, row_4, row_5, row_6]
game_state = 'play'
player_turn = 1
drop_list = []


def print_board():
    print("This is the current board: ")
    for row in board:
        print(row)


# Obviously the 'easier' way to do this is to loop for loops over every row and column to check every single possibility
# and given the size of the board this probably isn't that much more time spent, but I wanted a way to only check
# rows/columns/diagonals based on the last peg dropped
def check_for_victory(drop_location):
    # Declare variables that will be useful
    column_index = int(drop_location) - 1
    row_index = 6 - drop_list.count(drop_location)
    symbol_chain = 0
    symbol = '0'
    if player_turn == 2:
        symbol = 'X'

    # Vertical check:
    for row in reversed(board):
        if symbol_chain > 3:
            return True
        if row[column_index] == symbol:
            symbol_chain += 1
        else:
            symbol_chain = 0

    # Horizontal check:
    for peg in board[row_index]:
        if symbol_chain > 3:
            return True
        if peg == symbol:
            symbol_chain += 1
        else:
            symbol_chain = 0

    # Diagonal check down-up:
    diagonal_starting_point_x = column_index
    diagonal_starting_point_y = row_index

    if diagonal_starting_point_y < 5 and diagonal_starting_point_x > 0:
        while diagonal_starting_point_y < 5 and diagonal_starting_point_x > 0:
            diagonal_starting_point_y += 1
            diagonal_starting_point_x -= 1

    while diagonal_starting_point_y >= 0 and diagonal_starting_point_x <= 6:
        if symbol_chain > 3:
            return True
        if board[diagonal_starting_point_y][diagonal_starting_point_x] == symbol:
            symbol_chain += 1
        else:
            symbol_chain = 0
        diagonal_starting_point_y -= 1
        diagonal_starting_point_x += 1

    # Diagonal check up-down:
    diagonal_starting_point_x = column_index
    diagonal_starting_point_y = row_index

    if diagonal_starting_point_y > 0 and diagonal_starting_point_x > 0:
        while diagonal_starting_point_y > 0 and diagonal_starting_point_x > 0:
            diagonal_starting_point_y -= 1
            diagonal_starting_point_x -= 1

    while diagonal_starting_point_y <= 5 and diagonal_starting_point_x <= 6:
        if symbol_chain > 3:
            return True
        if board[diagonal_starting_point_y][diagonal_starting_point_x] == symbol:
            symbol_chain += 1
        else:
            symbol_chain = 0
        diagonal_starting_point_y += 1
        diagonal_starting_point_x += 1
    return False


if __name__ == '__main__':
    # The game will run until the global state_variable is set to 'false'
    while game_state == 'play':
        print_board()
        print("It's player " + str(player_turn) + "'s turn")
        dropped_state = 'false'
        drop_location = input("Enter the row you'd like to drop (int from 1-7): ")
        for row in reversed(board):
            if row[int(drop_location) - 1] == '#':
                if player_turn == 1:
                    row[int(drop_location) - 1] = '0'
                    drop_list.append(drop_location)
                    dropped_state = 'true'
                    break
                elif player_turn == 2:
                    row[int(drop_location) - 1] = 'X'
                    drop_list.append(drop_location)
                    dropped_state = 'true'
                    break

        # Using a state to check if a peg has been dropped or not
        if dropped_state == 'false':
            print("Can't drop in this column. It's already full")
            player_turn -= 1

        if check_for_victory(drop_location):
            print_board()
            print("Game over. Player " + str(player_turn) + " wins")
            game_state = 'stop'

        # Player turn assignment
        player_turn += 1
        if player_turn > 2:
            player_turn = 1
