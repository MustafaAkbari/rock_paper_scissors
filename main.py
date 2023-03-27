from starter_codes import rock, paper, scissors
import random

choice_list = [rock, paper, scissors]
computer_choice = random.choice(choice_list)


# print(computer_choice)

def game():
    print("Welcome to rock, paper, scissors game!")
    print("What do you choose? 0 for rock, 1 for paper and 2 for scissors: ")
    user_choice = input("Rock, Peper, Scissors: ")
    if user_choice == "0" and computer_choice == rock:
        print(f"Your choice:\n{rock}\nComputer choice:\n{rock}")
        print("No Winner!")
    elif user_choice == "0" and computer_choice == paper:
        print(f"Your choice:\n{rock}\nComputer choice:\n{paper}")
        print("You lose!")
    elif user_choice == "0" and computer_choice == scissors:
        print(f"Your choice:\n{rock}\nComputer choice:\n{scissors}")
        print("You Win!")
    elif user_choice == "1" and computer_choice == rock:
        print(f"Your choice:\n{paper}\nComputer choice:\n{rock}")
        print("You Win!")
    elif user_choice == "1" and computer_choice == paper:
        print(f"Your choice:\n{paper}\nComputer choice:\n{paper}")
        print("No Winner!")
    elif user_choice == "1" and computer_choice == scissors:
        print(f"Your choice:\n{paper}\nComputer choice:\n{scissors}")
        print("You lose!")
    elif user_choice == "2" and computer_choice == rock:
        print(f"Your choice:\n{scissors}\nComputer choice:\n{rock}")
        print("You lose!")
    elif user_choice == "2" and computer_choice == paper:
        print(f"Your choice:\n{scissors}\nComputer choice:\n{paper}")
        print("You Win!")
    elif user_choice == "2" and computer_choice == scissors:
        print(f"Your choice:\n{scissors}\nComputer choice:\n{scissors}")
        print("No Winner!")
    else:
        print("Please type a valid choice!")


game()

