import random
import tkinter as tk


# ------THE LAYOUT----
# -----MAIN FORMAT TO ADDING A PAGE --------


class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self, )
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, SecondPage, SecondPage2, VAR):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame("StartPage")

    def show_frame(self, page_name):
        """Show a frame for the given page name"""
        frame = self.frames[page_name]
        frame.tkraise()


# -----FIRST PAGE -----
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        frame = tk.Frame(self, )
        frame.pack()

        canvas = tk.Canvas(self, bg="#ffff99", )
        canvas.pack(expand=True, fill="both")

        L1 = tk.Label(canvas, bd=7, text="WELCOME", font=12)
        L1.place(relx=0.5, rely=0.1, relwidth=0.5, relheight=0.09, anchor="n")

        L2 = tk.Label(canvas, bd=7, text="WHAT IS YOUR NAME?", )  # create a function that will show the shows name
        # on the second page 1 and 2
        L2.place(relx=0.5, rely=0.25, relwidth=0.5, relheight=0.09, anchor="n")

        Entry1 = tk.Entry(canvas, bd=7, )
        Entry1.place(relx=0.25, relwidth=0.5, rely=0.45, relheight=0.09)

        B1 = tk.Button(canvas, bd=7, text="NEXT", command=lambda: controller.show_frame("SecondPage"))

        B1.place(relx=0.47, rely=0.95, anchor="s", relwidth=0.3, relheight=0.1)

        def phrase_generator():
            phrases = ["Hey ", "Whats up ", "Aloha ", "Habari Yako "]

            name = str(Entry1.get())

            return phrases[random.randint(0, 3)] + name

        def phrase_display():
            greetings = phrase_generator()

            greeting_display = tk.Text(master=canvas, )
            greeting_display.place(relx=0.48, rely=0.77, anchor="s", relwidth=0.5, relheight=0.1)

            greeting_display.insert(tk.END, greetings)

        display_button = tk.Button(canvas, text="Click Me MORE!!!", command=phrase_display)
        display_button.place(relx=0.25, rely=0.55)


# -----SECOND PAGE -------

class SecondPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        frame2 = tk.Frame(self, )
        frame2.pack()

        canvas2 = tk.Canvas(self, bg="#ffff99", )
        canvas2.pack(expand=True, fill="both")

        L3 = tk.Label(canvas2, bd=7, text="WHAT IS YOUR FAVORITE COLOR ?", )
        L3.place(relx=0.5, rely=0.25, relwidth=0.6, relheight=0.09, anchor="n")

        Entry2 = tk.Entry(canvas2, bd=7, )
        Entry2.place(relx=0.25, relwidth=0.5, rely=0.45, relheight=0.09)

        B2 = tk.Button(canvas2, bd=7, text=" NEXT Page!", command=lambda: controller.show_frame("VAR"))
        B2.place(relx=0.47, rely=0.95, anchor="s", relwidth=0.3, relheight=0.1)


# ----SECOND PAGE 2-----

class SecondPage2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        frame3 = tk.Frame(self, )
        frame3.pack()

        canvas3 = tk.Canvas(self, bg="#ffff99", )
        canvas3.pack(expand=True, fill="both")

        L4 = tk.Label(canvas3, bd=7, text="WHAT IS YOUR FAVORITE COLOR ?", )
        L4.place(relx=0.5, rely=0.25, relwidth=0.6, relheight=0.09, anchor="n")

        E3 = tk.Text(canvas3, bd=7, )
        E3.place(relx=0.25, relwidth=0.5, rely=0.45, relheight=0.09)

        B3 = tk.Button(canvas3, bd=7, text="FIND OUT!", command=lambda: controller.show_frame("VAR"))
        B3.place(relx=0.47, rely=0.7, anchor="s", relwidth=0.3, relheight=0.1)

        B4 = tk.Button(canvas3, bd=7, text="HOME", command=lambda: controller.show_frame("StartPage"))
        B4.place(relx=0.78, rely=0.9, anchor="s", relwidth=0.3, relheight=0.1)


# ------PAGE THAT SHOWS THE ANSWERS

class VAR(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        frame4 = tk.Frame(self, )
        frame4.pack()

        canvas4 = tk.Canvas(self, bg="#ffff99", )
        canvas4.pack(expand=True, fill="both")

        E4 = tk.Entry(canvas4, )
        E4.place(relx=0.05, rely=0.04, relwidth=0.9, relheight=0.78)

        B5 = tk.Button(canvas4, text="CHOOSE ANOTHER COLOR", command=lambda: controller.show_frame("SecondPage2"))
        B5.place(relx=0.1, rely=0.84, )

        B6 = tk.Button(canvas4, text="HOME", command=lambda: controller.show_frame("StartPage"))
        B6.place(relx=0.7, rely=0.84)


# WHAT MAKES THE APP TO RUN

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
