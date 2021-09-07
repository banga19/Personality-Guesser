from tkinter import *

HEIGHT = 450
WIDTH = 350

root = Tk()

frame4 = Frame(root, height=HEIGHT, width=WIDTH)
frame4.pack()

canvas4 = Canvas(root, height=HEIGHT, width=WIDTH, bg="#ffff99", )
canvas4.place(relwidth=1, relheight=1, )

E4 = Entry(canvas4, )
E4.place(relx=0.05, rely=0.04, relwidth=0.9, relheight=0.78)

B5 = Button(canvas4, text="CHOOSE ANOTHER COLOR")
B5.place(relx=0.1, rely=0.84, )

B6 = Button(canvas4, text="HOME")
B6.place(relx=0.7, rely=0.84)
root.mainloop()






