'''
Name: Armaan Merchant

program descripton: using turtle to draw a face with a hat
'''


import turtle
wn = turtle.Screen()
wn.bgcolor("lightblue")
draw = turtle.Turtle()
draw.color("beige")
draw.pensize(4)

#general face shape
draw.up()
draw.goto(-200, -200)
draw.down()
draw.begin_fill()
draw.setx(200)
draw.sety(200)
draw.setx(-200)
draw.sety(-200)
draw.end_fill()

#left eye
draw.color("white")
draw.up()
draw.begin_fill()
draw.goto(-90, 90)
draw.down()
draw.forward(40)
draw.left(90)
draw.forward(40)
draw.left(90)
draw.forward(40)
draw.left(90)
draw.forward(40)
draw.end_fill()

#right eye
draw.up()
draw.begin_fill()
draw.goto(75, 127)
draw.down()
draw.forward(40)
draw.left(90)
draw.forward(40)
draw.left(90)
draw.forward(40)
draw.left(90)
draw.forward(40)
draw.end_fill()

#left eyebrow
draw.up()
draw.color("black")
draw.goto(-100, 140)
draw.down()
draw.setx(-50)

#right eyebrow
draw.up()
draw.goto(70, 140)
draw.down()
draw.setx(120)

draw.up()
draw.goto(0, 50)
draw.down()
draw.goto(50,0)
draw.goto(0, 0)

#mouth
draw.up()
draw.begin_fill()
draw.goto(-75, -150)
draw.down()
draw.goto(-75, -75)
draw.goto(75, -75)
draw.goto(75, -150)
draw.goto(-75, -150)
draw.end_fill()

#hat
draw.color('maroon')
draw.up()
draw.goto(250, 200)
draw.down()
draw.begin_fill()
draw.goto(-210, 200)
draw.goto(-210, 300)
draw.goto(0, 300)
draw.goto(100, 250)
draw.goto(300, 250)
draw.goto(300, 200)
draw.end_fill()

#left pupil
draw.up()
draw.color("black")
draw.goto(-60, 110)
draw.begin_fill()
draw.forward(10)
draw.left(90)
draw.forward(10)
draw.left(90)
draw.forward(10)
draw.left(90)
draw.forward(10)
draw.end_fill()

#right pupil
draw.up()
draw.goto(105, 95)
draw.down()
draw.begin_fill()
draw.forward(10)
draw.left(90)
draw.forward(10)
draw.left(90)
draw.forward(10)
draw.left(90)
draw.forward(10)
draw.end_fill()

#get the turtle out of sight
draw.up()
draw.goto(-400,-400)

#end program
