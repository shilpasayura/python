import tkinter as tk
import turtle

root = tk.Tk()

for i in range(1,5):
    
    for i in range(1,3):
        turtle.forward(50)
        turtle.left(90)

        turtle.forward(30) #smaller side
        turtle.left(90)
    turtle.penup()    
    turtle.forward(100)
    turtle.pendown()

root.mainloop()