import turtle
import random
import math
import time
from playsound import playsound

window=turtle.Screen()
window.bgcolor("green")
window.title("Duck Shooting")
window.setup(width=1.0,height=1.0)

#draw border
border_drawer=turtle.Turtle()
border_drawer.up()
border_drawer.color("black")
border_drawer.speed(0)
border_drawer.setpos(-250,-250)
border_drawer.down()
border_drawer.pensize(3)
for i in range(4):
    border_drawer.forward(600)
    border_drawer.left(90)
border_drawer.hideturtle()

#create ducks
duckspeed=2
no_of_ducks=10
ducks=[]
color="white"
for i in range(no_of_ducks):
    ducks.append(turtle.Turtle())
    ducks[i].color(color)
    ducks[i].shape("turtle")
    ducks[i].setheading(-90)
    ducks[i].speed(0)
    ducks[i].up()
    x=random.randint(-200,200)
    y=random.randint(100,250)
    ducks[i].setpos(x,y)
ducks_state=['alive']*no_of_ducks

#setting score
score=0
score_pen=turtle.Turtle()
score_pen.speed(0)
score_pen.color("blue")
score_pen.up()
score_pen.hideturtle()
score_pen.setpos(-240,290)
score_pen.write("Score %s"%(score),font=("Century Gothic",15,"bold"))

#instructions
inst=turtle.Turtle()
inst.speed(0)
inst.color("red")
inst.up()
inst.ht()
inst.setpos(-500,100)
inst.write("Instructions:\nShoot all the ducks\nbefore 5 sec",font=("Century Gothic",15,"bold"))


def timer():
    global score,score_pen,no_of_ducks,ducks_state
    for i in range(no_of_ducks):
        ducks[i].hideturtle()
        ducks_state[i]="dead"
    print("Game Over")
    score_pen.clear()
    score_pen.setpos(0,0)
    score_pen.write("GAME OVER\nYour score is %s"%(score),align="center",font=("Century Gothic",30,"bold"))

def readpos(x,y):
    global score,score_pen,color,ducks_state,no_of_ducks
    for i in range(no_of_ducks):
        distance=math.sqrt(math.pow(x-ducks[i].xcor(),2)+math.pow(y-ducks[i].ycor(),2))
        if(distance<30 and ducks_state[i]=="alive"):
            color="blue"
            ducks[i].color(color)
            playsound("explosion.wav",0)
            ducks_state[i]="dead"
            time.sleep(0.2)
            ducks[i].hideturtle()
            score+=1
            score_pen.clear()
            score_pen.write("Score %s"%(score),font=("Century Gothic",15,"bold"))

window.listen()
window.onclick(readpos)
window.ontimer(timer,5000)
#main loop
while(True):
    for duck in ducks:
        #move ducks
        x=duck.xcor()
        x+=duckspeed
        duck.setx(x)
        
        #restrcting duck range
        if(duck.xcor()>350):
            y=duck.ycor()
            y-=40
            duckspeed*=-1
            duck.sety(y)

        if(duck.xcor()<-250):
            y=duck.ycor()
            y-=40
            duckspeed*=-1
            duck.sety(y)
        if(duck.ycor()<-250):
            print("Game Over")
            score_pen.clear()
            score_pen.setpos(0,0)
            score_pen.write("Score %s"%(score),font=("Century Gothic",15,"bold"))
