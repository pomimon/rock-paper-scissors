import random


def read_choice(choices):
    choice = None

    while choice not in choices:
        choice = input("Pick one of {choices}: ".format(choices=", ".join(choices)))

    return choice


def determine_winner(user_choice, comp_choice):
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


def main():
    # random.choice to select a random string in options, list options
    # comp_input and user_input
    # if elif else statements
    #   - tie game (user_input == computer input)
    #   - rock beats scissors, paper covers rock,
    #   - scissors cuts paper
    # while loop to keep playing
    # user picks wrong choice option
    while True:
        print("Let's play rock, paper, scissors")

        # user_choice = input("Enter your choice: ")
        options = ["rock", "paper", "scissors"]
        user_choice = read_choice(options)
        comp_choice = random.choice(options)
        print(f"you chose {user_choice}, computer chose {comp_choice}")

        determine_winner(user_choice, comp_choice)

        play_again = input("Would you like to play again? (y/n): ")
        if play_again.lower() != "y":
            break


if __name__ == "__main__":
    main()
