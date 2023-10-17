organism = int(input('Enter number of starting organisms: '))
increase = float(input('Enter average daily increase percentage: '))
days = int(input('Enter number of days to populate: '))
percentage = increase *.01
increased = 0
print('Starting number of oragnism:', organism)
print('Average daily increase:', percentage)
print('Number of days to populate:', days)
print('\n')
print('Day          Population')
for day in range((days+1)-days, days+1):
    print(day,'          ',organism)
    increased *= percentage
    organism += increase