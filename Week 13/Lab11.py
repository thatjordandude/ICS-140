def get_numbers():
    numbers = []
    print('Enter a letter to end inputs')
    number_input = 0
    while isinstance(number_input, int) or isinstance(number_input, float):
        try:
            number_input = float(input('Enter a number: '))
            numbers.append(number_input)
        except ValueError:
            break
    return numbers

def display_numbers(numbers):
    print('Numbers entered: ')
    for number in numbers:
        print(number)
    return 'total: {}'.format(sum(numbers))

def main():
    print(display_numbers(get_numbers()))

main()