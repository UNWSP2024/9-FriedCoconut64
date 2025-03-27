import os.path
import random
from random import randint


def random_number_file():
    while True:
        print('This program writes a series of random numbers to a file.')
        try:
            number_of_numbers = int(input("Please select a number from 1-1000 to write to the file:"))
            if number_of_numbers > 1000 or number_of_numbers <= 0:
                print("The number entered must be above 0 below 1000")
                continue
            break
        except ValueError:
            print('Invalid input. Please enter a valid integer')
    try:
        with open('numbers.txt', 'w') as numbers_file:
            for i in range(number_of_numbers):
                numbers_file.write(str(randint(1,500)) + '\n')
    except IOError:
        print("An error occurred trying to write to the file", numbers_file)
    except ValueError:
        print('There was an error with the amount of numbers in', numbers_file)
        print("The number of numbers must be above 0 and below 1000")

    try:
        with open('numbers.txt', 'r') as numbers_file:
            contents = numbers_file.read()
            print(contents)
    except IOError:
        print('There was an error trying to read the file.')


if __name__ == '__main__':
    random_number_file()
# Program #2, Donovan Thompson 3/26/2025
