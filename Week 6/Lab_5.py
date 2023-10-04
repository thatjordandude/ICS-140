color1 = input('Enter first primary color: ').lower()
color2 = input('Enter second primary color: ').lower()
primes = ['red', 'blue', 'yellow']
if color1 ==  'red' or 'blue' and color2 == 'blue' or 'red':
    colormix = 'purple'
if color1 ==  'red' or 'yellow' and color2 == 'yellow' or 'red':
    colormix = 'orange'
if color1 ==  'blue' or 'yellow' and color2 == 'yellow' or 'blue':
    colormix = 'green'
if color1 not in primes or color2 not in primes:
    print('The acceptable input are red, blue and yellow. You entered {} and {}.'.format(color1, color2))
elif color1 == color2:
    print('You inputed the same colors')
else:
    print('{} and {} make {}'.format(color1, color2, colormix))