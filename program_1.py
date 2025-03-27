import os.path
#I found the os import online when looking for solution for the file path in line 12
import random


def count_file_lines():
    names = 'John', 'Lucas', 'Adam', 'Stephanie', 'Grace', 'Troy', 'Clare'
    names_file = open('names.txt', 'w')
    names_file.write(', '.join(names) + '\n')
    names_file.close()
    try:
        with open(os.path.abspath('names.txt'), 'r') as file:
            name_count = 0
            for line in file:
                name_count = len(line.split(', '))
        print('In the count_file_lines function,', name_count, 'names were found')
    except IOError:
        print("An error occurred trying to read the file", names_file)
    except ValueError:
        print('There was an error with the amount of names in', names_file)




if __name__ == '__main__':
    count_file_lines()
# Program #1, Donovan Thompson 3/26/2025
