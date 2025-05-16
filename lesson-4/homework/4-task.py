import random
while True:
    think_num = random.randint(1, 100)
    attempts = 10       #maximum number of attempts
    print("\nWelcome to the Number Guessing Game.")
    print("I'm thinking of a number between 1 and 100.")
    
    while attempts > 0:
        try:
            guess = int(input(f"\nAttempts left: {attempts}. Enter your guess: "))
        except ValueError:
            print("Please only enter number: ")
            continue
        if guess > think_num:
            print("Too high!")
        elif guess < think_num:
            print("Too low!")
        else:
            print("You guessed it right!")
            break
        attempts -= 1

    if attempts == 0:
        print("😞 You lost. Want to play again?")
    response = input("Type 'Y', 'YES', 'y', 'yes', or 'ok' to play again: ")
    if response.lower() not in ['y', 'yes', 'ok']:
        print("Thanks for playing!")
        break
        