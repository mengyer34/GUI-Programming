from tkinter import *
window = Tk()
window.geometry("300x300")
window.title("Mengyi")

labell = Label(window, text="I am a student in PNC", fg="blue",bg="yellow", relief="solid",font=("arail", 17, "bold"))
labell.pack()

# Button 
button1 = Button(window, text="Demo",relief=RIDGE, fg="white",bg="brown",font=("arail", 17, "bold"))
button1.place(x=110, y=110)
window.mainloop()

# template
from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title('File')
root.iconbitmap("icons/check.ico")

root.mainloop()