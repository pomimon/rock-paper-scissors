import random


def main():


# random.choice to select a random string in options, list options
# comp_input and user_input
# if elif else statements
#   - tie game (user_input == computer input)
#   - rock beats scissors, paper covers rock,
#   - scissors cuts paper

# to-do later
# while loop to keep playing

    print("Let's play rock, paper, scissors")

    user_choice = input("Enter your choice: ")
    options = ["rock", "paper", "scissors"]
    comp_choice = random.choice(options)
    print(f"you chose {user_choice}, computer chose {comp_choice}")

    if user_choice == comp_choice:
        print("it's a tie")
    elif user_choice == "rock" and comp_choice == "paper":
        print("you lose, paper cover's rock")
    elif user_choice == "paper" and comp_choice == "rock":
        print("you won! paper cover's rock")

    elif user_choice == "scissors" and comp_choice == "paper":
        print("you won! scissors cut's paper")
    elif user_choice == "paper" and comp_choice == "scissors":
        print("you lose, scissors cut's paper")

    elif user_choice == "rock" and comp_choice == "scissors":
        print("you won! rock smashes scissors")
    elif user_choice == "scissors" and comp_choice == "rock":
        print("you lose! rock smashes scissors")













if __name__ == "__main__":
    main()
