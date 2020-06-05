import time
import turtle 
from turtle import Turtle
from random import randint


#window setup
window =turtle.Screen()
window.title("RACING GAME")
turtle.bgcolor("forestgreen")
turtle.color("white")
turtle.speed(0)  #speed 0 means turn off animation as afast as possible 
turtle.penup()
turtle.setpos(-140,250)
turtle.write("RACING GAME!!!",font=("Century Gothic",30,"bold"))
turtle.penup()

#dirt
turtle.setpos(-400,-180)
turtle.color("brown")
turtle.begin_fill()
turtle.pendown()
turtle.forward(800)
turtle.right(90)
turtle.forward(300)
turtle.right(90)
turtle.forward(800)
turtle.right(90)
turtle.forward(300)
turtle.end_fill()

#finish line
stamp_size=20
square_size=15
finish_line=200
turtle.color("black")
turtle.shape("square")
turtle.shapesize(square_size/stamp_size)
turtle.penup()

for i in range(10):
    turtle.setpos(finish_line,(150-(i*15*2)))
    turtle.stamp()

for i in range(10):
    turtle.setpos(finish_line+16,(135-(i*15*2)))
    turtle.stamp()

player=[]
colors=["black","pink","magenta","blue","darkgreen"]
l=len(colors)
j=80
for i in range(3):
    player.append(turtle.Turtle())
    player[i].speed(0)
    player[i].color(colors[i%l])
    player[i].shape("turtle")
    player[i].up()
    player[i].setpos(-250,j-50)
    player[i].down()
    j=j-40

#user1
user1=Turtle()
user1.speed(0)
user1.color("white")
user1.shape("turtle")
user1.up()
user1.setpos(-250,120)

#player speeds
for i in range(3):
    player[i].speed(i+randint(1,10))

#player animation
for i in range(15):
    player[i%3].forward(10+10*i)


#user controls
def up():
    user1.sety(user1.ycor()+10)

def down():
    user1.sety(user1.ycor()-10)

def left():
    user1.forward(-10)

def right():
    user1.forward(10)


window.onkeypress(up, "Up")
window.onkeypress(down, "Down")
window.onkeypress(right, "Right")
window.onkeypress(left, "Left")
window.listen()
