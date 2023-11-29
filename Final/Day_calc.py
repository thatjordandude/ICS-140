
months_in_days = {
    'january': 31,
    'february': 28,  
    'march': 31,
    'april': 30,
    'may': 31,
    'june': 30,
    'july': 31,
    'august': 31,
    'september': 30,
    'october': 31,
    'november': 30,
    'december': 31
}

def check_valid_date(month, day):
    if day > months_in_days[month]:
        return False
    else:
        return True
    
def day_count(month, day):
    day_counter = 0
    for key in months_in_days:
        if key == month:
            break
        day_counter += months_in_days[key]
    return day_counter + day
        
    
def main():
    print('Month choices are:')
    for key in months_in_days:
        print(key)

    month = 'december'
    day = 300000
    while not check_valid_date(month, day):
        month = input('Choose a valid month: ').lower()
        day = int(input('Choose desired day of the month chosen: '))
    
    print('Your day of the year is:', day_count(month, day))

main()