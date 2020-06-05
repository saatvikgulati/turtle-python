import turtle
import math
import random
#import vlc
from playsound import playsound
window=turtle.Screen()

window.bgcolor("black")
window.title("Space invaders")
window.bgpic("E:\\Game\\space.gif")

#Draw border

border_drawer=turtle.Turtle()
border_drawer.penup()
border_drawer.color("white")
border_drawer.speed(0)
border_drawer.setpos(-250,-250)
border_drawer.pendown()
border_drawer.pensize(3)
for i in range(4):
    border_drawer.forward(600)
    border_drawer.left(90)
border_drawer.hideturtle()

#create players
player1=turtle.Turtle()
window.addshape('spaceship.gif')
window.addshape('monster.gif')
player1.shape('spaceship.gif')
player1.color("blue")
player1.penup()
player1.speed(0)
player1.setpos(50,-250)
player1.left(90)
player1.shapesize(3)

#creating monster
'''monster=turtle.Turtle()
monster.color("red")
monster.shape("turtle")
monster.setheading(-90)
monster.speed(0)
monster.up()
monster.setpos(-250,250)'''

monsterspeed=2
no_of_monsters=5
monsters=[]
#sound_file=vlc.MediaPlayer("laser.wav")
#sound_file1=vlc.MediaPlayer("explosion.wav")
for i in range(no_of_monsters):
    monsters.append(turtle.Turtle())
    monsters[i].color("red")
    monsters[i].shape("monster.gif")
    monsters[i].setheading(-90)
    monsters[i].speed(0)
    monsters[i].up()
    x=random.randint(-200,200)
    y=random.randint(100,250)
    monsters[i].setpos(x,y)

#create bullet
bullet=turtle.Turtle()
bullet.shape("triangle")
bullet.shapesize(0.5,0.5)
bullet.color("white")
bullet.up()
bullet.hideturtle()
bullet.speed(0)
bulletspeed=20
bullet.left(90)

#define bullet state
bulletstate="ready"

#setting a score
score=0
score_pen=turtle.Turtle()
score_pen.speed(0)
score_pen.color("blue")
score_pen.up()
score_pen.hideturtle()
score_pen.setpos(-240,290)
score_pen.write("Score %s"%(score),font=("Century Gothic",15,"bold"))

#func that will check collison
def isCollision(t1,t2):
    x1=t1.xcor()
    y1=t1.ycor()
    x2=t2.xcor()
    y2=t2.ycor()
    distance=math.sqrt(math.pow(x1-x2,2)+math.pow(y1-y2,2))
    if distance<30:
        playsound("explosion.wav",0)
        #sound_file1.play()
        return True
    else:
        return False

def fire_bullet():
    global bulletstate
    if(bulletstate=="ready"):
        bulletstate="fire"
        #moving bullet up
        x=player1.xcor()
        y=player1.ycor()
        playsound("laser.wav",0)
        #sound_file.play()
        bullet.setpos(x,y+10)
        bullet.showturtle()

def right():
    curr_pos=player1.xcor()
    curr_pos+=15
    if(curr_pos>350):
        curr_pos-=15
    player1.setx(curr_pos)
        

def left():
    curr_pos=player1.xcor()
    curr_pos-=15
    if(curr_pos<-250):
        curr_pos+=15
    player1.setx(curr_pos)

def increase_speed():
    global monsterspeed
    if(score==5):
        monsterspeed+=2
    
window.listen()

window.onkeypress(right, "Right")
window.onkeypress(left, "Left")
window.onkey(fire_bullet,"space")

#main loop
while(True):
    for monster in monsters:
        #move monster
        x=monster.xcor()
        x+=monsterspeed
        monster.setx(x)

        #moving monster back and down
        if(monster.xcor()>350):
            y=monster.ycor()
            y=y-40
            monsterspeed*=-1
            monster.sety(y)
            
         #rebouncing from left wall and down
        if(monster.xcor()<-250):
            y=monster.ycor()
            y=y-40
            monsterspeed*=-1
            monster.sety(y)

        if(monster.ycor()<-200):
            print("Game Over")
            monster.hideturtle()
            player1.hideturtle()
            break

        #move the bullet up
        if(bulletstate=="fire"):
            #move the bullet
            y=bullet.ycor()
            y+=bulletspeed
            bullet.sety(y)

        #restrict the bullet range to the white box
        if(bullet.ycor()>350):
            bullet.hideturtle()
            bulletstate="ready"

        #check collison between bullet and monster and update score
        if(isCollision(bullet,monster)):
            x=random.randint(-200,200)
            y=random.randint(100,250)
            monster.setpos(x,y)
            #reset bullet position
            bullet.setpos(0,-400)
            bulletstate="ready"
            score+=1
            score_pen.clear()
            score_pen.write("Score %s"%(score),font=("Century Gothic",15,"bold"))

        #check collision between monster and player1
        '''if(isCollision(monster,player1)):
            monster.hideturtle()
            player1.hideturtle()
            print("Game Over")'''
        #changing difficulty levels
        #increase_speed()
