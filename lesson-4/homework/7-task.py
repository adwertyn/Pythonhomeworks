import random   # Importing the random module to make random choices

# List of valid options
options = ["rock", "paper", "scissors"]
#Scores
computer_score = 0
user_score = 0

#Game intro
print("Welcome to Rock, Paper, Scissors game \nThe first to score 5 points wins.")
while computer_score < 5 and user_score < 5:
    user_choice = input("Enter your option: ").lower()
    if user_choice not in options:
        print("Invalid choice. Please try again.\n")
        continue    # Skip to the next iteration of the loop
    
    # Computer randomly selects rock, paper, or scissors
    computer_choice = random.choice(options)

    # Determine who wins the round
    if (computer_choice == "rock" and user_choice == 'scissors') or (computer_choice == "scissors" and user_choice == "paper") or (computer_choice == "paper" and user_choice == 'rock'):
        computer_score += 1
        print("Computer wins this round")
    
    elif (user_choice == "rock" and computer_choice == 'scissors') or (user_choice == "scissors" and computer_choice == "paper") or (user_choice == "paper" and computer_choice == 'rock'):
      user_score += 1
      print("You win this round")

    else:
        print("Draw")
    # Display current scores
    print(f"Scores -> You: {user_score} | Computer: {computer_score}\n")
    
# Display final result
if user_score == 5:
    print("You won the match")
else:
    print("Computer won the match. Good luck next time!")
    
    
