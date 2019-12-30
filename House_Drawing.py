'''
Name: Armaan Merchant
Program description: this program draws a crazy cool house with a legendary turtle named after the american painter Bob Ross
'''

import turtle
import math

#creates the backgroud
canvas = turtle.Screen()

#set the background colour
canvas.bgcolor('SkyBlue')

#Creates the turtle Bob Ross!
bobross = turtle.Turtle()


#A function to create an isosceles triangle with angles 30, 30 and 120. the parameters distance and colour affect the triangles size and colour
def triangle(distance,colour):
    bobross.fillcolor(colour)
    bobross.begin_fill()
    bobross.left(30)
    bobross.forward(distance)
    bobross.right(60)
    bobross.forward(distance)
    bobross.right(150)
    bobross.forward((3**(1/2))*distance)
    bobross.right(180)
    bobross.end_fill()


#a function that creates rectanges with parameters x and y being the length of the sides
def rectangle(x,y):
    bobross.forward(x)
    bobross.right(90)
    bobross.forward(y)
    bobross.right(90)
    bobross.forward(x)
    bobross.right(90)
    bobross.forward(y)
    bobross.right(90)

#an adaptation of the rectangle function with 1 parameter, x, to make a square window
def window(x):
    bobross.begin_fill()
    bobross.forward(x)
    bobross.right(90)
    bobross.forward(x)
    bobross.right(90)
    bobross.forward(x)
    bobross.right(90)
    bobross.forward(x)
    bobross.right(90)
    bobross.end_fill()

    #this part creates the '+' in the window
    bobross.forward(0.5*x)
    bobross.right(90)
    bobross.forward(x)
    bobross.right(90)
    bobross.forward(0.5*x)
    bobross.right(90)
    bobross.forward(0.5*x)
    bobross.right(90)
    bobross.forward(x)

#This part creates a large square in green that represents the grass in the picture
bobross.fillcolor('YellowGreen')
bobross.begin_fill()
bobross.penup()
bobross.goto(-500,0)
bobross.pendown()
rectangle(1000,500)
bobross.end_fill()

#This creates the rectangular part of the house and colours it lavender
bobross.fillcolor('Lavender')
bobross.begin_fill()
bobross.penup()
bobross.goto(-175,100)
bobross.pendown()
rectangle(350,250)
bobross.end_fill()

#creates the brown door at the base of the house
bobross.fillcolor('SaddleBrown')
bobross.begin_fill()
bobross.penup()
bobross.goto(-25,-50)
bobross.pendown()
rectangle(50,100)
bobross.end_fill()

#roof
bobross.penup()
bobross.goto(-210,100)
bobross.pendown()
triangle(250,'maroon')

#creates the window on the left of the house with the window function and colours it yellow
bobross.fillcolor('LemonChiffon')
bobross.penup()
bobross.goto(-125,-50)
bobross.pendown()
window(60)

#creates the window to the right of the house with the window() function and colours it yellow
bobross.fillcolor('LemonChiffon')
bobross.penup()
bobross.goto(75,-50)
bobross.pendown()
window(60)

#creates the doorknob on the door at the base of the house and colours it white
bobross.penup()
bobross.goto(-17,-100)
bobross.pendown()
bobross.fillcolor('white')
bobross.begin_fill()
bobross.circle(5)
bobross.end_fill()

#creates the door for the balcony and colours it brown
bobross.fillcolor('SaddleBrown')
bobross.begin_fill()
bobross.penup()
bobross.goto(20,75)
bobross.pendown()
rectangle(50,100)
bobross.end_fill()

#creates the window with the window() function for the balcony and colours it yellow
bobross.fillcolor('LemonChiffon')
bobross.penup()
bobross.goto(-50,60)
bobross.pendown()
window(50)

#Creates the grill for the balcony using a for loop to loop the rectangle() function to keep creating rectangles for a given range
#creates the rail of the balcony with the rectangle() function and colours it golden
bobross.penup()
bobross.goto(-60,30)
bobross.pendown()
for grill in range(15):
    rectangle(10,55)
    bobross.forward(10)
    grill += 1
bobross.goto(-60,30)
bobross.fillcolor('DarkGoldenrod')
bobross.begin_fill()
rectangle(150,10)
bobross.end_fill()


