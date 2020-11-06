'''
 X | O | X
---+---+---
 O | O | X
---+---+---
   | X |
'''

import random

def print_board_and_legend(board):
    for i in range(3):
        line1 = " " +  board[i][0] + " | " + board[i][1] + " | " +  board[i][2]
        line2 = "  " + str(3*i+1)  + " | " + str(3*i+2)  + " | " +  str(3*i+3)
        print(line1 + " "*5 + line2)
        if i < 2:
            print("---+---+---" + " "*5 + "---+---+---")

def make_empty_board():
    board = []
    for i in range(3):
        board.append([" "]*3)
    return board

# 1 a)
def board_coordinate(square_num):
    '''Returns coordinate in a list [row, column] of the
    given position
    '''
    row = ((square_num - 1) // 3)
    position = (3 * row) + 1

    for column_count in range(3):
        if position == square_num:
            return [row,column_count]
        position += 1
    return None

# 1 b)
def put_in_board(board, mark, square_num):
    '''Mark ("X" or "O") in the coordinates of square_num
    '''
    board[board_coordinate(square_num)[0]][board_coordinate(square_num)[1]] = mark
    return board

# 1 c) in main block

# 2 a)
def get_free_squares(board):
    ''' Returns coords of empty squares
    '''
    empty = []    # keeps track of coords empty squares
    coord = []

    # for each squares, check if the content is equal to " "
    #get the coordinate and append it to the empty tracking array

    for i in range(len(board)):
        for e in range(len(board[0])):
            if board[i][e] == " ":
                coord = [i,e]
            empty.append(coord)
    return empty

# 2 b)
def make_random_move(board, mark):
    ''' finds a random free square in board and put mark in that square
    '''
    empty = get_free_squares(board)
    random_square_coord = empty[int(len(empty) * random.random())]

    board[random_square_coord[0]][random_square_coord[1]] = mark

    return board

# 2 c) in main block

# 3 a)
def is_row_all_marks(board, row_i, mark):
    ''' Returns True iff row_i in board contains 3 marks = mark
    '''
    # check every element in row_i if they are all equal to mark
    return board[row_i] == [mark,mark,mark]

# 3 b)
def is_col_all_marks(board, col_i, mark):
    ''' Returns True iff col_i in board contains 3 marks = mark'''
    # check every element in row_i if they are all equal to mark
    column = []

    for i in board:
        column.append(i[col_i])

    return column == [mark,mark,mark]


# 3 c)
# use the above 2 fcns, also check diagonals
def is_diagonal_all_marks(board, mark):
    diagonal_1 = []
    diagonal_2 = []

    for i in range (len(board)):
        diagonal_1.append(board[i][i])
        diagonal_2.append(board[len(board)-1-i][i])

    return diagonal_1 == [mark,mark,mark] or diagonal_2 == [mark,mark,mark]

def is_win(board, mark):
    ''' Returns True iff the mark mark won on the board board'''
    for i in range(len(board)):
        if is_row_all_marks(board,i,mark) or is_col_all_marks(board,i,mark) or is_diagonal_all_marks(board,mark):
            return True
    return False

# 3 d) in main block

# 4 a)
# Write a function which tries to put the computer’s mark in every free square on the board, and checks
# whether is_win() returns True for the new board, returns if it does, and removes the mark and tries
# to place it in another square otherwise. If there is no square such that putting a mark in it leads to an
# immediate win, the function should put mark in a random free square

def smart_move(board,mark):
    empty_board = get_free_squares(board)
    test_board = board

    for i in empty_board:
        test_board[i[0]][i[1]] = mark
        if is_win(test_board,mark):
            return test_board
        else:
            test_board = board

    return(make_random_move())

# 4 b)
# Improve the algorithm that plays for the computer as much as you can.

if __name__ == '__main__':
    board = make_empty_board()
    print_board_and_legend(board)

    game = True
    won = False

    invalid_input = True
    while game:
        while invalid_input:
            input_str = input("Enter your move: ")
            if input_str not in (["1","2","3","4","5","6","7","8","9"]):
                print("Invalid Input. Try again.")
            else:
                invalid_input = False
                board = put_in_board(board, "X", int(input_str))
                print_board_and_legend(board)
                print("\n")

        #user win check
        won = is_win(board,"X")
        if won:
            print("Congratulations!")
            break

        #Computer move
        board = make_random_move(board,"O")
        invalid_input = True
        print_board_and_legend(board)

        #computer win check
        won = is_win(board,"X")
        if won:
            print("Lost!")
            print_board_and_legend(board)
            break

    '''
    turn_counter = 0
    # 1 c)
    while game:
        if turn_counter % 2 == 0:
            mark = "X"
        else:
            mark = "O"

        input_str = input("Enter your move: ")
        if input_str not in (["1","2","3","4","5","6","7","8","9"]):
            print("Invalid Input. Try again.")
            turn_counter -= 1
        else:
            board = put_in_board(board, mark, int(input_str))

        print_board_and_legend(board)
        print("\n\n")

        if is_win(board,mark):
            print(f'Congratulations! {mark} won!')
            break

        turn_counter += 1
    '''
