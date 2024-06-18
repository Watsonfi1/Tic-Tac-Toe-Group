# // Functions \\
def WinLoseScore ():
    global guesses
    for i in possible_wins:
        if currentboard == possible_wins[1][i]:
            print("")  

def singleplayer():
    print("singleplayer")
def multiplayer():
    global name1
    global name2
    global guesses
    global NUMBERS
    global bp
    gamecomplete = False
    
    while True:
        startingturn = input("Who do you want to start ( {} or {} )? ".format(name1, name2)).lower()
        if startingturn == name1.lower():
            turns = 1
            break
        elif startingturn == name2.lower():
            turns = -1
            break
        else:
            print("That wasn't a valid name.")
    while gamecomplete == False:
        if turns == 1:
            # X Starts
                while True:
                    moves = input("{}, where do you want your piece to go? ".format(name1))
                    if moves not in guesses and moves in NUMBERS:
                        guesses.append(moves)
                        try:
                            moves = int(moves)
                            moves -= 1
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
                turns *= -1
                gamecomplete = WinLoseScore()
        if turns == -1:
            # O Starts
                while True:
                    moves = input("{}, where do you want your piece to go? ".format(name2))
                    if moves not in guesses and moves in NUMBERS:
                        guesses.append(moves)
                        try:
                            moves = int(moves)
                            moves -= 1
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
                turns *= -1
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
            singleplayer()
            break
        else:
            print("That wasn't an option, try singleplayer or multiplayer.")  

# // Variables \\

NUMBERS = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
guesses = []
possible_wins = [["Player X wins"], ["Player O wins"]]
play = True
startingplayer = 1
bp = ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ']

# // Main Code \\
intro()

while play == True:
    play = playagain()
