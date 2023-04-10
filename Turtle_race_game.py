import turtle
from turtle import *
from random import randint

#set up screen
window=turtle.Screen()
window.title("Turtle Race game")


turtle.bgcolor("forestgreen")
turtle.speed(0)
turtle.penup()
turtle.setpos(-140,200)
turtle.write("Turtle Race Game ",align = "center",font=("Ärial",40,"bold"))

turtle.setpos(-650,-210)
turtle.color("chocolate")
turtle.begin_fill()
turtle.pendown()
for i in range(2):  #rectangle
    turtle.forward(1300)
    turtle.right(90)
    turtle.forward(1300)
    turtle.right(90)
turtle.end_fill()


# FINISH LINE
gap_size = 20
shape("square")
penup()

# WHITE SQUARES ROW 1
color("white")
for i in range(10):
    goto(250, (170 - (i * gap_size * 2)))
    stamp()

# WHITE SQUARES ROW 2
for i in range(10):
    goto(250 + gap_size, ((210 - gap_size) - (i * gap_size * 2)))
    stamp()

# BLACK SQUARES ROW 1
color("black")
for i in range(10):
    goto(250, (190 - (i * gap_size * 2)))
    stamp()

# BLACK SQUARES ROW 2
for i in range(10):
    goto(251 + gap_size, ((190 - gap_size) - (i * gap_size * 2)))
    stamp()
       
#contestants
#player1
turtle1=Turtle()
turtle1.speed(0)
turtle1.color("blue")
turtle1.shape("turtle")
turtle1.penup()
turtle1.goto(-250,100)
turtle1.pendown()

#player2
turtle2=Turtle()
turtle2.speed(0)
turtle2.color("red")
turtle2.shape("turtle")
turtle2.penup()
turtle2.goto(-250,50)
turtle2.pendown()


#player3
turtle3=Turtle()
turtle3.speed(0)
turtle3.color("pink")
turtle3.shape("turtle")
turtle3.penup()
turtle3.goto(-250,0)
turtle3.pendown()


#player4
turtle4=Turtle()
turtle4.speed(0)
turtle4.color("yellow")
turtle4.shape("turtle")
turtle4.penup()
turtle4.goto(-250,-50)
turtle4.pendown()

t1=0
t2=0
t3=0
t4=0

for i in range(180):
    k=randint(1,5)
    l=randint(1,5)
    m=randint(1,5)
    n=randint(1,5)
    
    turtle1.forward(k)
    turtle2.forward(l)
    turtle3.forward(m)
    turtle4.forward(n)
    
    t1=+k
    t2+=l
    t3+=m
    t4+=n
    
    if t1>=480:
        turtle1.goto(0,-120)
        turtle.goto(0,-150)
        turtle.write("Winner is turtle 1",font=("Arial",20,"bold"))
        break
    
    elif  t2>=480:
        turtle2.goto(0,-120)
        turtle.goto(0,-150)
        turtle.write("Winner is turtle 2",font=("Arial",20,"bold"))
        break
    
    elif t3>=480:
        turtle3.goto(0,-120)
        turtle.goto(0,-150)
        turtle.write("Winner is turtle 3",font=("Arial",20,"bold"))
        break
    
    elif t4>=480:
        turtle4.goto(0,-120)
        turtle.goto(0,-150)
        turtle.write("Winner is turtle 4",font=("Arial",20,"bold"))
        break


turtle.hideturtle()
turtle.done()

    
    