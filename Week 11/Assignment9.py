


def county_tax(total_sales):
    countytax = total_sales * .025
    return countytax

def state_tax(total_sales):
    statetax = total_sales * .05
    return statetax

def total_tax(statetax , countytax):
    totaltax = statetax + countytax
    return totaltax

def main():
    total_sales = float(input('Enter total number of sales: '))
    print('The state tax is: ${:.2f}'.format(state_tax(total_sales)))
    print('The county tax is: ${:.2f}'.format(county_tax(total_sales)))
    print('The total tax is: ${:.2f}'.format
          (total_tax(state_tax(total_sales), county_tax(total_sales))))
main()