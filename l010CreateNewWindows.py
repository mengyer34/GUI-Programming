from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title("Learn to code at codemy.com")
# Icon for ico
root.iconbitmap('icons/check.ico')

def open():
    global my_img
    top = Toplevel()
    top.title("Learn to Code at me!")
    top.iconbitmap("icons/check.ico")
    my_img = ImageTk.PhotoImage(Image.open("icons/phone.png"))
    my_label = Label(top, image=my_img).pack()
    btn2 = Button(top, text="Close Window", command=top.destroy).pack()

btn = Button(root, text="Open Second Window", command=open).pack()

root.mainloop()