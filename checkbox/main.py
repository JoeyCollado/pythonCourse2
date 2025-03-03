#checkbox widget

from tkinter import *

#defining display command
def display():
    if(x.get()==1): #if somebody clicks on the checkbox
     print("You agree")
    else:
     print("You dont agree")

window = Tk()

#defining x
x = IntVar() #coz we want it to return an integer, (you can use StringVar if you want to return a string)


check_button = Checkbutton(window, 
                           text="I agree to something",
                           variable=x,  
                           onvalue=1,    #onvalue = refers to what's going to be stored within our variable when its toggled on
                           offvalue=0,
                           command=display,
                           font=('Arial',20),
                           fg='green',
                           bg='black',
                           activeforeground='green',
                           activebackground='black',
                           padx=25,
                           pady=10)
                           
check_button.pack()

window.mainloop()