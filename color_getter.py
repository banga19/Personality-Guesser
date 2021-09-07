from tkinter import *

root = Tk()


class StartPage:

    def Widgets(self):

        def Color_retriever():

            color1 = "red"
            color2 = "green"
            color3 = "black"

            if entry.get() == color1:
                print("you picked red")
            elif entry.get() == color2:
                print("You picked green")
            elif entry.get() == color3:
                print("you picked black")
            else:
                print("we don't have that color")

                return Color_retriever()

        def Color_Display():
            colorz = Color_retriever()

            display = Text(master=canvas)
            display.place(relx=0.27, rely=0.69)

            display.insert(END, colorz)

        def one_punch():
            return Color_Display()

        frame = Frame(self)
        frame.pack()

        canvas = Canvas(self, bg="Violet")
        canvas.pack(expand=True, fill="both")

        entry = Entry(canvas, )
        entry.place(relx=0.27, rely=0.49, relwidth=0.34, relheight=0.09)

        button = Button(canvas, text="NEXT", command=one_punch)
        button.place(relx=0.27, rely=0.59, )


root.mainloop()
