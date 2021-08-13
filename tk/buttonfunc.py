import tkinter

###main

#tkinter works by starting a tcl/tk interpreter under the covers,
#Creating an instance of Tk initializes this interpreter and creates the root window

window=tkinter.Tk()
window.title("My Button")

#pad adds padding/space around the button
#pack puts/packs the button in the window
button = tkinter.Button(window,text="Hi",width=40)

##must be called for windows to be drawn and events to be processed

button.pack(padx=20, pady=20) 

window.mainloop()
