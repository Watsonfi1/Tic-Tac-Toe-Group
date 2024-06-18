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
    global startingplayer
    global guesses
    gamecomplete = False
    while True:
        if startingplayer > 1:
            while gamecomplete == False:
                while True:
                    moves = input("{}, where do you want your first piece to go? ".format(name1))
                    if moves not in guesses:
                        try:
                            int(moves)
                            break
                        except:
                            print("That is not a valid number.")
                guesses.append(moves)
                BP.pop(moves)
                BP.insert(" X", moves)



            #X starts
        if startingplayer < 1:
            #O starts

        #do before ending
        startingplayer *= -1

def intro():
    global name1
    global name2
    print("Welcome to Tic-Tac-Toe!")
    while True:
        gamemode = input("Would you like to play singleplayer or multiplayer? ").lower()
        if gamemode == "multiplayer":
            name1 = input("What is player 1's name? ")
            name2 = input("What is player 2's name? ")
            multiplayer()
            break
        elif gamemode == "singleplayer":
            name1 = input("What is your name? ")
            singleplayer()
            break
        else:
            print("That wasn't an option, try singleplayer or multiplayer.")  
def playagain():
    while True:
        again = input("Would you like to play again?").lower:
        if again == "yes":
            

# // Variables \\
guesses = []
possible_wins = [["Player X wins"], ["Player O wins"]]
play = True
startingplayer = 1
BP = ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ']
# // Main Code \\
#Abreviations for Top left, Top Right, ect
TL = TM = TR = ML = MM = MR = BL = BM = BR = "  "

print("      *       *       \n {}   *  {}   *  {}   \n      *       *       \n* * * * * * * * * * * ".format(TL,TM,TR),
      "\n      *       *       \n {}   *  {}   *  {}   \n      *       *       \n* * * * * * * * * * * \n      *       *       ".format(ML,MM,MR),
      "\n {}   *  {}   *  {}   \n      *       *       \n".format(BL,BM,BR))

intro()

while play = True:
    play = playagain()
