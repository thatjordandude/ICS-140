
def traingle_area(height, base):
    area = (base * height) / 2
    return area

def traingle_parimeter(side1, side2, side3):
    perimeter = side1+side2+side3
    return perimeter
def main():
    side1 = float(input('Enter Side1 length: '))
    side2 = float(input('Enter Side2 length: '))
    side3 = float(input('Enter Side3 length: '))
    print('Triangle parimeter is:',traingle_parimeter(side1,side2,side3))
    base_identify = input('Which side was the base? 1, 2, or 3: ')
    if base_identify == '1':
        base = side1
    if base_identify == '2':
        base = side2
    if base_identify == '3':
        base = side3
    height = float(input('What is the height of the traingle: '))
    print('The area of the traingle is:', traingle_area(height, base))
main()