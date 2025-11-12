import random

def display_welcome():
    """Display welcome message and game rules"""
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print()

def select_difficulty():
    """Allow user to select difficulty level and return number of chances"""
    print("Please select the difficulty level:")
    print("1. Easy (10 chances)")
    print("2. Medium (5 chances)")
    print("3. Hard (3 chances)")
    
    while True:
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                print("\nGreat! You have selected the Easy difficulty level.")
                return 10
            elif choice == 2:
                print("\nGreat! You have selected the Medium difficulty level.")
                return 5
            elif choice == 3:
                print("\nGreat! You have selected the Hard difficulty level.")
                return 3
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter a number (1, 2, or 3).")

def play_game():
    """Main game logic"""
    display_welcome()
    chances = select_difficulty()
    
    # Generate random number between 1 and 100
    target_number = random.randint(1, 100)
    attempts = 0
    
    print("Let's start the game!\n")
    
    while attempts < chances:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            
            if guess == target_number:
                print(f"Congratulations! You guessed the correct number in {attempts} attempts.")
                return
            elif guess > target_number:
                print(f"Incorrect! The number is less than {guess}.")
            else:
                print(f"Incorrect! The number is greater than {guess}.")
            
            remaining = chances - attempts
            if remaining > 0:
                print()
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            print()
    
    print(f"\nGame Over! You've run out of chances.")
    print(f"The correct number was {target_number}.")

def main():
    """Main function to run the game"""
    play_game()
    
    # Ask if user wants to play again
    while True:
        play_again = input("\nWould you like to play again? (yes/no): ").lower()
        if play_again in ['yes', 'y']:
            print("\n" + "="*50 + "\n")
            play_game()
        elif play_again in ['no', 'n']:
            print("Thanks for playing! Goodbye!")
            break
        else:
            print("Please enter 'yes' or 'no'.")

if __name__ == "__main__":
    main()