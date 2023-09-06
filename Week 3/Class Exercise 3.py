def miles_per_gal(miles, gallons):
    
    mpg=miles / gallons
    print(f'Your MPG is:{mpg: .2f}')

miles=float(input('Miles: '))
gallons=float(input('Gallons: '))

miles_per_gal(miles, gallons)