# Import the random module
import random

# Create a list of options that has rock, paper, and scissors
options = ["rock", "paper", "scissors"]

# Create a score variable and set it to zero
score = {"wins": 0, "losses": 0, "ties": 0}

# Create a variable to count the number of rounds played
rounds_played = 0

while True:
    # Get the user's choice
    user_choice = input("Enter rock, paper, or scissors (or 'quit' to stop playing): ").lower()

    # Check if the user wants to quit
    if user_choice == "quit":
        break

    # Check if the user's choice is valid
    if user_choice not in options:
        print("Invalid choice. Please try again.")
        continue

    # Get the computer's choice
    computer_choice = random.choice(options)

    # Determine the winner
    if user_choice == computer_choice:
        result = "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        result = "win"
    else:
        result = "loss"

    # Update the score
    if result == "win":
        score["wins"] += 1
    elif result == "loss":
        score["losses"] += 1
    else:
        score["ties"] += 1

    # Update the rounds played
    rounds_played += 1

    # Print the result and the score
    print(f"You chose {user_choice}, the computer chose {computer_choice}.")
    if result == "win":
        print("You win!")
    elif result == "loss":
        print("You lose.")
    else:
        print("It's a tie.")
    print(f"Score: {score['wins']} wins, {score['losses']} losses, {score['ties']} ties.")
    print(f"Rounds played: {rounds_played}\n")