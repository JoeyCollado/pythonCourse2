#text area
#text widget = functions like a text area , you can enter multiple lines of text
from tkinter import *

def submit():
    input = text.get("1.0", END) #get the text from index 1.0 to end
    print(input)
window = Tk()

text = Text(window,
            bg="light yellow",
            font=("System", 25, "bold"),
            height=8,
            width=20,
            padx=20,
            pady=20,
            fg="purple")
text.pack()

button = Button(window, text='Submit', command=submit)
button.pack()

window.mainloop()