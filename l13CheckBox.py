from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title('File')
root.iconbitmap("icons/check.ico")
root.geometry("400x400")

def show():
    # Get var 0 or 1
    myLabel = Label(root, text=var.get()).pack()

# # first thing
# var = IntVar()

# or get On or Off or other word would you like
var = StringVar()

# c = Checkbutton(root, text="Check this box, I dare you!", variable=var)
c = Checkbutton(root, text="Check this box, I dare you!", variable=var, onvalue="On", offvalue="Off" )
# Change select by default
c.deselect()
c.pack()

myButton = Button(root, text="Show Selection", command=show).pack()

root.mainloop()