from tkinter import *
from tkinter import messagebox
import random
from Proekt import sending, main_window


def runbut():
    class Runbutton:
        def __init__(self, main):
            self.label = Label(main, text="Вы \n хотите показать \n нам Кешу?", font=("Comic Sans MS", 50))
            self.but_yes = Button(main, text="Да", font=("Comic Sans MS", 25))
            self.but_no = Button(main, text="Нет", font=("Comic Sans MS", 25))

            self.label.pack()
            self.but_yes.place(x=170, y=280)
            self.but_no.place(x=270, y=280)

            self.but_yes.bind("<Button-1>", self.xeek)
            self.but_no.bind("<Enter>", self.xex)

        def xex(self, event):
            self.but_no.place(x=random.randint(50, 500), y=random.randint(50, 500))

        def xeek(self, event):
            self.mes = messagebox.showinfo("ПОПУГАЙ", "Зрители хотят увидеть Кешу)")
            window.destroy()

    def close():
        rus = messagebox.askokcancel("Кеша", "Вы хотите выйти?")
        if rus:
            rul = messagebox.askokcancel("КЕША", "А Кеша точно будет?)")
            if rul:
                messagebox.showinfo("УРА", "УРА")
                window.destroy()
                main_window.maw()

            else:
                messagebox.showerror("ОШИБКА", "ОТВЕТ НЕПРАВИЛЬНЫЙ")
                sending.skam_1()

    window = Tk()
    window.geometry("600x600")
    q = Runbutton(window)
    window.protocol("WM_DELETE_WINDOW", close)
    window.mainloop()

# runbut()
