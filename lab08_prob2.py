"""
CISC 131 Problem 1 - Ani Lamichhane (lami5034)
"""

import random

def createBoard(dims):
    board = []
    for row in range(dims):
        board.append([])
        for _column in range(dims):
            rnum = random.randint(0, 1)
            board[row].append(bool(rnum))
    return board

def printBoard(board):
    dims = len(board[1])
    for column in range(dims):
        for row in range(dims):
            if board[column][row] is True:
                print("@", end="")
            else:
                print("0", end="")
        print("")

def winningBoard(board):
    for i in range(len(board)):
        for x in range(len(board[i])):
            if board[i][x] is True:
                return False
    return True

def makeMove(board, x, y):
    positionx = (len(board) - 1 - (y - 1))
    positiony = x - 1

    if (x < 1 or x > len(board)) or (y < 1 or y > len(board)):
        return False

    board[positionx][positiony] = not board[positionx][positiony]
    for i in range(len(board)):
        for j in range(len(board[i])):
            if positionx == i:
                if abs(j - positiony) == 1:
                    board[i][j] = not board[i][j]
            elif (j - positiony) == 0:
                if abs(i - positionx) == 1:
                    board[i][j] = not board[i][j]

    return True

def playLightsOut():

    dim = int(input("What size board do you want to start with? "))
    board = createBoard(dim)
    printBoard(board)

    keep_going = True

    while keep_going:
        x = int(input("Enter an x coordinate: "))
        y = int(input("Enter an y coordinate: "))

        if not makeMove(board, x, y):
            print("Not a valid move")
        printBoard(board)

        if winningBoard(board):
            print("You won!!!")
            keep_going = False

        else:
            input_string = input("Do you want to keep going (Y/N)? ")
            if input_string != "Y" and input_string != "y":
                keep_going = False
playLightsOut()
