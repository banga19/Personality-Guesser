from tkinter import *

HEIGHT = 450
WIDTH = 350

root = Tk()


frame2 = Frame(root, height=HEIGHT, width=WIDTH)
frame2.pack()

canvas2 = Canvas(root, height=HEIGHT, width=WIDTH, bg="#ffff99")
canvas2.pack()

L3 = Label(canvas2, bd=7, text="WHAT IS YOUR FAVORITE COLOR ?", )
L3.place(relx=0.5, rely=0.25, relwidth=0.6, relheight=0.09, anchor="n")

E2 = Entry(canvas2, bd=7, )
E2.place(relx=0.25, relwidth=0.5, rely=0.45, relheight=0.09)

B2 = Button(canvas2, bd=7, text="FIND OUT!")
B2.place(relx=0.47, rely=0.7, anchor="s", relwidth=0.3, relheight=0.1)

root.mainloop()
