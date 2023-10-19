# Inputs
hourly_rate = float(input('Enter the hourly rate: '))
hours_worked = float(input('Enter the amount of hours worked: '))

# normal wages function
def normal_wage(hourly_rate, hours_worked): 
    if hours_worked <= 40:
        total = hourly_rate * hours_worked
    else:
        total = hourly_rate * 40
    return total

# overtime calculation                
def overtime_calc(hourly_rate, hours_worked):
    if hours_worked <= 40:
        return 'Regular Hours: {:.2f}\nRegular pay: ${:.2f}\nNo overtime pay was made'.format(hours_worked, normal_wage(hourly_rate, hours_worked))
    else:
        overtime_hours = hours_worked - 40
        regular_hours = hours_worked - overtime_hours
        overtime_hourly = overtime_hours * 1.5
        overtime_pay = overtime_hourly * hourly_rate
        total_pay = normal_wage(hourly_rate, regular_hours) + overtime_pay
        return 'Regular hours worked: {:.2f}\nRegular pay: ${:.2f}\nOvertime Hours: {:.2f}\nOvertime Pay: ${:.2f}\nTotal pay: ${:.2f}'.format(regular_hours, normal_wage(hourly_rate, regular_hours), overtime_hours, overtime_pay, total_pay)

if hours_worked <= 0:
    print('Please enter a value greater than 0')
elif hours_worked > 40: 
    print(overtime_calc(hourly_rate, hours_worked))
else:
    print(normal_wage(hourly_rate, hours_worked))
    print('Regular Hours: {:.2f}\nRegular pay: ${:.2f}\nNo overtime pay was made'.format(hours_worked, normal_wage(hourly_rate, hours_worked)))
