number = 2
l = []
while True:
    try:
        number = float(input('Enter number to add to total, enter letter to end: '))    
        l.append(number)
    except ValueError:
        break

total = 0
for num in l:
    total += num
mean = total/len(l)
if len(l) > 0:
    print('Your sum is:', total)
    print('Your average is:', mean)
else:
    print('No valid numbers entered.')