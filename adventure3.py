#text based adventure game for CIP2021 final project

#beginning
def start():
    print("You are in a deserted house.")
    print("There are two doors. One to your left and one to your right.")
    print("Which one do you choose? (l or r)")

    answer = input(">").lower()

    if "l" in answer:
        empty_room()
    elif "r" in answer:
        riddle_room()
    else:
        print("Very well then.")
        game_over("Very well then.")
        

def game_over(self):
    print("Game Over!")
    play_again()

def play_again():
    print("Do you want to play again? (y or n)")
    answer = input(">").lower()

    if "y" in answer:
        start()
    else:
        exit()

#first room on left
def empty_room():
    print("The room before you appears perfectly normal.")
    print("Do you:")
    print("1). Walk straight to the other door?")
    print("2). Ransack the room looking for treasure?")
    

    answer = input(">")

    if answer == "1":
        print("You triggered a poison dart. You're dead.")
        game_over("You're dead.")
        play_again()
    elif answer == "2":
        print("You rifle through every drawer in the room, finding a key.")
        print("It fits the door and you move on to the next room.")
        witch_room()
    else:
        print("How hard is it to type 1 or 2?")
        game_over("how hard?")

#second room on left
def witch_room():
    print("There is a beautiful woman in the room.")
    print("Do you:")
    print("1). Back out of the room and hope she doesn't see you?")
    print("2). You smile and begin talking.")

    answer = input(">")

    if answer == "1":
        print("There is a bright flash of light. You're dead.")
        game_over("you're dead")
    elif answer == "2":
        print("Your friendliness pays off and she gives you a key for the next room.")
        treasure_room()
    else:
        print("How hard is it to type 1 or 2?")
        game_over("how hard")

#final room
def treasure_room():
    print("You enter a large room with bookcases along each wall.")
    print("One wall also has a huge fireplace.")
    print("There are overstuffed chairs and wooden tables throughout as well.")
    print("In the center of the room is a closed chest.")
    print("Do you:")
    print("1). Open the chest?")
    print("2). Browse the books?")

    answer = input(">")

    if answer == "1":
        print("The chest opens easily.")
        print("It is filled with gold and jewels.")
        print("Congratulations! You win the game!")
        play_again()
    elif answer == "2":
        print("You see the books are either by your favorite author or on subjects you want to read about.")
        print("Congratulations! You win the game!")
        play_again()

#first room on right
def riddle_room():
    print("There is a framed canvas handing from the ceiling.")
    print("One the canvas is printed")
    print("What goes on four feet in the morning,")
    print("two feet at noon,")
    print("and three feet in the evening?")
    print("Do you:")
    print("1). Answer the riddle correctly? (man)")
    print("2). Try to go around the canvas?")

    answer = input(">")

    if answer == "1":
        print("The canvas rises and clears the way for you to exit.")
        beast_room()
    elif answer == "2":
        print("The floor opens and you fall.")
        print("You die.")
        print("Eventually.")
        game_over("eventually")
    else:
        print("How hard is it to type 1 or 2?")
        game_over("how hard")

#second room on right
def beast_room():
    print("You enter a dimly lit room.")
    print("You can just make out a low growl.")
    print("Do you:")
    print("1). Run to the other door?")
    print("2). Try to calm the beast down?")

    answer = input(">")

    if answer == "1":
        print("The beast pounces. You're dead.")
        game_over("your dead")
    elif answer == "2":
        print("You make friends and go through the door together.")
        treasure_room()
    else:
        print("How hard is it to type 1 or 2?")
        game_over("how hard")



start()

