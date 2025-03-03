#button = when you click it, it does something

from tkinter import *

count = 0

def click():
    global count #increment 1 so we can count how many times the button been cliked
    count+=1
    print("You click the button")
    print(count)

window = Tk()

#photo = PhotoImage(file='C:\\Users\\akosi\\OneDrive\\Desktop\\icct.png')

button = Button(window,    #set a button the the window
                text="click me", #text button 
                command=click, #add a command to the button, and after this you have to define its function by declaring a function
                font=("Comic Sans", 30),
                fg="cyan",
                bg="black",
                activeforeground="cyan",
                activebackground="black",
                #image="photo",
                compound='bottom')  
button.pack() #add the window the the button

window.mainloop()