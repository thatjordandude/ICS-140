

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31,
           37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
def is_prime(number: int):
    if number <= 1:
        return False
    elif number < 100:
        if number in primes:
            return True
    elif number > 100: 
        numbers = [int(digit) for digit in str(number)]
        last_digit = numbers[-1]
        sum_of_digits = sum(numbers)
        if last_digit in [0, 2, 4, 5, 6, 8]:
            return False
        elif sum_of_digits % 3 == 0:
            return False
        return True
    
        

number = int(input('Enter number to check if prime: '))
if is_prime(number):
    print('{} is a prime number'.format(number))
else:
    print('{} is not a prime number'.format(number))