#!/usr/bin/env python3
# Created By: Jack Turcotte
# Date: May 1st, 2025

# Celsius to fahrenheit


def fahrenheit():

    # Get temperature in celsius from user
    temp_c = input("Enter your temperature in Celsius: ")

    # Try converting string to int
    try:

        # Calculate temperature in fahrenheit
        temp_c = float(temp_c)
        temp_f = 9 / 5 * temp_c + 32
        print("your temperature in fahrenheit is", temp_f)
    except:

        # Warn user that they entered a string
        print("Enter a number next time, you entered:", temp_c)


def main():
    print("Welcome to fahrenheit program")
    fahrenheit()


if __name__ == "__main__":
    main()
