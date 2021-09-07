from tkinter import *

root = Tk()

photo = PhotoImage(file="orange.jpeg")
label = Label(image=photo)
label.pack()

root.mainloop()