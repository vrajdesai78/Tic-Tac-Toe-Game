import sys
import random
import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) 
rate = engine.getProperty('rate')
engine.setProperty('rate',120)


def display_board(board):
    print(' '+board[7]+' | '+board[8]+' | '+board[9]+' ')
    print('-----------')
    print(' '+board[4]+' | '+board[5]+' | '+board[6]+' ')
    print('-----------')
    print(' '+board[1]+' | '+board[2]+' | '+board[3]+' ')


def user_1(marker1, u1, board, u1_name):
    engine.say(f'{u1_name} Enter your position ')
    engine.runAndWait()
    pos1 = int(input("Enter the position: "))
    if(pos1>=1 and pos1<=9):
        if board[pos1] == '':
            board[pos1] = marker1
            u1.append(pos1)
        else:
            print("You can't select this position")
            engine.say("You can't select this position")
            engine.runAndWait()
    else:
        print("You can't select this position")
        engine.say("You can't select this position")
        engine.runAndWait()
    display_board(board)


def user_2(marker2, u2, board, u2_name):
    engine.say(f'{u2_name} Enter your position ')
    engine.runAndWait()
    pos2 = int(input("Enter the position: "))
    if(pos2>=1 and pos2<=9):
        if board[pos2] == '':
            board[pos2] = marker2
            u2.append(pos2)
        else:
            print("You can't select this position")
            engine.say("You can't select this position")
            engine.runAndWait()
    else:
        print("You can't select this position")
        engine.say("You can't select this position")
        engine.runAndWait()
    display_board(board)

def tic(board, win, u1, u2, ter, marker1, marker2, u1_name, u2_name):
    c = random.randint(1,2)
    if c == 1:
        print(f"{u1_name} is selected to play first")
        engine.say(f"{u1_name} is selected to play first")
        engine.runAndWait()
    else:
        print(f"{u2_name} is selected to play first")
        engine.say(f"{u2_name} is selected to play first")
        engine.runAndWait()
    n = 0
    while(1):
        if(ter == 0):
            if c == 1:
                user_1(marker1, u1, board, u1_name)
                n+=1
            else:
                user_2(marker2, u2, board, u2_name)
                n+=1
            for item in win:
                b1 = set(u1)
                b2 = set(u2)
                w = set(item)
                if w.issubset(b1):
                    print(f"Congratulations {u1_name}! you are winner ")
                    engine.say(f"Congratulations {u1_name}! you are winner ")
                    engine.runAndWait()
                    ter = 1
                elif w.issubset(b2):
                    print(f"Congratulations {u2_name}! you are winner ")
                    engine.say(f"Congratulations {u2_name}! you are winner ")
                    engine.runAndWait()
                    ter = 1
                elif n == 9:
                    print("Game is Tied")
                    engine.say('Oops! Game is Tied')
                    engine.runAndWait()
                    replay(board, win, u1, u2, ter, marker1, marker2, u1_name, u2_name)
                else:
                    continue
        else:
            replay(board, win, u1, u2, ter, marker1, marker2, u1_name, u2_name)
        
        if(ter == 0):
            if c == 1:
                user_2(marker2, u2, board, u2_name)
                n+=1
            else:
                user_1(marker1, u1, board, u1_name)
                n+=1
            for item in win:
                b1 = set(u1)
                b2 = set(u2)
                w = set(item)
                if w.issubset(b1):
                    print(f"Congratulations {u1_name}! you are winner ")
                    engine.say(f"Congratulations {u1_name}! you are winner ")
                    engine.runAndWait()
                    ter = 1
                elif w.issubset(b2):
                    print(f"Congratulations {u2_name}! you are winner ")
                    engine.say(f"Congratulations {u2_name}! you are winner ")
                    engine.runAndWait()
                    ter = 1
                elif n == 9:
                    print("Game is Tied")
                    engine.say("Oops! Game is Tied")
                    engine.runAndWait()
                    replay(board, win, u1, u2, ter, marker1, marker2, u1_name, u2_name)
                else:
                    continue
        else:
            replay(board, win, u1, u2, ter, marker1, marker2, u1_name, u2_name)

def replay(board, win, u1, u2, ter, marker1, marker2, u1_name, u2_name):
    engine.say("Are you ready to play again Yes or No")
    engine.runAndWait()
    ans = input("Are you ready to play again Y/N: ")
    if(ans == 'y' or ans == 'Y'):
        board = ['','','','','','','','','','','']
        win = [[1,2,3],[1,4,7],[1,5,9],[2,5,8],[3,6,9],[3,5,7],[4,5,6],[7,8,9]]
        u1 = []
        u2 = []
        engine.say("Enter the name of first user")
        engine.runAndWait()
        u1_name = input("Enter the name of first user: ")

        engine.say(f"Enter the marker X, or, O for {u1_name}")
        engine.runAndWait()
        marker1 = input("Enter the marker X/O: ")

        engine.say("Enter the name of second user ")
        engine.runAndWait()
        u2_name = input("Enter the name of second user: ")
        ter = 0
        if marker1 == 'x' or marker1 == 'X':
            marker2 = 'O'
        else:
            marker2 = 'X'
        tic(board, win, u1, u2, ter, marker1, marker2, u1_name, u2_name)
    else:
        sys.exit()
        
board = ['','','','','','','','','','','']
win = [[1,2,3],[1,4,7],[1,5,9],[2,5,8],[3,6,9],[3,5,7],[4,5,6],[7,8,9]]
u1 = []
u2 = []

engine.say("Enter the name of first user")
engine.runAndWait()
u1_name = input("Enter the name of first user: ")

engine.say(f"Enter the marker X, or, O for {u1_name}")
engine.runAndWait()
marker1 = input("Enter the marker X/O: ")

engine.say("Enter the name of second user ")
engine.runAndWait()
u2_name = input("Enter the name of second user: ")
ter = 0
if marker1 == 'x' or marker1 == 'X':
    marker2 = 'O'
else:
    marker2 = 'X'

tic(board, win, u1, u2, ter, marker1, marker2, u1_name, u2_name)
