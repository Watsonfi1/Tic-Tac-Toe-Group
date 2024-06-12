# // Functions \\
def singleplayer():
    print("singleplayer")
def multiplayer():
    print("Alright, you have selected multiplayer.")
    while True:
        readinstructions = input("Do you want the instructions (Yes/No)? ").lower()
        if readinstructions == "yes":
             print("\nInstructions: Tic-Tac-Toe is a simple kids game, the aim of the game is to get 3 of your shapes in a row on the 3x3 board. When it is your turn to make a move, you will have to enter the number of the \nsquare you want to place your shape in. You are not able to put your shape in a square that is already taken. Each round, 5 points will be awarded to the winning player.\n\nMultiplayer: If the multiplayer gamemode has been selected, both players will be asked for their name at the start. They will enter how many rounds they want to play. After both names have been selected, each player will be asked if they want to start or not. If both players wish to start, there will be a 50/50 chance, if one player wants to start, they will, and if both players do not want to start it will be a 50/50 chance.\n\nSingleplayer: If the single player gamemode has been selected, the player will be playing against a computer generating moves. The player will also enter how many rounds they want to play. They will be asked for their name, and then the player will always start.")
             break
        else:
             break

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

print("* * * * * * * * * * * * * \n*       *       *       *\n*  {}   *  {}   *       *\n*       *       *       *\n* * * * * * * * * * * * *",
      "\n*       *       *       *\n*       *       *       *\n*       *       *       *\n* * * * * * * * * * * * * \n*       *       *       *",
      "\n*       *       *       *\n*       *       *       *\n* * * * * * * * * * * * * \n")
intro()
