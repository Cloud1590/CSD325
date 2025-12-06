''' 
Daniel Vance
December 5, 2025
Assignment: Module 1 - Beer Countdown (CSD325 Advanced Python)
Purpose: Ask the user for a starting number of bottles and count down using a loop.
'''

# Function: beer_countdown
# Takes the starting bottle count and prints the lyrics of the
# beer countdown song until the count reaches zero.

def beer_countdown(starting_bottle_count):

    # Keep track of how many bottles are left
    bottles_remaining = starting_bottle_count

    # Continue looping as long as there is at least one bottle
    while bottles_remaining > 0:

        # If more than one bottle left, use plural form
        if bottles_remaining > 1:
            print(f"{bottles_remaining} bottles of beer on the wall, "
                  f"{bottles_remaining} bottles of beer.")
        
        # Otherwise, print the singular version (1 bottle)
        else:
            print("1 bottle of beer on the wall, 1 bottle of beer.")

        # Decrease the number of bottles for the next loop
        bottles_remaining -= 1


# Function: main
# Handles user input and calls the countdown function.

def main():

    # Ask the user how many bottles to begin with
    # Validate input so non-integer values (e.g. "abc" or "\\") are rejected
    while True:
        user_input = input("How many bottles of beer are on the wall? ")
        try:
            starting_value = int(user_input)
            if starting_value <= 0:
                print("Please enter a positive integer greater than 0.")
                continue
            break
        except ValueError:
            print("That's not a valid integer. Please enter a whole number.")

    # Call the countdown function with the user's number
    beer_countdown(starting_value)

    # Final message once the countdown ends
    print("Time to buy more beer!")


# Run the main program
if __name__ == "__main__":
    main()