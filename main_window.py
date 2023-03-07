from tkinter import *
from datetime import datetime
from tkinter import messagebox
from Proekt import zmeikapy, notebooks, parol, perevod_is, spamer_1_lvl, WARNING, run_button, parser
import webbrowser

def maw():
    class Mainwindiw(object):
        def __init__(self, main_win):
            self.label_1 = Label(main_win,
                                 text=f"Главное окно.\n Сейчас времени \n{datetime.now().replace(microsecond=0)}"
                                 , font=("Comic Sans MS", 35))
            # self.label_1.pack()
            self.but_1 = Button(main_win, text="Игра 'Змейка'", font=("Comic Sans MS", 15))
            self.but_2 = Button(main_win, text="Перевод числа в другие\n системы исчисления",
                                font=("Comic Sans MS", 15))
            self.but_3 = Button(main_win, text="Текстовый редактор", font=("Comic Sans MS", 15))
            self.but_4 = Button(main_win, text="Генератор паролей", font=("Comic Sans MS", 15))
            self.but_5 = Button(main_win, text="СПАМЕР, 1 уровень", font=("Comic Sans MS", 15))
            self.but_6 = Button(main_win, text="Нажми на кнопку", font=("Comic Sans MS", 15))
            self.but_7 = Button(main_win, text="Картотека", font=("Comic Sans MS", 15))

            self.label_1.pack()
            self.but_1.place(x=25, y=200)
            self.but_2.place(x=25, y=260)
            self.but_3.place(x=25, y=340)
            self.but_4.place(x=25, y=400)
            self.but_5.place(x=385, y=200)
            self.but_6.place(x=385, y=260)
            self.but_7.place(x=385, y=320)

            # self.label_1.pack()
            self.but_1.bind("<Button-1>", self.game)
            self.but_2.bind("<Button-1>", self.perevod)
            self.but_3.bind("<Button-1>", self.notebok)
            self.but_4.bind("<Button-1>", self.generate)
            self.but_5.bind("<Button-1>", self.spam_1)
            self.but_6.bind("<Button-1>", self.skamer)
            self.but_7.bind("<Button-1>", self.kart)

        def kart(self, event):
            root.destroy()
            parser.kartoteka()

        def game(self, event):
            root.destroy()
            zmeikapy.game_zmaika()

        def perevod(self, event):
            self.kek = messagebox.showinfo(")))))))))", "Приложение находится на доработке)")
            webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ",new=2)
        def notebok(self, event):
            root.destroy()
            notebooks.notbook()

        def generate(self, event):
            root.destroy()
            parol.gen_par()

        def spam_1(self, event):
            root.destroy()
            spamer_1_lvl.spamer1()

        def skamer(self, event):
            root.destroy()
            run_button.runbut()

    def close():
        cl = messagebox.askokcancel("Выход", "Вы точно хотите выйти?")
        if cl:
            messagebox.showinfo("Пока", "Удачи!)")
            root.destroy()

    root = Tk()
    root.resizable(width=False, height=False)
    root.protocol("WM_DELETE_WINDOW", close)
    root.geometry("600x500")
    w = Mainwindiw(root)
    root.mainloop()
