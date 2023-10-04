import random
from time import sleep

bet = int(input('ENTER YOUR BET!!!!: '))

if bet == 0:
    print('0 lands on green')
elif bet <= 10:
    if bet % 2 == 0:
        print(bet, 'lands on black')
    else:
        print(bet, 'lands on red')
elif bet <= 18:
    if bet % 2 == 0:
        print(bet, 'lands on red')
    else:
        print(bet, 'lands on black')
elif bet <= 28:
    if bet % 2 == 0:
        print(bet, 'lands on black')
    else:
        print(bet, 'lands on red')
elif bet <= 36:
    if bet % 2 == 0:
        print(bet, 'lands on red')
    else:
        print(bet, 'lands on black')     
elif bet > 36:
    print('Not valid bet')   

r = random.randint(1,36)
print('spinning..........')
sleep(1)
print('spinning..........')
sleep(1)
print('ball landed on {} your bet was {}...'.format(r, bet))
if bet == r:
    print('YOU WIN!')
else:
    print('YOU LOSE')