import tkinter as tk

LARGE_FONT = ("verdana", 12)


class MyApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        self.frames = {}

        frame = StartPage(container, self)

        frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frame[cont]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.frame.__init__(self, parent)
        button = tk.Button()
        button.pack_()


app = MyApp()
app.mainloop()
