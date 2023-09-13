
breakfast = float(input('Enter Cost of Breakfast: '))
lunch = float(input('Enter Cost of lunch: '))
dinner = float(input('Enter Cost of dinner: '))

total = breakfast + lunch + dinner
average = total/3

print('Your total cost was ${:.2f}'.format(total))
print('Your average cost was ${:.2f}'.format(average))