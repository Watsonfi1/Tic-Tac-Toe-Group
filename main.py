# // Functions \\
def singleplayer():
    print("singleplayer")
def multiplayer():
    print("multiplayer")

def intro():
    print("Welcome to Tic-Tac-Toe!")
    while True:
            gamemode = input("Would you like to play singleplayer or multiplayer? ").lower()
            if gamemode == "multiplayer":
                multiplayer()
                break
            elif gamemode == "singleplayer":
                singleplayer()
                break
            else:
                print("That wasn't an option, try singleplayer or multiplayer.")


# // Variables \\


# // Main Code \\
#Abreviations for Top left, Top Right, ect
TL = TM = TR = ML = MM = MR = BL = BM = BR = "  "
print("* * * * * * * * * * * * * \n*       *       *       *\n*  {}   *  {}   *  {}   *\n*       *       *       *\n* * * * * * * * * * * * *".format(TL,TM,TR),
      "\n*       *       *       *\n*  {}   *  {}   *  {}   *\n*       *       *       *\n* * * * * * * * * * * * * \n*       *       *       *".format(ML,MM,MR),
      "\n*  {}   *  {}   *  {}   *\n*       *       *       *\n* * * * * * * * * * * * * \n".format(BL,BM,BR))

