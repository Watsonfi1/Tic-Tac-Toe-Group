import random
import time

# // Functions \\
def WinLoseScore():
    global guesses
    global score1
    global score2
    global startingplayer
    global bp
    num1 = [0,1]
    num2 = [0,1,2]
    number = [0,1,2,3,4,5,6,7,8]
    tie = 0
    Xwin = ["X", "X", "X"]
    Owin = ["O", "O", "O"]
    diagonals = [slice(0,9,4), slice(2,7,2)]
    rows = [slice(0, 3), slice(3,6), slice(6,9)]
    colums = [slice(0,7,3), slice(1,8,3), slice(2,9,3)]
    currentboard = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
    for i in number:
        if bp[i] == " X":
            currentboard.pop(i)
            currentboard.insert(i, "X")
        if bp[i] == " O":
            currentboard.pop(i)
            currentboard.insert(i, "O")
        if currentboard[i] != ' ':
            tie += 1
    for i in num1:
        if currentboard[diagonals[i]] == Xwin:
            score1 += 1
            print("{} won! {} has {} score and {} has {} score.".format(name1, name1, score1, name2, score2))
            return True
        elif currentboard[diagonals[i]] == Owin:
            score2 += 1
            print("{} won! {} has {} score and {} has {} score.".format(name2, name2, score2, name1, score1))
            return True
    for i in num2:
        if currentboard[rows[i]] == Xwin:
            score1 += 1
            print("{} won! {} has {} score and {} has {} score.".format(name1, name1, score1, name2, score2))
            return True
        elif currentboard[rows[i]] == Owin:
            score2 += 1
            print("{} won! {} has {} score and {} has {} score.".format(name2, name2, score2, name1, score1))
            return True
        if currentboard[colums[i]] == Xwin:
            score1 += 1
            print("{} won! {} has {} score and {} has {} score.".format(name1, name1, score1, name2, score2))
            return True
        elif currentboard[colums[i]] == Owin:
            score2 += 1
            print("{} won! {} has {} score and {} has {} score.".format(name2, name2, score2, name1, score1))
            return True
        if tie == 9:
            score1 += 0.5
            score2 += 0.5
            print("You drew! {} has {} score and {} has {} score.".format(name2, score2, name1, score1))
            return True
    return False
       

def singleplayer():
    # Globals variables
    global guesses
    global NUMBERS
    global bp
    global name2
    name2 = "Computer"
    gamecomplete = False

    # Sets the starting player
    while True:
        startingturn = input("{}, do you want to start (yes/no)? ".format(name1)).lower()
        if startingturn == "yes".lower():
            turns = -1
            break
        elif startingturn == "no".lower():
            turns = 1
            break
        else:
            print("That was an invalid answer.")
    while gamecomplete == False:
        turns *= -1
        if turns == 1:
            # Human player starts
                while True:
                    # Asks where the human player wants their piece to go
                    moves = input("{}, where do you want your piece to go? ".format(name1))
                    if moves not in guesses and moves in NUMBERS:
                        guesses.append(moves)
                        try:
                            moves = int(moves) - 1
                            break
                        except:
                            print("That is not a valid number.")
                    else:
                        print("That is an invalid number, or has already been used.")
                # Adds the moves to the variable, then prints the board
                bp.pop(moves)
                bp.insert(moves, " X")
                print("      *       *       \n {}   *  {}   *  {}   \n      *       *       \n* * * * * * * * * * * ".format(bp[0], bp[1], bp[2]),
                "\n      *       *       \n {}   *  {}   *  {}   \n      *       *       \n* * * * * * * * * * * \n      *       *       ".format(bp[3], bp[4], bp[5]),
                "\n {}   *  {}   *  {}   \n      *       *       \n".format(bp[6], bp[7], bp[8]))
                gamecomplete = WinLoseScore()
        if turns == -1:
            # Computer player starts
                # Generates a random move for the computer
                while True:
                    moves = random.choice(NUMBERS)
                    if moves not in guesses and moves in NUMBERS:
                        guesses.append(moves)
                        moves = int(moves) - 1
                        break
                # Adds the moves to the variable, then prints the board
                bp.pop(moves)
                bp.insert(moves, " O")
                print("Alright, it's my turn! - Computer\n")
                time.sleep(2)
                print("      *       *       \n {}   *  {}   *  {}   \n      *       *       \n* * * * * * * * * * * ".format(bp[0], bp[1], bp[2]),
                "\n      *       *       \n {}   *  {}   *  {}   \n      *       *       \n* * * * * * * * * * * \n      *       *       ".format(bp[3], bp[4], bp[5]),
                "\n {}   *  {}   *  {}   \n      *       *       \n".format(bp[6], bp[7], bp[8]))
                gamecomplete = WinLoseScore()

