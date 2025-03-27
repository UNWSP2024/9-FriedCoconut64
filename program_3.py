def sum_numbers_from_file():
    number_series = ('2', '4', '67', '23', '84', '123')

    with open('numbers.txt', 'w') as average_number_file:
        average_number_file.write('\n'.join(number_series))

    total = 0
    try:
        with open('numbers.txt', 'r') as contents:
            for line in contents:
                total += int(line.strip())
        print('The total of all the numbers in numbers.txt is', total)
    except IOError:
        print('There was an error reading', average_number_file)
    except ValueError:
        print('There was an error with the numbers in', average_number_file)

if __name__ == '__main__':
    sum_numbers_from_file()
# Program #3, Donovan Thompson 3/26/2025
