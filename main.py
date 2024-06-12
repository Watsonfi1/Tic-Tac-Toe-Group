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
intro()