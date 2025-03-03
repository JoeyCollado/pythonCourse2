#GUI
#Tkinter = python standard GUI

#windows = GUI elements: button, textboxes, labels, images
#widgets = serves as a container to hold or contain these widgets

from tkinter import * #import anything related to tkinter module

#changeable
window = Tk() #instantiate an instance of a window 
window.geometry("420x420") #set the size of the window
window.title("First GUI") #changes the title of the window


Icon = PhotoImage(file='C:\\Users\\akosi\\OneDrive\\Desktop\\icct.png')  #changes the icon of the window
window.iconphoto(True,Icon)

window.config(background="black")#changes bg color
                        

window.mainloop() #display the window in computer screen and it will also listen to events
