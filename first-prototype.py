from tkinter import *
import turtle
root = Tk()


root.wm_title('Spiral Game')
root.configure(background='purple')
pen_size=100
pen_Colour='blue'
abidraws = turtle.Turtle()
abidraws.speed(100)


def kaleidoscope(pen_size, pen_Colour):
    abidraws.pendown()
    abidraws.color(pen_Colour)
    for i in range(50):
        abidraws.forward(pen_size)
        abidraws.left(123)

def pentagon(pen_size, pen_Colour):
    abidraws.pendown()
    abidraws.color(pen_Colour)
    for i in range(pen_size):
        abidraws.forward(i * 10)
        abidraws.right(144)

def spiral(pen_size, pen_Colour):
    abidraws.pendown()
    abidraws.color(pen_Colour)
    meme=0
    for i in range(100):
        abidraws.forward(meme/10)
        meme+=pen_size/100
        abidraws.left(15)

def clock(pen_size,pen_Colour):
    abidraws.pendown()
    abidraws.color(pen_Colour)
    for i in range(180):
        abidraws.forward(pen_size)
        abidraws.right(30)
        abidraws.forward(pen_size/5)
        abidraws.left(60)
        abidraws.forward(pen_size/3)
        abidraws.right(30)
        abidraws.penup()
        abidraws.setposition(0, 0)
        abidraws.pendown()
        abidraws.right(2)

def size(penSize):
    global pen_size
    if penSize==1:
        pen_size=50
    elif penSize==2:
        pen_size=100
    else:
        pen_size=180
    print(pen_size)


def colour(penColour):
    global pen_colour
    if penColour==1:
        pen_Colour='red'
    elif penColour==2:
        pen_colour='green'
    else:
        pen_colour='blue'
        

Label(root, text='Spiral Game', font=("Helvetica", 24), fg="orange", bg='purple').grid(rowspan=1,columnspan=3,row=0,column=0)
Label(root, text='Shape', font=("Helvetica", 18), fg="orange", bg='purple').grid(row=1,column=0)
Label(root, text='Colour', font=("Helvetica", 18), fg="orange", bg='purple').grid(row=1,column=2)
Label(root, text='Size', font=("Helvetica", 18), fg="orange", bg='purple').grid(row=1,column=1)
Button(root, text='Kaleidoscope', bg='orange', command=lambda:kaleidoscope(pen_size,pen_Colour), height = 2, width = 10).grid(row=2,column=0)
Button(root, text='Pentagon',bg='orange', command=lambda:pentagon(pen_size,pen_Colour), height = 2, width = 10).grid(row=3,column=0)
Button(root, text='Spiral',bg='orange', command=lambda:spiral(pen_size,pen_Colour), height = 2, width = 10).grid(row=4,column=0)
Button(root, text='Clock',bg='orange', command=lambda:clock(pen_size,pen_Colour), height = 2, width = 10).grid(row=5,column=0)
Button(root, text='Size: Small',bg='orange', command=lambda:size(1), height = 2, width = 10).grid(row=2,column=1)
Button(root, text='Size: Medium',bg='orange', command=lambda:size(2), height = 2, width = 10).grid(row=3,column=1)
Button(root, text='Size: Large',bg='orange', command=lambda:size(3), height = 2, width = 10).grid(row=4,column=1)
Button(root, text='Colour: Red',bg='orange', command=lambda:colour(1), height = 2, width = 10).grid(row=2,column=2)
Button(root, text='Colour: Green',bg='orange', command=lambda:colour(2), height = 2, width = 10).grid(row=3,column=2)
Button(root, text='Colour: Blue',bg='orange', command=lambda:colour(3), height = 2, width = 10).grid(row=4,column=2)



root.mainloop()

