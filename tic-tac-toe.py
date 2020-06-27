import sys
import random
def display_board(board):
    print(' '+board[7]+' | '+board[8]+' | '+board[9]+' ')
    print('-----------')
    print(' '+board[4]+' | '+board[5]+' | '+board[6]+' ')
    print('-----------')
    print(' '+board[1]+' | '+board[2]+' | '+board[3]+' ')


def user_1(marker1, u1, board):
    pos1 = int(input("Enter the position: "))
    if(pos1>=1 and pos1<=9):
        if board[pos1] == '':
            board[pos1] = marker1
            u1.append(pos1)
        else:
            print("You can't select this position")
    else:
        print("You can't select this position")
    display_board(board)


def user_2(marker2, u2, board):
    pos2 = int(input("Enter the position: "))
    if(pos2>=1 and pos2<=9):
        if board[pos2] == '':
            board[pos2] = marker2
            u2.append(pos2)
        else:
            print("You can't select this position")
    else:
        print("You can't select this position")
    display_board(board)

def tic(board, win, u1, u2, ter, marker1, marker2):
    c = random.randint(1,2)
    if c == 1:
        print("Player 1 is selected to play first")
    else:
        print("Player 2 is selected to play first")
    n = 0
    while(1):
        if(ter == 0):
            if c == 1:
                user_1(marker1, u1, board)
                n+=1
            else:
                user_2(marker2, u2, board)
                n+=1
            for item in win:
                b1 = set(u1)
                b2 = set(u2)
                w = set(item)
                if w.issubset(b1):
                    print("Player 1 is a winner")
                    ter = 1
                elif w.issubset(b2):
                    print("Player 2 is a winner")
                    ter = 1
                elif n == 9:
                    print("Game is Tied")
                    replay(board, win, u1, u2, ter, marker1, marker2)
                else:
                    continue
        else:
            replay(board, win, u1, u2, ter, marker1, marker2)
        
        if(ter == 0):
            if c == 1:
                user_2(marker2, u2, board)
                n+=1
            else:
                user_1(marker1, u1, board)
                n+=1
            for item in win:
                b1 = set(u1)
                b2 = set(u2)
                w = set(item)
                if w.issubset(b1):
                    print("Player 1 is a winner")
                    ter = 1
                elif w.issubset(b2):
                    print("Player 2 is a winner")
                    ter = 1
                elif n == 9:
                    print("Game is Tied")
                    replay(board, win, u1, u2, ter, marker1, marker2)
                else:
                    continue
        else:
            replay(board, win, u1, u2, ter, marker1, marker2)

def replay(board, win, u1, u2, ter, marker1, marker2):
    ans = input("Are you ready to play Y/N: ")
    if(ans == 'y' or ans == 'Y'):
        board = ['','','','','','','','','','','']
        win = [[1,2,3],[1,4,7],[1,5,9],[2,5,8],[3,6,9],[3,5,7],[4,5,6],[7,8,9]]
        u1 = []
        u2 = []
        marker1 = input("Enter the marker X/O: ")
        ter = 0
        if marker1 == 'x' or marker1 == 'X':
            marker2 = 'O'
        else:
            marker2 = 'X'
        tic(board, win, u1, u2, ter, marker1, marker2)
    else:
        sys.exit()
        
board = ['','','','','','','','','','','']
win = [[1,2,3],[1,4,7],[1,5,9],[2,5,8],[3,6,9],[3,5,7],[4,5,6],[7,8,9]]
u1 = []
u2 = []
marker1 = input("Enter the marker X/O: ")
ter = 0
if marker1 == 'x' or marker1 == 'X':
    marker2 = 'O'
else:
    marker2 = 'X'

tic(board, win, u1, u2, ter, marker1, marker2)
