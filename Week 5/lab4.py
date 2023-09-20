import locale

locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

def discount_check(item_count):
    price_before_disc=item_count * 99
    if item_count <= 9:
        discount = .0
    elif item_count < 19:
        discount = .10
    elif item_count < 49:
        discount = .20
    elif item_count < 99:
        discount = .30
    else:
        discount = .40
    
    discount_amount = float(discount) * float(price_before_disc)
    final_price = price_before_disc - float(discount_amount)
    final_price = locale.format_string('%.2f', final_price, grouping=True)
    print('The discount is {:.0%}'.format(discount))
    print('The purchase amount is ${}'.format(final_price))

item_count = int(input('Enter number of software packages to purchase: '))
discount_check(item_count)