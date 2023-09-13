import turtle
size = int(input('Enter size of house: '))
roof_color = input('Enter color of roof: ')
house_color = input('Enter color of house: ')
t = turtle.Turtle()
t.color(house_color)
t.begin_fill()
for i in range(4):
    t.forward(size)
    t.right(90)
t.end_fill()
t.color(roof_color)
t.begin_fill()
t.left(60)
t.forward(size)
t.right(120)
t.forward(size)

t.end_fill()


turtle.done()