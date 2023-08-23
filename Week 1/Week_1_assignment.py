import turtle
t=turtle.Turtle()
t.hideturtle()
t.speed(20)
# robot head
t.penup()
t.setpos(0,-300)
t.pendown()
t.begin_fill()
t.color('gray')
t.circle(300)
t.end_fill()


# robot ear 1
earl = 180
earw = 75
t.penup()
t.color("orange")
t.setpos(280,0)
t.pendown()
t.begin_fill()
t.right(90)
t.forward(earl/2)
t.left(90)
t.forward(earw)
t.left(90)
t.forward(earl)
t.left(90)
t.forward(earw)
t.left(90)
t.forward(earl/2)
t.end_fill()

# robot ear 2

t.penup()
t.color("orange")
t.setpos(-280,0)
t.pendown()
t.begin_fill()
t.right(180)
t.forward(earl/2)
t.left(90)
t.forward(earw)
t.left(90)
t.forward(earl)
t.left(90)
t.forward(earw)
t.left(90)
t.forward(earl/2)
t.end_fill()



# eye 1
t.penup()
t.setpos(150,150)
t.pendown()
t.color('purple')
t.begin_fill()
t.circle(50)
t.end_fill()

# eye 2
t.penup()
t.setpos(-70,150)
t.pendown()
t.color('purple')
t.begin_fill()
t.circle(50)
t.end_fill()



# Nose
t.penup()
t.setpos(0,0)
t.color('red')
t.pendown()
t.begin_fill()
t.right(0)
t.forward(100)
t.right(120)
t.forward(60)
t.right(120)
t.forward(100)
t.end_fill()


# Mouth
t.penup()
t.setpos(-150, -200)
t.right(160)
t.color('black')
t.pendown()
t.forward(50)
t.right(90)
t.forward(50)
t.right(-90)
t.forward(50)
t.right(90)
t.forward(50)
t.right(-90)
t.forward(50)
t.right(90)
t.forward(50)
t.right(-90)
t.forward(50)
t.right(90)
t.forward(50)
t.right(-90)
t.forward(50)
turtle.done()