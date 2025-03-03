#RadioButton = similar to checkbox. but you can only select one from a group

from tkinter import *

window = Tk()

image = PhotoImage(file='C:\\Users\\akosi\\OneDrive\\Desktop\\iccticon.png')
image2 = PhotoImage(file='C:\\Users\\akosi\\OneDrive\\Desktop\\iccticon.png')
image3 = PhotoImage(file='C:\\Users\\akosi\\OneDrive\\Desktop\\iccticon.png')

images = (image,image2,image3   )

food = ["pizza", "hamburger", "hotdog"]

def order():
     if(x.get()==0):
          print("you ordered 1")
     elif(x.get()==1):
          print("you ordered 2")
     elif(x.get()==2):
          print("you ordered 3")
     else:
          print("huh")

x = IntVar()

for index in range(len(food)): #iterate once through all the elements from the list, its gon create 3 radiobuttons
     radiobutton = Radiobutton(window, 
                               text=food[index],  #adds text to radio buttons
                               variable=x,        #groups radio buttons together if they share the same variable
                               value=index,       #assigns each radio button a different value
                               padx=25,           #adds padding to x axis
                               font=("Impact",50),
                               image = images[index], #adds images to radio button  
                               compound= 'left', #add images and text to the left
                               indicatoron=0, #eliminate circle indicators
                               width= 75,
                               command=order) #this will set command of radiobutton to function           
    
     radiobutton.pack(anchor=W)

window.mainloop()