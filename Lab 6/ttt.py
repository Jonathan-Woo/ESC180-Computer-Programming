'''
 X | O | X
---+---+---
 O | O | X    
---+---+---
   | X | 
'''

import random

#default methods
def print_board_and_legend(board):
    '''draws the board and legend to the screen
    '''
    for i in range(3):
        line1 = " " +  board[i][0] + " | " + board[i][1] + " | " +  board[i][2]
        line2 = "  " + str(3*i+1)  + " | " + str(3*i+2)  + " | " +  str(3*i+3) 
        print(line1 + " "*5 + line2)
        if i < 2:
            print("---+---+---" + " "*5 + "---+---+---")
        
def make_empty_board():
    '''creates an empty board with empty values
    '''
    board = []
    for i in range(3):
        board.append([" "]*3)
    return board

#question 1a
def board_coordinate(square_num):
    '''Returns coordinate in a list [row,column] of the 
    given position 
    '''
    row = ((square_num - 1) // 3)
    
    position = (3 * row) + 1
    
    for column_count in range(3):
        if position == square_num:
            return [row,column_count]
        position += 1
    return None

#question 1b
def put_in_board(board, mark, square_num):
    '''Mark ("X" or "O") in the coordinates of square_num
    '''
    board[board_coordinate(square_num)[0]][board_coordinate(square_num)[1]] = mark
    
if __name__ == '__main__':
    board = make_empty_board()
    print_board_and_legend(board)    
    
    print("\n\n")
    
    print(board_coordinate(board, 3))
    
    board = [["O", "X", "X"],
             [" ", "X", " "],
             [" ", "O", " "]]
    
    print_board_and_legend(board)
