import random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "stone" and computer_choice == "scissor") or \
         (user_choice == "scissor" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "stone"):
        return "You win!"
    else:
        return "Computer wins!"

choices = ["stone", "scissor", "paper"]
user_choice = input("Enter your choice (stone, scissor, paper): ")
computer_choice = random.choice(choices)

print("Computer chose:", computer_choice)
print(determine_winner(user_choice, computer_choice))