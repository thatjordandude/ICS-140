import turtle

t = turtle.Turtle()
forward = 10
t.speed(15)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
for i in range(400):
    t.forward(forward)
    t.right(90)
    t.color(colors[i%6])
    forward += 10

turtle.done()