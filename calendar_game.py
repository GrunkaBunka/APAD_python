import numpy as np
import math
import time
#numpy
rng = np.random.default_rng()

#get the date
print("please enter the month as a number (Jan as 1, Feb as 2, etc.)")
month = int(input())
print("please enter the day of the month")
day = int(input())

#make the empty board
board = np.zeros((7,7))
board[0:2,6]=9
board[6,3:7]=9

#make the according space -1
if month < 7:
    board[0,month-1]=-1
else:
    board[1,month-7]=-1

if day < 8:
    board[2,day-1]=-1
elif day < 15:
    board[3,day-8]=-1
elif day < 22:
    board[4,day-15]=-1
elif day < 29:
    board[5,day-22]=-1
else:
    board[6,day-29]=-1

#make a dictionary with a numpy array and a boolean stating if the piece is used or not
pieces = {1: [np.array([[1,0],[1,0],[1,1],[0,1]]),0],
          2: [np.array([[0,0,2],[2,2,2],[2,0,0]]),0],
          3: [np.array([[3,3,3],[3,0,0],[3,0,0]]),0],
          4: [np.array([[4,0],[4,4],[4,0],[4,0]]),0],
          5: [np.array([[5,5,5],[5,5,5]]),0],
          6: [np.array([[6,6],[6,6],[6,0]]),0],
          7: [np.array([[0,0,0,7],[7,7,7,7]]),0],
          8: [np.array([[8,0,8],[8,8,8]]),0]}

#place a piece on the board
def place(p,x,y):
    #check if piece will be out of bounds at all
    def outbounds(p,x,y):
        if (x+pieces[p][0].shape[0]) > 7:
            return True
        elif (y+pieces[p][0][0].shape[0]) > 7:
            return True
        else:
            return False
    #before indexing make sure the piece won't be out of bounds
    #check if a piece will overlap with anything currently on the board
    def overlap(p,x,y):
        if outbounds(p,x,y):
            return True
        for i in range(0,pieces[p][0].shape[0]):
            for j in range(0,pieces[p][0][0].shape[0]):
                if board[x+i,y+j] != 0 and pieces[p][0][i,j] != 0:
                    return True
        return False
    #check if piece is used or if they will overlap
    if pieces[p][1] != 1 and not overlap(p,x,y):
        for i in range(0,pieces[p][0].shape[0]):
            for j in range(0,pieces[p][0][0].shape[0]):
                #index across the rows and columns replacing
                board[x+i,y+j]=pieces[p][0][i,j]
                pieces[p][1] = 1


#rotate a piece left
def rotatel(p):
   pieces[p][0] = np.rot90(pieces[p][0])
#rotate a piece right
#this function is kinda arbitrary but im gonna keep it for now incase it comes in handy later
def rotater(p):
   rotatel(p)
   rotatel(p)
   rotatel(p)
#horizontally flip a piece
def flip(p):
   pieces[p][0] = np.fliplr(pieces[p][0])

#check if the board is solved
def solvecheck(board):
    for i in board:
        for j in i:
            if j == 0:
                return False
    return True

#solve it
counter = 0
copy = board.copy
def solve(board,counter):
    counter += 1
    if solvecheck(board):
        print(board)
        print("The puzzle is solved!")
        return
    elif counter < 10:
        #make a random number 1 to 8 to choose a piece
        randyp = rng.random()
        randyp *= 8
        randyp += 1
        randyp = math.trunc(randyp)
        #make a random number 0 to 6 to choose an x
        randyx = rng.random()
        randyx *= 6
        randyx = math.trunc(randyx)
        #make a random number 0 to 6 to choose a y
        randyy = rng.random()
        randyy *= 6
        randyy = math.trunc(randyy)
        #place piece at a random spot
        place(randyp,randyx,randyy)
        print(" ")
        print(board)
        time.sleep(1)
        counter += 1
        solve(board,counter)
    else:
        counter = 0
        board = copy
        solve(board,counter)

solve(board,counter)
