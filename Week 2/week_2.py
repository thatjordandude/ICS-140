tax = .07125
com = float(input('Enter cost of meal: '))
pretax = com * tax
total = com+pretax

Grad1=total*.15
Grad2=total*.2
Grad3=total*.25

print('The tax today was {}. Your total meal cost is {}. Purchase tax of {}.'.format(tax, total, pretax))

print('Tip suggestions: 15%: {}, 20%: {}, 25%: {}'.format(Grad1, Grad2, Grad3))
