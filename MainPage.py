from tkinter import *

HEIGHT = 450
WIDTH = 350


# def Chosen():
    # mtext = ment.get()
    # La2 = Label(Canvas, text=mtext, )
    # La2.pack(height=HEIGHT, width=W)

    # return


root = Tk()

ment = StringVar()

frame = Frame(root, height=HEIGHT, width=WIDTH)
frame.pack()

canvas = Canvas(root, height=HEIGHT, width=WIDTH, bg="#ffff99", )
canvas.place(relwidth=1, relheight=1, )

L1 = Label(canvas, bd=7, text="WELCOME", font=12)
L1.place(relx=0.5, rely=0.1, relwidth=0.5, relheight=0.09, anchor="n")

L2 = Label(canvas, bd=7, text="WHAT IS YOUR NAME?", )
L2.place(relx=0.5, rely=0.25, relwidth=0.5, relheight=0.09, anchor="n")

E1 = Entry(canvas, bd=7, textvariable=ment)
E1.place(relx=0.25, relwidth=0.5, rely=0.45, relheight=0.09)

B1 = Button(canvas, bd=7, text="NEXT")
B1.place(relx=0.47, rely=0.7, anchor="s", relwidth=0.3, relheight=0.1)


root.mainloop()
