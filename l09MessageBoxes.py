from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title("Learn to code at codemy.com")
# Icon for ico
root.iconbitmap('icons/check.ico')

# showinfo, showwarning, showerror, askokcancel, askyesno
def popup():
    response = messagebox.askyesno("This is my Popup", "Hello World!")
    # show what will caught
    Label(root, text=response).pack()
    
    # Condition
    if response == 1:
        Label(root, text="You click on Yes!").pack()
    else:
        Label(root, text="You click on No!").pack()

    

Button(root, text="Popup", command=popup).pack()

root.mainloop()