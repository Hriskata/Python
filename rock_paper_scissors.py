import random

while True:
    choises = ["rock", "paper", "scissors"]

    computer = random.choice(choises)
    player = None

    while player not in choises:
        player = input("pick rock, paper or scissors? : ").lower()

    print("computer: " + computer)
    print("player: " + player)
    if player == computer:
        print("Tie!")
    elif player == "rock":
        if computer == "scissors":
            print("You win!")
        else:
            print("You lose!")
    elif player == "paper":
        if computer == "rock":
            print("You win!")
        else:
            print("You lose!")
    elif player == "scissors":
        if computer == "paper":
            print("You win!")
        else:
            print("You lose!")
    play_again = input("Play again? (yes/no): ").lower()

    if play_again != "yes":
        break
print("Bye!")
