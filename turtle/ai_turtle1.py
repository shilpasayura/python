import turtle
import time
import random


def move_food(F):
    global fx, fy
    # Move food random
    ww2=ww/2
    wh2=wh/2
    fx = (random.randint(-ww2, wh2)// 10) * 10
    fy = (random.randint(-ww2, wh2) // 10) * 10
    F.goto(fx, fy)

ww = 500
wh = 500
speed = 0.1
fx = 0
fy = 0

# Set up the screen
wn = turtle.Screen()
wn.title("AI Snake ")
#wn.bgcolor("green")
wn.setup(ww, wh)

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("turtle")
#head.color("yellow")
head.penup()
head.goto(0, 0)

# food
F = turtle.Turtle()
F.speed(0)
F.shape("circle")
F.color("red")
F.penup()
move_food(F)

xd = 0
yd = 0
points = 0

# Main loop
while points < 5:

    xd = fx - head.xcor()
    yd = fy - head.ycor()

    if xd < 0:
        stx = -10
        xdir=180
    else:
        stx = 10
        xdir=0

    if yd < 0:
        sty = -10
        ydir=270
    else:
        sty = 10
        ydir=90

    head.setheading(xdir)
    while xd != 0:
        head.setx(head.xcor() + stx)
        xd = xd - stx
        time.sleep(.1)

    head.setheading(ydir)
    while yd != 0:
        head.sety(head.ycor() + sty)
        yd = yd - sty
        time.sleep(.1)

    if head.distance(F) < 20:
        #turtle.write("Collision")
        collision = 1

    # Move the food
    move_food(F)
    time.sleep(1)
    points = points + 1

wn.mainloop()