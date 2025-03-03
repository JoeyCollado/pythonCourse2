#color chooser
from tkinter import *
from tkinter import colorchooser

def click():
    color = colorchooser.askcolor() #ask color is a function, here we store the function inside the variable
    colorHex = color[1] #extracting the hexadecimal value
    print(colorHex) #prints the hexdecimal value
    window.config(bg=colorHex) #changes the background color

    

window = Tk()


window.geometry("420x420")
button = Button(text='Click me', command=click)
button.pack()

window.mainloop()