import tkinter as tk
import turtle

root = tk.Tk()

turtle.speed("fast")
turtle.pencolor("white")
turtle.pensize(2)

turtle.Screen().bgcolor("blue")

def vsnow():
    turtle.right(30)
    turtle.forward(60)
    turtle.backward(60)
    turtle.left(60)

    turtle.forward(60)
    turtle.backward(60)
    turtle.right(30)


#vsnow()

def snowArm():
    for i in range(0,4):
        turtle.forward(30)
        vsnow()
    turtle.backward(120) #go back to starting location

# repeat the snowflake arm
def snowf():
    for x in range(0,12):
        snowArm()
        turtle.right(30) 


snowf()


root.mainloop()
