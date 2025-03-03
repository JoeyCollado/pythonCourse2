#label = an area widget that holds text and/or an image within a window


from tkinter import *
window = Tk()

photo = PhotoImage(file='C:\\Users\\akosi\\OneDrive\\Desktop\\peak.png')

#                                                                       
label = Label(window, text="Hello World",       #set the master of the label to our window
                      font=('Arial',
                            40,
                            'bold'),
                            fg='green',         #foreground color
                            bg='black',         #background color
                            relief=RAISED,      #border style
                            bd=10,              #border style width
                            padx=20,            #padding to the x axis
                            pady=20,            #padding to the y axis
                            image=photo,        #adding image to the label
                            compound='bottom',)  #setting the location of the image in the label
label.pack() #adding the label to the window, option 1
#label.place(x=0, y=0) #adding the label to the window, option 2, we can use the x and y coordinate to place our label



window.mainloop()