import random
import math
import numpy as np

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
    c = 7
    if level == 1:
        while True:
            col = random.randint(0, c - 1)
            pop = random.choice((True, False))
            if check_move(board, turn, col, pop): return (col, pop)
            else: continue
    elif level == 2:
        while True:
            if turn == 1: turn_after = 2
            else: turn_after = 1
            for i in range(c):
                board_temporary = apply_move(board, turn, i, False)
                if check_victory(board_temporary, turn) == turn:
                    return(i, False)
            for i in range(c):
                board_temporary = apply_move(board, turn_after, i, False)
                if check_victory(board_temporary, turn_after) == turn_after:
                    return (i, False)
            else:
                col = random.randint(0, c - 1)
                pop = random.choice((True, False))
                if check_move(board, turn, col, pop): return (col, pop)
    
def display_board(board):
    c = 7
    r = int(len(board)/c)
    print(np.fliplr(np.array(board[::-1]).reshape(r, c)))
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
    while True:
        player1 = input("Player 1! Human or computer? (h: human c: computer) ")
        if player1 == "h": break
        elif player1 == "c":
            while True:
                try:
                    level1 = int(input("Pick a level for Player 1! (1: Easy 2: Medium) "))
                    if not level1 in range(1, 3):
                        print("Invalid input! Enter a positive integer!")
                        continue
                    break
                except ValueError: print("Invalid input! Enter either '1' or '2'!")
            break
        else: print("Invalid input!") 
    while True:
        player2 = input("Player 2! Human or computer? (h: human c: computer) ")
        if player2 == "h": break 
        elif player2 == "c":
            while True:
                try:
                    level2 = int(input("Pick a level for Player 2! (1: Easy 2: Medium) "))
                    if not level2 in range(1, 3):
                        print("Invalid input! Enter a positive integer!")
                        continue
                    break
                except ValueError: print("Invalid input! Enter either '1' or '2'!")
            break
        else: print("Invalid input!")
    c = 7
    board = [0] * r * c
    turn = 1
    who_played = 1
    col = None
    pop = False
    while check_victory(board, who_played) == 0:
        display_board(board)
        print("Player ", turn, "'s turn", sep="")
        if (player1, turn) == ("c", 1):
            level = level1
            col, pop = computer_move(board, turn, level)
        elif (player2, turn) == ("c", 2):
            level = level2
            col, pop = computer_move(board, turn, level)
        while (player1, turn) == ("h", 1) or (player2, turn) == ("h", 2):
            pop_user = str(input("Pop or add? (p: pop a: add) "))
            if pop_user == "p": 
                pop = True
            elif pop_user == "a": 
                pop = False
            else: 
                print("Invalid input!")
                continue
            try:
                col = int(input("Enter a column number! (1-7) ")) - 1
                if not col in range(c):
                    print("Invalid input! Enter an integer from 1 to 7 (inclusive)!")
                    continue
                elif not check_move(board, turn, col, pop):
                    if pop == True:
                        if board[col] == 0: print("No piece to pop on that column! Try another column!")
                        else: print("The bottom piece cannot be popped because it's not your piece! Try another column!")
                    else:
                        print("Column full! Try another column!")    
                    continue
                break
            except ValueError: print("Invalid input! Enter an integer!")
        board = apply_move(board, turn, col, pop)
        if turn == 1: 
            turn = 2
            who_played = 1
        else: 
            turn = 1
            who_played = 2
        if check_victory(board, who_played) == 1: 
            display_board(board)
            print("Player 1 wins!")
        elif check_victory(board, who_played) == 2:
            display_board(board)
            print("Player 2 wins!")
    pass

if __name__ == "__main__": 
    menu()
    
