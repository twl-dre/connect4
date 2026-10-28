import random
import math

def check_move(board, turn, col, pop):
    c = 7
    r = int((len(board) + 1)/c)
    if pop == True:
        if board[col] == turn: return True
        else: return False
    elif board[(r * c) - c + col] == 0: return True
    else: return False

def apply_move(board, turn, col, pop):
    c = 7
    r = int(len(board)/c)
    if check_move(board, turn, col, pop):
        if pop == True:
            for i in range(r - 1):
                index = i * c + col
            board[index] = board[index + c]
        else:
            for i in range(r - 1):
                index = i * c + col
                if board[index] == 0:
                    board_updated = board.copy()
                    board_updated[index] == turn
                    return board_updated

def check_victory(board, who_played):
    who_played = 0
    c = 7
    r = int(len(board)/c)
    for i in range(c * (r - 3)):
        if board[i] == board[i + c] == board[i + c * 2] == board [i + c * 3] > 0: 
            who_played = board [i]
            if who_played == 1: return 1
            else: return 2
    for i in range(0, r * c, 7):
        for j in range(i, i + 4):
            if board[j] == board[j + 1] == board[j + 2] == board[j + 3] == 1 > 0:
                who_played = board [i]
                if who_played == 1: return 1
                else: return 2
    for i in range(0, c * (r - 3), 7):
        for j in range(i , i + 4):
            if board[j] == board[j + 8] == board[j + 16] == board [j + 24] > 0:
                who_played = board [i]
                if who_played == 1: return 1
                else: return 2
    for i in range(0 , r * c - 4 , 7):
        for j in range(i , i + 4):
            if board[j] == board[j - 6] == board[j - 12] == board [j - 18] > 0:
                who_played = board [i]
                if who_played == 1: return 1
                else: return 2
    if who_played > 0: return who_played
    else: return 0 

def computer_move(board, turn, level):
    # implement your function here
    return (0,False)
    
def display_board(board):
    # implement your function here
    pass

def menu():
    # implement your function here
    pass

if __name__ == "__main__": 
    menu()


    
