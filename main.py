# // Functions \\
def singleplayer():
    print("singleplayer")
def multiplayer():
    print("multiplayer")
def gamerules():
     print("gamerules")

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

    gamerule = input("Do you know the rules to Tic-Tac-Toe? ").lower()
    if gamerule != "yes":
        gamerules()
                
         

# // Variables \\


# // Main Code \\

print("* * * * * * * * * * * * * \n*       *       *       *\n*  {}   *  {}   *       *\n*       *       *       *\n* * * * * * * * * * * * *",
      "\n*       *       *       *\n*       *       *       *\n*       *       *       *\n* * * * * * * * * * * * * \n*       *       *       *",
      "\n*       *       *       *\n*       *       *       *\n* * * * * * * * * * * * * \n")
intro()
