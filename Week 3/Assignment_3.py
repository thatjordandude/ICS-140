principal = float(input('Enter Principal Amount: '))
interest_rate = float(input('Enter Interest Amount as a Decimal: '))
number_of_compounds = float(input('Enter number of compounds in months: '))
time = float(input('Enter number years: '))
result = principal * (1 + (interest_rate / number_of_compounds))**(number_of_compounds * time)
print('After {} years, your account will be ${:.2f}'.format(int(time), result))