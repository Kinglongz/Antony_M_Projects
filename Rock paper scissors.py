import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]
while True:
    user_choice = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    print("You chose: ", user_choice)
    if user_choice == "q":
        break

    if user_choice not in options:
        print("Wrong input. Try again or press Q to quit")
        continue

    random_number = random.randint(0, 2)
    # rock: 0, paper: 1, scissors: 2
    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")

    if user_choice == "rock" and computer_pick == "scissors":
        print("You won!")
        user_wins += 1
    elif user_choice == "rock" and computer_pick == "rock":
        print("You & Computer picked the same")
    elif user_choice == "scissors" and computer_pick == "scissors":
        print("You & Computer picked the same")
    elif user_choice == "paper" and computer_pick == "paper":
        print("You & Computer picked the same")
    elif user_choice == "paper" and computer_pick == "rock":
        print("You won!")
        user_wins += 1
    elif user_choice == "scissors" and computer_pick == "paper":
        print("You won!")
        user_wins += 1
    
    else:
        print("You lost!")
        computer_wins += 1

print("You won:", user_wins, "times.")
print("Computer won:", computer_wins, "times.")
print("Goodbye!")