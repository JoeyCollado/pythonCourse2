from tkinter import *

#entry widget = textbox that accepts a single line of user input

#defines what submit button does
def submit():
    username = entry.get() #storing the entry.get to username variable
    print("Hello " + username)
    entry.config(state=DISABLED)#after the username is submit the entry box will be disabled

#defines what delete button does
def delete():
    entry.delete(0,END) #delete a text from index 0 til the end, coz the constructor contains two positional arguments
#defines what backspace button does
def backspace():
    entry.delete(len(entry.get())-1, END) #deletes the last character

window = Tk()

entry = Entry(window,
              font=("Consolas", 50),
              fg="green",
              bg="black",
              show="*") #creating an instance of the entry and adding it to the 
entry.insert(0,'Spongebob') #creates a default text on the window
entry.pack(side=LEFT) #placing the window to left

#button 1
submit_button = Button(window,text="Submit", command=submit)
submit_button.pack(side=RIGHT)

#button 2
delete_button = Button(window,text="Delete", command=delete)
delete_button.pack(side=RIGHT)

#button 3
backspace_button = Button(window,text="Backspace", command=backspace)
backspace_button.pack(side=RIGHT)


window.mainloop()