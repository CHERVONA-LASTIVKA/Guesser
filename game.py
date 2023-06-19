import random

def guess_number():
    lower_bound = 1
    upper_bound = 100
    target_number = random.randint(lower_bound, upper_bound)
    attempts = 0

    print("Welcome to the Guess the Number Game!")
    print(f"I'm thinking of a number between {lower_bound} and {upper_bound}. Can you guess it?")

    while True:
        guess = input("Enter your guess (or 'q' to quit): ")
        
        if guess.lower() == 'q':
            print("Thanks for playing. Goodbye!")
            break
        
        try:
            guess = int(guess)
            
            if guess < lower_bound or guess > upper_bound:
                print("Invalid guess. The number is between 1 and 100.")
                continue
            
            attempts += 1
            
            if guess < target_number:
                print("Too low! Try again.")
            elif guess > target_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                break
        
        except ValueError:
            print("Invalid input. Please enter a valid number.")


# Run the game
guess_number()
