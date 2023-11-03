import math
# def circle_measurements(radius):
#     area = math.pi*radius**2
#     circum = math.pi*(radius*2)
#     return area, circum
# # print(circle_measurements(15))
# area, circumference = circle_measurements(5)
# print(area, circumference)

# def calculations(num1, num2):
#     total_sum = num1 + num2
#     average = total_sum / 2
#     return total_sum, average
# print(calculations(4, 2))
# total , mean = calculations(1, 3)

# import hello.py
# hello.world()
# import circle.py
# circumference, area = circle.circle_measurements(10)

def add(a, b):
    print( '{} + {} ='.format(a, b), a + b)

def subtract(a, b):
    print( '{} - {} ='.format(a, b),a - b)

def multiply(a, b):
    print( '{} * {} ='.format(a, b),a * b)

def divide(a, b):
    quotient = a // b
    remainder = a % b
    print( '{} / {} ='.format(a, b), quotient, 'wtih remainder', remainder)

def main():
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    add(a, b)
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    subtract(a, b)
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    multiply(a, b)
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    divide(a, b)
main()
