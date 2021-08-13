from tkinter import *

#convert farehheit to celsius and kelvinS
def convert_fahr():
    words = fbtext.get() #get input from entry text boxS
    ftemp = float(words) #convert string to float
    celbox.delete(0, END)
    celbox.insert(0, '%.2f' % (tocel(ftemp))) #insert celsius equivalent
    kelbox.delete(0, END)
    kelbox.insert(0, '%.2f' % (tokel(tocel(ftemp)))) #insert kelvin equivalent
    return

def convert_cel():
    words = cbtext.get()
    ctemp = float(words)
    fahrbox.delete(0, END)
    fahrbox.insert(0, '%.2f' % (tofahr(ctemp)))
    kelbox.delete(0, END)
    kelbox.insert(0, '%.2f' % (tokel(ctemp)))

def convert_kel():
    words = kbtext.get()
    ktemp = float(words)
    fahrbox.delete(0, END)
    fahrbox.insert(0, '%.2f' % (tofahr(ktoc(ktemp))))
    celbox.delete(0, END)
    celbox.insert(0, '%.2f' % (ktoc(ktemp)))

def tocel(fahr): #convert farenheit 2 celsius
    return (fahr-32) * 5.0 / 9.0

def tofahr(cel):#convert celsius to farenheit
    return cel * 9.0 / 5.0 + 32

def ktoc(kel): #kelvin to celsius
    return kel - 273.15

def tokel(cel): #celsius to kelvin
    return cel + 273.15

###main
w=Tk() #tkinter works by starting a tcl/tk interpreter under the covers,
#Creating an instance of Tk initializes this interpreter and creates the root window
w.title("My Temperature Converter")

#Labels
fahrlabel = Label(w, text = 'Fahrenheit')
fahrlabel.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = E)

cellabel = Label(w, text = 'Celsius')
cellabel.grid(row = 1, column = 0, padx = 5, pady = 5, sticky = E)

kellabel = Label(w, text = 'Kelvin')
kellabel.grid(row = 2, column = 0, padx = 5, pady = 5, sticky = E)

#Horizontally adjacent text entry boxes
fbtext = StringVar()
fbtext.set('')
fahrbox=Entry(w,textvariable=fbtext)
fahrbox.grid(row=0,column=1,padx=5,pady=5)

cbtext = StringVar()
cbtext.set('')
celbox=Entry(w,textvariable=cbtext)
celbox.grid(row=1,column=1,padx=5,pady=5)

kbtext = StringVar()
kbtext.set('')
kelbox=Entry(w,textvariable=kbtext)
kelbox.grid(row=2,column=1,padx=5,pady=5)

##Go button & functionality
fgobutton = Button(w, text = 'Go', command = convert_fahr)#on pressing Go,
#function convert_fahr is activated 
fgobutton.grid(row = 0, column = 2, padx = 5, pady = 5, sticky = N+S+E+W)

cgobutton = Button(app, text = 'Go', command = convert_cel)
cgobutton.grid(row = 1, column = 2, padx = 5, pady = 5, sticky = N+S+E+W)

kgobutton = Button(app, text = 'Go', command = convert_kel)

#when we press the button named
#Exit quit from class quitter is called and that closes the window
#in-built

kgobutton.grid(row = 2, column = 2, padx = 5, pady = 5, sticky = N+S+E+W)

#Exit button
exitbutton = Button(w, text = 'Exit', command = quit) #when we press the button named
#Exit quit from class quitter is called and that closes the window
#in-built
exitbutton.grid(row = 3, column = 0, padx = 5, pady = 5, sticky = N+S+E+W, columnspan = 3)
#columnspan option is used to let a widget span more than one column,
#W+E+N+S means that the widget should be expanded in both directions.
w.mainloop()
