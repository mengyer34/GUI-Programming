from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Learn to code at codemy.com")
# Icon for ico
root.iconbitmap('icons/check.ico')

frame = LabelFrame(root, text="This is my frame...", padx=100, pady=100)
frame.pack(padx=10, pady=10)

b = Button(frame, text="Don't Click Here!")
b2 = Button(frame, text="Don't Click Here!")
b.grid(row=0, column=0, pady=10)
b2.grid(row=1, column=0)

root.mainloop()