import time
from tkinter import CENTER
import turtle
import random
pen = turtle.Pen()
pen.hideturtle()
pen.pensize(5)

# finish

pen.penup()
pen.setpos(-250,-250)
pen.pendown()
pen.forward(500)

# start

pen.penup()
pen.setpos(-250,250)
pen.pendown()
pen.forward(500)

# make turtles
colors = ['green', 'purple', 'yellow', 'red', 'blue']
turtle_list = []

for color in colors:
    new_turtle = turtle.Turtle()
    new_turtle.color(color)
    turtle_list.append(new_turtle)

# place turtles

distance = -240
for turtles in turtle_list:
    turtles.shape('turtle')
    turtles.setheading(90)
    turtles.penup()
    turtles.setpos(distance, -263)
    distance += 120

# Hype test

f=turtle.Turtle()
f.hideturtle()
f.write('Ready?', align=CENTER, font=('Arial', 32, 'bold'))
time.sleep(1)
f.clear()
f.write('3', align=CENTER, font=('Arial', 32, 'bold'))
time.sleep(1)
f.clear()
f.write('2', align=CENTER, font=('Arial', 32, 'bold'))
time.sleep(1)
f.clear()
f.write('1', align=CENTER, font=('Arial', 32, 'bold'))
time.sleep(1)
f.clear()
f.write('Go!', align=CENTER, font=('Arial', 32, 'bold'))
time.sleep(1)
f.clear()

# Winner

random = random.randint(1,25)
winner = None
while winner is None:
    for turtles in turtle_list:
        turtles.forward(random)
        if turtles.ycor() > 250:
            winner = turtles
            break
winner_color = winner.color()[0]
f.penup()
f.setpos(0,265)
f.color(winner_color)
f.write(f'Winner: {winner_color}', font=('Arial', 32, 'bold'))

turtle.mainloop()


