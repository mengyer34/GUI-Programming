from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title('File')
root.iconbitmap("icons/check.ico")


# # Open File (*.*) => for all file
# root.filename = filedialog.askopenfilename(initialdir="icons", title="Select A file", filetypes=(("png files", "*.png"), ("all files", "*.*")))
# my_label = Label(root, text=root.filename).pack()
# my_image = ImageTk.PhotoImage(Image.open(root.filename))
# my_image_label = Label(image=my_image).pack()

def open():
    global my_image
    # Open File (*.*) => for all file
    root.filename = filedialog.askopenfilename(initialdir="icons", title="Select A file", filetypes=(("png files", "*.png"), ("all files", "*.*")))
    my_label = Label(root, text=root.filename).pack()
    my_image = ImageTk.PhotoImage(Image.open(root.filename))
    my_image_label = Label(image=my_image).pack()

my_btn = Button(root, text="Open File", command=open).pack()

root.mainloop()