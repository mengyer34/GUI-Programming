from tkinter import *
# Need
from PIL import ImageTk, Image
root = Tk()
root.title("Set img")

# Icon for ico
root.iconbitmap('icons/check.ico')

# img set
my_img = ImageTk.PhotoImage(Image.open("icons/phone.png"))

# Image put on screen
my_label = Label(image=my_img)
my_label.pack()

my_img

button_quit = Button(root, text="Exit Program", command=root.quit)
root.mainloop()