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












if __name__ == "__main__":
    main()
