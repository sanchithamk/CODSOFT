import random

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'tie'
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return 'win'
    else:
        return 'lose'

def display_choices(user_choice, computer_choice):
    print(f"Your choice: {user_choice}")
    print(f"Computer's choice: {computer_choice}")

def display_result(result):
    if result == 'win':
        print("You win!")
    elif result == 'lose':
        print("You lose!")
    else:
        print("It's a tie!")

def main():
    user_score = 0
    computer_score = 0

    print("Welcome to Rock, Paper, Scissors!")

    while True:
        # Get user choice
        user_choice = input("Choose rock, paper, or scissors: ").lower()
        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue

        # Get computer choice
        computer_choice = get_computer_choice()

        # Determine the winner
        result = determine_winner(user_choice, computer_choice)

        # Display choices and result
        display_choices(user_choice, computer_choice)
        display_result(result)

        # Update scores
        if result == 'win':
            user_score += 1
        elif result == 'lose':
            computer_score += 1

        # Display scores
        print(f"Score - You: {user_score}, Computer: {computer_score}")

        # Ask if the user wants to play again
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

    print("Thanks for playing! Final Score - You: {}, Computer: {}".format(user_score, computer_score))

if __name__ == "__main__":
    main()
