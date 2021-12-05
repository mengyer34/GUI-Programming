# from tkinter import *

# root = Tk()

# # Create a Label widget
# myLabel = Label(root, text="Hello World!")

# # Shoving it onto the screen
# myLabel.pack()

# root.mainloop()


# Part2 Ways that we use for set location text
from tkinter import *

root = Tk()

# Create a Label widget
myLabel1 = Label(root, text="Hello World!")
myLabel2 = Label(root, text="I am a student in PNC")
myLabel3 = Label(root, text="Mengyi").grid(row=0, column=5)

# Shoving it onto the screen
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=5)

root.mainloop()