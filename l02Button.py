# Creating Buttons
from tkinter import *

root = Tk()

# Function creating
def myClick():
    myLabel = Label(root, text="Look! I click a Button!")
    myLabel.pack()
# Size of button is padx or pady
myButton = Button(root, text="Click Me", padx=30, pady=10, command=myClick, fg="white", bg="blue")
myButton.pack()

root.mainloop()