def multiplayer():
    # Globals variables
    global name1
    global name2
    global guesses
    global NUMBERS
    global bp
    global startingplayer
    gamecomplete = False
    
    # Makes the chosen starting player start.
    while True:
        startingturn = input("Who do you want to start ( {} or {} )? ".format(name1, name2)).lower()
        if startingturn == name1.lower():
            turns = -1
            break
        elif startingturn == name2.lower():
            turns = 1
            break
        else:
            print("That wasn't a valid name.")
    while gamecomplete == False:
        turns *= -1
        if turns == 1:
            # X Starts
                while True:
                    moves = input("{}, where do you want your piece to go? ".format(name1))
                    if moves not in guesses and moves in NUMBERS:
                        guesses.append(moves)
                        try:
                            moves = int(moves) - 1
                            break
                        except:
                            print("That is not a valid number.")
                    else:
                        print("That is an invalid number, or has already been used.")
                bp.pop(moves)
                bp.insert(moves, " X")
                print("      *       *       \n {}   *  {}   *  {}   \n      *       *       \n* * * * * * * * * * * ".format(bp[0], bp[1], bp[2]),
                "\n      *       *       \n {}   *  {}   *  {}   \n      *       *       \n* * * * * * * * * * * \n      *       *       ".format(bp[3], bp[4], bp[5]),
                "\n {}   *  {}   *  {}   \n      *       *       \n".format(bp[6], bp[7], bp[8]))
                gamecomplete = WinLoseScore()
        if turns == -1:
            # O Starts
                while True:
                    moves = input("{}, where do you want your piece to go? ".format(name2))
                    if moves not in guesses and moves in NUMBERS:
                        guesses.append(moves)
                        try:
                            moves = int(moves) - 1
                            break
                        except:
                            print("That is not a valid number.")
                    else:
                        print("That is an invalid number, or has already been used.")
                bp.pop(moves)
                bp.insert(moves, " O")
                print("      *       *       \n {}   *  {}   *  {}   \n      *       *       \n* * * * * * * * * * * ".format(bp[0], bp[1], bp[2]),
                "\n      *       *       \n {}   *  {}   *  {}   \n      *       *       \n* * * * * * * * * * * \n      *       *       ".format(bp[3], bp[4], bp[5]),
                "\n {}   *  {}   *  {}   \n      *       *       \n".format(bp[6], bp[7], bp[8]))
                gamecomplete = WinLoseScore()

def intro():
    global name1
    global name2
    print("Welcome to Tic-Tac-Toe!")
    while True:
        gamemode = input("Would you like to play singleplayer or multiplayer? ").lower()
        if gamemode == "multiplayer":
            name1 = input("What is player 1's name? ")
            name1 = name1.lower().capitalize()
            name2 = input("What is player 2's name? ")
            name2 = name2.lower().capitalize()
            multiplayer()
            break
        elif gamemode == "singleplayer":
            name1 = input("What is your name? ")
            name1 = name1.lower().capitalize()
            singleplayer()
            break
        else:
            print("That wasn't an option, try singleplayer or multiplayer.")

def playagain():
    while True:
        again = input("Would you like to play again? (yes or no) ").lower()
        if again == "yes":
            return True
        elif again =="no":
            print("Thank you for playing!")
            return False
        else:
            print("That's not an option!")

# // Variables \\

NUMBERS = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
guesses = []
possible_wins = [["Player X wins"], ["Player O wins"]]
play = True
startingplayer = 1
bp = ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ']
score1 = 0
score2 = 0


# // Main Code \\
while play == True:
    intro()
    play = playagain()



