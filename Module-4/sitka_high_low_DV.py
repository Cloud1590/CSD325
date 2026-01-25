"""
Author: Daniel Vance
Course: CSD-325
Assignment: Module 4

Description:
This program allows the user to view Sitka weather data from 2018.
The user may choose to view high temperatures, low temperatures,
or exit the program. The program loops until the user chooses to exit.
"""

import csv
import sys
from datetime import datetime
from matplotlib import pyplot as plt


FILENAME = 'sitka_weather_2018_simple.csv'


def load_weather_data():
    """Load dates, highs, and lows from the CSV file."""
    dates = []
    highs = []
    lows = []

    with open(FILENAME) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        for row in reader:
            current_date = datetime.strptime(row[2], '%Y-%m-%d')
            dates.append(current_date)

            highs.append(int(row[5]))
            lows.append(int(row[6]))

    return dates, highs, lows


def plot_temperatures(dates, temperatures, color, title):
    """Plot temperature data using matplotlib."""
    fig, ax = plt.subplots()
    ax.plot(dates, temperatures, c=color)

    plt.title(title, fontsize=20)
    plt.xlabel('', fontsize=14)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=14)
    plt.tick_params(axis='both', which='major', labelsize=12)

    plt.show()


def display_menu():
    """Display the program menu."""
    print("\nSitka Weather Menu")
    print("1. View High Temperatures")
    print("2. View Low Temperatures")
    print("3. Exit")


def main():
    """Main program loop."""
    dates, highs, lows = load_weather_data()

    while True:
        display_menu()
        choice = input("Select an option (1-3): ")

        if choice == '1':
            plot_temperatures(
                dates,
                highs,
                'red',
                "Daily High Temperatures - 2018"
            )
        elif choice == '2':
            plot_temperatures(
                dates,
                lows,
                'blue',
                "Daily Low Temperatures - 2018"
            )
        elif choice == '3':
            print("Thank you for using the Sitka Weather program. Goodbye!")
            sys.exit()
        else:
            print("Invalid selection. Please choose 1, 2, or 3.")


if __name__ == "__main__":
    main()
