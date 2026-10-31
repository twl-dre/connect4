import random
import math

def check_move(board, turn, col, pop):
    c = 7
    r = int(len(board)/c)
    if pop == True:
        if board[col] == turn: return True
        else: return False
    elif board[(r * c) - c + col] == 0: return True
    else: return False

def apply_move(board, turn, col, pop):
    c = 7
    r = int(len(board)/c)
    if pop == True:
        board_updated = board.copy()
        for i in range(r - 1):
            index = (i * c) + col
            board_updated[index] = board_updated[index + c]
        board_updated[(r * c) - c + col] = 0            
        return board_updated
    else:
        for i in range(r):
            index = (i * c) + col
            if board[index] == 0:
                board_updated = board.copy()
                board_updated[index] = turn
                return board_updated

def check_victory(board, who_played):
    c = 7
    r = int(len(board)/c)
    player1win = False
    player2win = False
    for i in range(c * (r - 3)):
        if board[i] == board[i + c] == board[i + c * 2] == board [i + c * 3] == 1: player1win = True
        if board[i] == board[i + c] == board[i + c * 2] == board [i + c * 3] == 2: player2win = True
        
    for i in range(0, r * c, 7):
        for j in range(i, i + 4):
            if board[j] == board[j + 1] == board[j + 2] == board[j + 3] == 1: player1win = True
            if board[j] == board[j + 1] == board[j + 2] == board[j + 3] == 2: player2win = True
    
    if r >= 4:       
        for i in range(0, c * (r - 3), 7):
            for j in range(i , i + 4):
                if board[j] == board[j + 8] == board[j + 16] == board [j + 24] == 1: player1win = True
                if board[j] == board[j + 8] == board[j + 16] == board [j + 24] == 2: player2win = True

        for i in range(0 , r * c - 4 , 7):
            for j in range(i , i + 4):
                if board[j] == board[j - 6] == board[j - 12] == board [j - 18] == 1: player1win = True
                if board[j] == board[j - 6] == board[j - 12] == board [j - 18] == 2: player2win = True
    
    if player1win == True and player2win == True:
        if who_played == 1: return 2
        else: return 1
    elif player1win == True: return 1
    elif player2win == True: return 2
    else: return 0
    

def computer_move(board, turn, level):
    #
    return (0,False)
    
def display_board(board):
    print(board)
    pass

def menu():
    print("Connect 4")
    while True:
        try: 
            r = int(input("How many rows would you like to have? "))
            if r < 0: 
                print("Invalid input! Enter a positive integer!")
                continue
            break
        except ValueError: print("Invalid input! Enter a positive integer!")
    c = 7
    board = [0] * r * c
    turn = 1
    who_played = 1
    col = None
    pop = False
    game_over = False
    while game_over == False:
        display_board(board)
        while True:
            pop_user = str(input("Pop or add? (p: pop a: add) "))
            if pop_user == "p": 
                pop = True
                break
            elif pop_user == "a": 
                pop = False
                break
            else: print("Invalid input!" )
        while True:
            try:
                col = int(input("Enter a column number! (1-7) ")) - 1
                if not col in range(c):
                    print("Invalid input!")
                    continue
                break
            except ValueError: print("Invalid input! Enter an integer from 1 to 7 (inclusive)!")
        if check_move(board, turn, col, pop):
            board = apply_move(board, turn, col, pop)
            if turn == 1: 
                turn = 2
                who_played = 1
            else: 
                turn = 1
                who_played = 2
        else: print("Invalid input!")
        if check_victory(board, who_played) == 1: 
            display_board(board)
            print("Player 1 wins!")
            game_over = True
        elif check_victory(board, who_played) == 2:
            display_board(board)
            print("Player 2 wins!")
            game_over = True
    pass

if __name__ == "__main__": 
    menu()
    
