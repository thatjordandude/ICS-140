class Rect:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area_of_rect(self):
        area = self.length * self.width
        return area


rect1length = float(input("Enter length of 1st rectangle: "))
rect1width = float(input("Enter width of 1st rectangle: "))

rect2length = float(input("Enter length of 2nd rectangle: "))
rect2width = float(input("Enter width of 2nd rectangle: "))

rect1 = Rect(rect1length, rect1width)
rect2 = Rect(rect2length, rect2width)

if rect1.area_of_rect() < rect2.area_of_rect():
    print('Rectangle 2 is bigger')
elif rect1.area_of_rect() == rect2.area_of_rect():
    print('The rectangles are the same size')
else:
    print('Rectangle 1 is bigger')