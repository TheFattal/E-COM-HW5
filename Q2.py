import random

# Generate a random number between 1 and 100
target_number: int = random.randint(1, 100)
print("Welcome to the Number Guessing Game!")
print("I've chosen a number between 1 and 100. Try to guess it!")

num_guesses: int = 0
while True:
    guess = int(input("Enter your guess (between 1 and 100): "))
    num_guesses += 1
    if guess < target_number:
        print("Too low! Try guessing higher.")
    elif guess > target_number:
        print("Too high! Try guessing lower.")
    else:
        print(f"BINGO! You guessed the number {target_number} correctly in {num_guesses} guesses!")
        play_again = input("Do you wish to continue playing? (YES or NO): ").strip().lower()
        if play_again == 'NO' or play_again == 'no':
            print("Thank you for playing!")
            break
