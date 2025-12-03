def main ():
    difficulty = input("Difficult ou casual?: ")
    players = input("Multiplayer or Single-player?: ")

    if difficulty == "Difficulty":
        if players == "Multiplayer":
            recommend("Poker")
        else:
            recommend("Klondike") 
    else:
        if players == "Multiplayer":
            recommend("Hearts")
        else:
            recommend("Clock")     

def recommend(game):
    print("You might like", game)


main()        