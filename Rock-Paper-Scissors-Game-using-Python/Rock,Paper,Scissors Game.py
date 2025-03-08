import random  # Import the random module to generate random choices for the computer

# Print the rules of the game
print("Winning rules of the game ROCK PAPER SCISSORS are:\n"
      + "Rock vs Paper -> Paper wins \n"
      + "Rock vs Scissors -> Rock wins \n"
      + "Paper vs Scissors -> Scissors wins \n")

# Initialize scores for the user and computer
user_score = 0
computer_score = 0
rounds = 5  # Set the number of rounds to play

# Loop through the number of rounds
for round_number in range(1, rounds + 1):
    print(f"\nRound {round_number}:")  # Indicate the current round
    print("Enter your choice \n 1 - Rock \n 2 - Paper \n 3 - Scissors \n")  # Prompt user for input
    choice = int(input("Enter your choice: "))  # Get user input
    
    # Validate user input
    while choice > 3 or choice < 1:
        choice = int(input('Enter a valid choice please ☺: '))  # Ask for valid input if out of range
    
    # Map user choice to name
    if choice == 1:
        choice_name = 'Rock'
    elif choice == 2:
        choice_name = 'Paper'
    else:
        choice_name = 'Scissors'
    
    print('User  choice is:', choice_name)  # Display user's choice
    print("Now it's Computer's Turn...")  # Indicate it's the computer's turn
    
    # Generate computer's choice
    comp_choice = random.randint(1, 3)  # Randomly select a number between 1 and 3
    
    # Map computer choice to name
    if comp_choice == 1:
        comp_choice_name = 'Rock'
    elif comp_choice == 2:
        comp_choice_name = 'Paper'
    else:
        comp_choice_name = 'Scissors'

    print("Computer choice is:", comp_choice_name)  # Display computer's choice
    print(choice_name, 'vs', comp_choice_name)  # Show the choices made
    
    # Determine the result of the round
    if choice == comp_choice:
        result = "DRAW"  # It's a tie
        print("<== It's a tie! ==>")
    elif (choice == 1 and comp_choice == 2) or (choice == 2 and comp_choice == 1):
        result = 'Paper'  # Computer wins
        computer_score += 1  # Increment computer's score
        print("<== Computer wins! ==>")
    elif (choice == 1 and comp_choice == 3) or (choice == 3 and comp_choice == 1):
        result = 'Rock'  # User wins
        user_score += 1  # Increment user's score
        print("<== User wins! ==>")
    elif (choice == 2 and comp_choice == 3) or (choice == 3 and comp_choice == 2):
        result = 'Scissors'  # User wins
        user_score += 1  # Increment user's score
        print("<== User wins! ==>")

# Final score after all rounds
print("\nFinal Scores:")  # Indicate final scores
print("User  Score:", user_score)  # Display user's score
print("Computer Score:", computer_score)  # Display computer's score

# Determine and display the overall winner
if user_score > computer_score:
    print("<== User is the overall winner! ==>")
elif computer_score > user_score:
    print("<== Computer is the overall winner! ==>")
else:
    print("<== Overall result is a tie! ==>")

print("Thanks for playing!")  # Thank the user for playing
