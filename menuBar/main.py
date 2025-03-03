from tkinter import *


def openFile():
    print("File has been opened")
def saveFile():
    print("File has been saved")

window = Tk()

menuBar = Menu(window) #adding the menubar to the window
window.config(menu=menuBar) #setting the menu = menubar

fileMenu = Menu(menuBar, tearoff=0) #adding this menu to the menubar
menuBar.add_cascade(label="File", menu=fileMenu) #this will have a dropdown menu effect

#adding these options to the dropdown menu, of the file menu
fileMenu.add_command(label="Open", command=openFile)
fileMenu.add_command(label="Save", command=saveFile)
fileMenu.add_separator() #creates a line that separates exit from open and save
fileMenu.add_command(label="Exit", command=quit)

window.mainloop()