import random

def random_number_game():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    
    print("Welcome to the Random Number Guessing Game!")
    print("Try to guess the number between 1 and 100.")
    
    while True:
        try:
            guess = int(input("Enter your guess: "))
            if guess < 1 or guess > 100:
                print("Invalid input. Please enter a number between 1 and 100.")
                continue
            
            attempts += 1
            
            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    random_number_game()
