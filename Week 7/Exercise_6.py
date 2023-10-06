import random
r = random.randint(1,10)
guess = None
count = 0
while guess != r:
    guess=int(input('Enter your guess: '))
    count += 1
    if guess > r:
        print('Too High! guess a lower number')
    elif guess < r:
        print('Too low! guess a higher number')
print('Correct! the secret number was {}! You guessed a total of {} times.'.format(r, count))