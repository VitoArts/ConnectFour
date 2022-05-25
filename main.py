#Connect four has 7 columns (Horizontal) and 6 rows (Vertical)
row_1 = ['#', '#', '#', '#', '#', '#', '#']
row_2 = ['#', '#', '#', '#', '#', '#', '#']
row_3 = ['#', '#', '#', '#', '#', '#', '#']
row_4 = ['#', '#', '#', '#', '#', '#', '#']
row_5 = ['#', '#', '#', '#', '#', '#', '#']
row_6 = ['#', '#', '#', '#', '#', '#', '#']
board = [row_1, row_2, row_3, row_4, row_5, row_6]
game_state = 'play'
player_turn = 1

def print_board():
    print("This is the current board: ")
    for row in board:
        print(row)

#horizontal
def check_for_victory(drop_location):
    return False

if __name__ == '__main__':
    #The game will run until the global state_variable is set to 'false'
    while game_state == 'play':
        print_board()
        print("It's player " + str(player_turn) +"'s turn")
        dropped_state = 'false'
        drop_location = input("Enter the row you'd like to drop (int from 1-7): ")
        for row in reversed(board):
            if row[int(drop_location)-1] == '#':
                if player_turn == 1:
                    row[int(drop_location)-1] = '0'
                    dropped_state = 'true'
                    break
                elif player_turn == 2:
                    row[int(drop_location) - 1] = 'X'
                    dropped_state = 'true'
                    break

        #Using a state to check if a peg has been dropped or not
        if dropped_state == 'false':
            print("Can't drop in this column. It's already full")
            player_turn -= 1

        if check_for_victory(drop_location):
            print ("Game over. Player " + str(player_turn) + " wins")
            game_state = 'stop'

        #Player turn assignment
        player_turn += 1
        if player_turn > 2:
            player_turn = 1