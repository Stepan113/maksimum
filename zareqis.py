import sqlite3 as sq
from tkinter import *
from tkinter import messagebox
import main_window as wm
import regis


class Zareqistration:
    def __init__(self, main):
        self.mian = main
        self.label = Label(main, text="Авторизация", font=("Comic Sans MS", 24))
        self.label_login = Label(main, text="Логин", font=("Comic Sans MS", 24))
        self.entry_login = Entry(main, font=("Times New Roman", 24))
        # Palace Script MT

        self.label_password = Label(main, text="Пароль", font=("Comic Sans MS", 24))
        self.entry_password = Entry(main, font=("Times New Roman", 24), show="*")
        self.button_accept = Button(main, text="Зарегистрироваться", font=("Comic Sans MS", 24))
        self.button_reqistr = Button(main, text="Уже регистрировались?", font=("Comic Sans MS", 24))

        self.label.pack()
        self.label_login.pack()
        self.entry_login.pack()
        self.label_password.pack()
        self.entry_password.pack()
        self.button_accept.pack()
        self.button_reqistr.pack()

        self.button_accept.bind("<Button-1>", self.zareqis)
        self.button_reqistr.bind("<Button-1>", self.regis)

        # self.login = str(self.entry_login.get())
        # self.password = str(self.entry_password.get())

    def zareqis(self, event):
        # pass
        login = str(self.entry_login.get())
        password = str(self.entry_password.get())
        login_fl = True if len(login) >= 6 else False
        password_fl = True if len(password) >= 8 else False
        if login_fl and password_fl:
            with sq.connect("table_2.db") as req:
                cur = req.cursor()
                cur.execute("""CREATE TABLE IF NOT EXISTS registration(
                    login TEXT,
                    password TEXT)""")
                cur.execute("""SELECT login FROM registration WHERE login=?""", (login,))
                req.commit()
                result = cur.fetchall()
                if len(result) == 0:
                    cur.execute("""INSERT INTO registration VALUES (?,?)""", (login, password))
                    req.commit()
                    self.mes_ok = messagebox.showinfo("Успешно!", "Вы успешно зарегистрировались!")
                    window.destroy()
                    wm.maw()
                    # self.main.destroy()
                else:
                    self.mes_not_ok = messagebox.showerror("Ошибка!", "Пользователь с таким именем уже существует")

        else:
            self.mes_not = messagebox.showerror("Ошибка", "Пароль должен содержать 8 символом, а логин-6")

    def regis(self, event):
        window.destroy()
        regis.reg()


window = Tk()
window.resizable(width=False, height=False)
q = Zareqistration(window)
window.mainloop()
