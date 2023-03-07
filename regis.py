from tkinter import *
import sqlite3 as sq
from tkinter import messagebox
import main_window as wm


def reg():
    class Registrations:
        def __init__(self, main):
            self.label_login_1 = Label(main, text="Логин", font=("Comic Sans MS", 24))
            self.entry_login_1 = Entry(main, font=("Times New Roman", 24))
            self.label_password_1 = Label(main, text="Пароль", font=("Comic Sans MS", 24))
            self.entry_password_1 = Entry(main, font=("Times New Roman", 24), show="*")
            self.button_1 = Button(main, text="Войти", font=("Comic Sans MS", 24))

            self.label_login_1.pack()
            self.entry_login_1.pack()
            self.label_password_1.pack()
            self.entry_password_1.pack()
            self.button_1.pack()

            self.button_1.bind("<Button-1>", self.regis)

            # self.login_1 = str(self.entry_login_1.get())
            # self.password_1 = str(self.entry_password_1.get())

        def regis(self, event):
            login_1 = str(self.entry_login_1.get())
            password_1 = str(self.entry_password_1.get())
            with sq.connect("table_2.db") as reg:
                cur_1 = reg.cursor()
                cur_1.execute("""SELECT login FROM registration WHERE login=? AND password=?""", (login_1, password_1))
                reg.commit()
                result_1 = cur_1.fetchall()
                if len(result_1) == 1:
                    self.mes = messagebox.showinfo("Успешно!", "Вы успешно вошли в систему ")
                    window_1.destroy()
                    wm.maw()
                else:
                    self.mes_not_ok = messagebox.showerror("Ошибка", "Такого пользователя не существует")

    def close():
        window_1.destroy()

    window_1 = Tk()
    window_1.resizable(width=False,height=False)
    window_1.geometry("400x250")
    window_1.protocol("WM_DELETE_WINDOW", close)
    q = Registrations(window_1)
    window_1.mainloop()
