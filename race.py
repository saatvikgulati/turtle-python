import turtle
import time
from random import randint
window=turtle.Screen()
window.bgcolor("brown")
tur=turtle.Pen()
tur.speed(0)
tur.up()
stamp_size=20
square_size=15
finish_line=200
tur.color("black")
tur.shape("square")
tur.shapesize(square_size/stamp_size)
tur.up()
for i in range(10):
    tur.setpos(finish_line,(150-(i*square_size*2)))
    tur.stamp()
for j in range(10):
    tur.setpos(finish_line+square_size,((150-square_size)-(j*square_size*2)))
    tur.stamp()
tur.hideturtle()
p1=turtle.Pen()
p2=turtle.Pen()
p3=turtle.Pen()
p4=turtle.Pen()
d=turtle.Pen()
p1.shape("turtle")
p2.shape("turtle")
p3.shape("turtle")
p4.shape("turtle")
p1.speed(0)
p1.up()
p2.speed(0)
p2.up()
p3.speed(0)
p3.up()
p4.speed(0)
p4.up()
d.speed(0)
d.up()
d.setpos(-300,-190)
d.down()
d.left(90)
d.forward(400)
d.right(90)
d.up()
d.hideturtle()
p1.setpos(-300,0)
p2.setpos(-300,-50)
p3.setpos(-300,50)
p4.setpos(-300,100)
d.setpos(-300,0)
d.down()
d.forward(2000)
d.up()
d.setpos(-300,-50)
d.down()
d.forward(2000)
d.up()
d.setpos(-300,50)
d.down()
d.forward(2000)
d.up()
d.setpos(-300,100)
d.down()
d.forward(2000)
d.up()
for i in range(145):
    p2.forward(randint(1,5))
    p1.forward(randint(1,5))
    p3.forward(randint(1,5))
    p4.forward(randint(1,5))
