
def get_roulette_color(number):
    if number == 0:
        return 'GREEN'
    if number % 2 == 0:
        if number < 11:
            return 'BLACK'
        elif number < 19:
            return 'RED'
        elif number < 29:
            return 'BLACK'
        elif number < 37:
            return 'RED'
    else:
        if number < 11:
            return 'RED'
        elif number < 19:
            return 'BLACK'
        elif number < 29:
            return 'RED'
        elif number < 37:
            return 'BLACK'
        
def get_high_low(number):
    if number == 0:
        return 'ZERO'
    elif number < 19:
        return 'LOW'
    elif number <= 36:
        return 'HIGH'
    
def get_odd_even(number):
    if number == 0:
        return 'ZERO'
    elif number % 2 == 0:
        return 'EVEN'
    else:
        return 'ODD'
    
def win():
    bet = input('Enter your bet').upper()
    if bet.isdigit():
            
    elif bet == 'ODD' or 'EVEN':

    elif bet ==  'LOW' or 'HIGH':

