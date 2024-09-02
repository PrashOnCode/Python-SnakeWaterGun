import random

'''
1 for snake
-1 for water
0 for gun
'''

def get_computer_choice():
    """Randomly select computer's choice from the options."""
    return random.choice([-1, 0, 1])

def get_user_choice():
    """Get and validate the user's choice."""
    yourdictionary = {"snake": 1, "water": -1, "gun": 0}
    while True:
        # Prompt the user for their choice and convert it to lowercase
        yourstring = input("Enter your choice (snake, water, gun): ").lower()
        # Check if the user's choice is valid
        if yourstring in yourdictionary:
            return yourdictionary[yourstring]
        else:
            print("Invalid choice. Please choose from snake, water, or gun.")

def determine_winner(computer, user):
    """Determine the winner based on the choices of the computer and user."""
    if computer == user:
        # If both choices are the same, it's a draw
        return "draw"
    elif (computer == -1 and user == 1) or \
         (computer == 1 and user == 0) or \
         (computer == 0 and user == -1):
        # Conditions where the user wins
        return "user"
    else:
        # All other conditions mean the computer wins
        return "computer"

def print_result(user_choice, computer_choice, result):
    """Print the result of the game along with the choices and score."""
    reversedictionary = {1: "snake", -1: "water", 0: "gun"}
    # Display choices for both user and computer
    print(f"You chose: {reversedictionary[user_choice]}")
    print(f"Computer chose: {reversedictionary[computer_choice]}")
    
    # Display the result based on who won
    if result == "draw":
        print("It's a draw!")
    elif result == "user":
        print("You win!")
    else:
        print("You lose!")

def main():
    """Main function to run the game loop."""
    user_score = 0
    computer_score = 0
    
    while True:
        # Get choices from both computer and user
        computer_choice = get_computer_choice()
        user_choice = get_user_choice()
        # Determine who wins
        result = determine_winner(computer_choice, user_choice)
        
        # Print the result of the current game
        print_result(user_choice, computer_choice, result)
        
        # Update scores based on the result
        if result == "user":
            user_score += 1
        elif result == "computer":
            computer_score += 1
        
        # Display current scores
        print(f"Scores -> You: {user_score}, Computer: {computer_score}")
        
        # Ask if the user wants to play again
        replay = input("Do you want to play again? (yes/no): ").lower()
        if replay != "yes":
            print("Thanks for playing!")
            break

# Run the main function if the script is executed directly
if __name__ == "__main__":
    main()