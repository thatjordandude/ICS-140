import turtle
import time
from tkinter import CENTER

# shapes
def draw_rectangle(width, height):
    t = turtle.Turtle()
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)

def draw_star(size):
    t = turtle.Turtle()
    for _ in range(5):
        t.forward(size)
        t.right(144)

def draw_triangle(side_length):
    t = turtle.Turtle()
    for _ in range(3):
        t.forward(side_length)
        t.left(120)

print('Choose a Star, Rectangle, or Triangle to be drawn!')
chosen_shape = input('Your choice: ')

# Validate the input
while chosen_shape.lower() not in ['star', 'rectangle', 'triangle']:
    print('Invalid choice. Please choose "star," "rectangle," or "triangle."')
    chosen_shape = input('Your choice: ')

# future Jordan: add sizes and color inputs? or randommness input? #########################

# added suspense
f=turtle.Turtle()
f.hideturtle()
f.write('Ready?', align=CENTER, font=('Arial', 32, 'bold'))
time.sleep(1)
f.clear()
f.write('Draw!', align=CENTER, font=('Arial', 32, 'bold'))
time.sleep(1)
f.clear()

# if statements
if chosen_shape.lower() == 'star':
    draw_star(100)
elif chosen_shape.lower() == 'rectangle':
    draw_rectangle(100, 50)
elif chosen_shape.lower() == 'triangle':
    draw_triangle(100)

# end click 
time.sleep(3)
f.write('Click to exit', align=CENTER, font=('Arial', 32, 'bold'))
turtle.exitonclick()