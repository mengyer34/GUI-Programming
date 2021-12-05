# Input fields
from tkinter import *

root = Tk()

# Input box
a = Entry(root, width=50, borderwidth=5)
a.pack()
# add Placeholder 
a.insert(0, "Enter Your Name")

# Function creating (we use a.get() to caught input)
def myClick():
    hello = "Hello " + a.get()
    myLabel = Label(root, text=hello)
    myLabel.pack()
# Size of button is padx or pady
myButton = Button(root, text="Enter Your Name", padx=30, pady=5, command=myClick, fg="white", bg="blue")
myButton.pack()

root.mainloop()