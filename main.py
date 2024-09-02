import random

'''
1 for snake
-1 for water
0 for gun
'''

# The computer randomly selects one of the three options
computer = random.choice([-1, 0, 1])

# Prompt the user to enter their choice
yourstring = input("Enter your choice from snake, water or gun : ")

# Dictionary to convert choices to their numeric values
yourdictionary = {"snake": 1, "water": -1, "gun": 0}

# Dictionary to convert numeric values back to choices
reversedictionary = {1: "snake", -1: "water", 0: "gun"}

# Convert the user's choice from string to its numeric value
you = yourdictionary[yourstring]

# Print out both the user's choice and the computer's choice
print(f"You choose: {reversedictionary[you]}\nComputer choose: {reversedictionary[computer]}")

# Determine the result of the game
if computer == you:
    # If both choices are the same, it's a draw
    print("What a game! It's a draw!")
else:
    # Check various conditions to determine if the user wins or loses
    if computer == -1 and you == 1:
        # Computer chose water and user chose snake: user wins
        print("You win!")

    elif computer == -1 and you == 0:
        # Computer chose water and user chose gun: user loses
        print("You lose!")

    elif computer == 1 and you == -1:
        # Computer chose snake and user chose water: user loses
        print("You lose!")

    elif computer == 1 and you == 0:
        # Computer chose snake and user chose gun: user wins
        print("You win!")

    elif computer == 0 and you == -1:
        # Computer chose gun and user chose water: user wins
        print("You win!")

    elif computer == 0 and you == 1:
        # Computer chose gun and user chose snake: user loses
        print("You lose!")

    else:
        # This block should never be reached; it handles unexpected cases
        print("Something went wrong!")