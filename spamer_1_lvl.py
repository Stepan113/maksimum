from tkinter import *


def spamer1():
    window = Tk()
    label = Label(window, text="Тебе крышка)", font=("Comic Sans MS", 24)).pack()

    def infinity_win():
        rot = Toplevel()
        while True:
            rot.after(10, infinity_win())

    button_one = Button(window, text="Infinite Window !", command=infinity_win)
    button_one.pack()
    window.mainloop()
