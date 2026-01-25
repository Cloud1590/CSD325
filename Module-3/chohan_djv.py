"""
Cho-Han Dice Game
Original author: Al Sweigart (al@inventwithpython.com)
Modified by: Daniel James Vance
Course: CSD-325
Assignment: Module 3

Description:
This program simulates the traditional Japanese dice game Cho-Han.
The player bets on whether the total of two dice will be even (CHO)
or odd (HAN).

Modifications made for this assignment:
1. Changed the input prompt to use the student's initials (djv:).
2. Changed the house fee from 10% to 12%.
3. Added a bonus rule that awards the player 10 mon if the dice
   total is 2 or 7.
4. Added user messaging to notify the player when the bonus is earned.
"""

import random
import sys

JAPANESE_NUMBERS = {
    1: 'ICHI',
    2: 'NI',
    3: 'SAN',
    4: 'SHI',
    5: 'GO',
    6: 'ROKU'
}

print('''Cho-Han Dice Game

In this traditional Japanese dice game, two dice are rolled.
The player must guess if the total is even (CHO) or odd (HAN).

BONUS NOTICE:
If the total of the dice is 2 or 7, the player receives a
10 mon bonus added to their purse.
''')

# Starting amount of money for the player
purse = 5000

# Main game loop
while True:
    print('You have', purse, 'mon. How much do you bet? (or QUIT)')

    # Validate bet input
    while True:
        pot = input('djv: ')

        if pot.upper() == 'QUIT':
            print('Thanks for playing!')
            sys.exit()
        elif not pot.isdecimal():
            print('Please enter a valid number.')
        elif int(pot) > purse:
            print('You do not have enough money to make that bet.')
        else:
            pot = int(pot)
            break

    # Roll the dice
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)

    print('\nThe dealer swirls the cup and rolls the dice.')
    print('CHO (even) or HAN (odd)?')

    # Validate CHO/HAN bet
    while True:
        bet = input('djv: ').upper()
        if bet != 'CHO' and bet != 'HAN':
            print('Please enter either CHO or HAN.')
        else:
            break

    # Reveal dice results
    print('\nThe dealer reveals:')
    print(' ', JAPANESE_NUMBERS[dice1], '-', JAPANESE_NUMBERS[dice2])
    print(' ', dice1, '-', dice2)

    total = dice1 + dice2
    roll_is_even = total % 2 == 0
    correct_bet = 'CHO' if roll_is_even else 'HAN'

    # Determine win or loss
    if bet == correct_bet:
        print('You won! You take', pot, 'mon.')
        purse += pot

        house_fee = pot * 12 // 100
        print('The house collects a', house_fee, 'mon fee.')
        purse -= house_fee
    else:
        print('You lost!')
        purse -= pot

    # Bonus condition
    if total == 2 or total == 7:
        print('BONUS! The dice total was', total,
              '- you receive a 10 mon bonus!')
        purse += 10

    # Check for game over
    if purse == 0:
        print('You have run out of money!')
        print('Thanks for playing!')
        sys.exit()
