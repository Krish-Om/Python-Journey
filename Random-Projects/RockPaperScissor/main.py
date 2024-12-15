from random import randrange


def determine_winner(p, c):
    if p == c:
        return "Tie"
    if (p == "r" and c == "s") or (p == "p" and c == "r") or (p == "s" and c == "p"):
        return "Player wins"
    else:
        return "Computer wins"


def init_game():

    player = player_choice()
    computer = comp_choice()
    res = determine_winner(player, computer)
    print(res)


def player_choice():
    p_choice = input("Enter a choice: ").lower()
    if p_choice not in ["r", "s", "p"]:
        print("choose the correct choice: ")
        init_game()
    else:
        return p_choice


def comp_choice():
    randNum = randrange(100)
    if randNum >= 0 and randNum <= 40:
        return "r"
    elif randNum > 40 and randNum <= 60:
        return "p"
    else:
        return "s"


print("Welcome to the Rock(r) Paper(p) and Scissor(s) Game:")
playing = input("Do you want to start? ").lower()


if playing != "yes":
    print("Thank you for trying!")
    quit()
else:
    name = input("May I have your name? ")
    init_game()
