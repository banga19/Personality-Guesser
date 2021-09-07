from tkinter import *

HEIGHT = 450
WIDTH = 350

root = Tk()

frame3 = Frame(root, height=HEIGHT, width=WIDTH)
frame3.pack()

canvas3 = Canvas(root, height=HEIGHT, width=WIDTH, bg="#ffff99")
canvas3.pack()

L4 = Label(canvas3, bd=7, text="WHAT IS YOUR FAVORITE COLOR ?", )
L4.place(relx=0.5, rely=0.25, relwidth=0.6, relheight=0.09, anchor="n")

E3 = Entry(canvas3, bd=7, )
E3.place(relx=0.25, relwidth=0.5, rely=0.45, relheight=0.09)

B3 = Button(canvas3, bd=7, text="FIND OUT!")
B3.place(relx=0.47, rely=0.7, anchor="s", relwidth=0.3, relheight=0.1)

B4 = Button(canvas3,  bd=7, text="HOME")
B4.place(relx=0.78, rely=0.9, anchor="s", relwidth=0.3, relheight=0.1)

root.mainloop()








