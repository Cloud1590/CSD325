def beer_countdown(starting_bottles):
    bottles = starting_bottles

    while bottles > 0:
        if bottles > 1:
            print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer.")
            bottles -= 1
        else:
            print("1 bottle of beer on the wall, 1 bottle of beer.")
            bottles -= 1

    # Once the function is done, it returns control to the main program
    return


def main():
    # Ask the user how many bottles to start with
    starting = int(input("How many bottles of beer are on the wall? "))
    
    beer_countdown(starting)

    print("Time to buy more beer!")


# Run the main program
main()
