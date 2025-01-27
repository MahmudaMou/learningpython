import random
options = ["rock","paper","scissor"]
playing = True
while playing:
    computer = random.choice(options)
    player = None
    while player not in options:
        player = input("Enter a choice(rock/paper/scissor):").lower()

    print(f"Your choice: {player}")
    print(f"Computer:{computer}")
    if player == computer:
        print("it's a tie!")
    elif player == "rock" and computer == "scissor":
        print("Congratulations!you win!")
    elif player == "paper" and computer == "rock":
        print("Congratulations!you win!")
    elif player == "scissor" and computer == "paper":
        print("Congratulations!you win!")
    else:
        print("You lose!")
    if not input("Do you want to play again(y/n): ").lower() == "y":
        playing = False
print("Thanks for playing")



