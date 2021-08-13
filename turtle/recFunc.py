import tkinter as tk
import turtle

root = tk.Tk()

def rect(horiz,vert,color):
    #put the pen down to start drawing
    turtle.pendown()  
    turtle.pensize(2)

    turtle.color(color)
    turtle.begin_fill()

    for i in range(1,3):
        turtle.forward(horiz)
        turtle.right(90)
        turtle.forward(vert)
        turtle.right(90)

    turtle.end_fill()
    #pull pen up to stop drawing
    turtle.penup() 
    turtle.speed("slow")   

rect(50,25,'red')    






root.mainloop()
