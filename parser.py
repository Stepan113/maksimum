from tkinter import *
import sqlite3 as sq
from tkinter import messagebox
from Proekt import main_window

def kartoteka():
    class Kartoteka:
        def __init__(self, main):
            self.label = Label(main, text="Это Ваша личная картотека",font=("Comic Sans MS",25))
            self.label_name = Label(main, text="Введите имя человека",font=("Comic Sans MS",25))
            self.entry_name = Entry(main,font=("Comic Sans MS",25))
            self.label_number = Label(main, text="Введите номер человека",font=("Comic Sans MS",25))
            self.entry_number = Entry(main,font=("Comic Sans MS",25))
            self.label_city = Label(main, text="Введите город",font=("Comic Sans MS",25))
            self.entry_city = Entry(main,font=("Comic Sans MS",25))
            self.button_accept = Button(main, text="Принять",font=("Comic Sans MS",25))
            self.button_show = Button(main, text="Показать картотеку",font=("Comic Sans MS",25))

            self.label.pack()
            self.label_name.pack()
            self.entry_name.pack()
            self.label_number.pack()
            self.entry_number.pack()
            self.label_city.pack()
            self.entry_city.pack()
            self.button_accept.pack()
            self.button_show.pack()

            self.button_accept.bind("<Button-1>", self.accept)
            self.button_show.bind("<Button-1>", self.show)

        def accept(self, event):
            try:
                name = str(self.entry_name.get()).lower()
                number = int(self.entry_number.get())
                city = str(self.entry_city.get()).lower()
                alphabet = "абвгдеёжзийклмопрстуфхцчшщъыьэюя"
                # num="0123456789!@№#;$%^:&?*()_+=/-+\/|<>';:~`"
                name_flag = False if name.isdigit() else 0
                city_flag = False if city.isdigit() else 0
                if len(str(number)) == 11 and len(name) >= 3 and (name_flag == False) and (city_flag == False):
                    with sq.connect("table_2.db") as acc:
                        cur = acc.cursor()
                        cur.execute("""CREATE TABLE IF NOT EXISTS kartoteka(
                            name TEXT,
                            number INTEGER,
                            city TEXT)""")
                        cur.execute("""SELECT * FROM kartoteka WHERE name=? AND number=? AND city=?""",
                                    (name, number, city))
                        result = cur.fetchall()
                        if len(result) == 0:
                            cur.execute("""INSERT INTO kartoteka VALUES (?,?,?)""", (name, number, city))
                            acc.commit()
                            self.mes_ok = messagebox.showinfo("Успешно", "Данные были успешно занесены")
                        else:
                            self.mes = messagebox.showerror("Ошибка", "Такой пользователь уже есть в картотеке")
                else:
                    self.mes_not = messagebox.showerror("Ошибка", "Неправильный ввод данных")


            except ValueError:
                self.mes = messagebox.showerror("Ошибка", "Неверный ввод данных")

        def show(self, event):
            def close():
                root.destroy()
                kartoteka()

            window.destroy()
            with sq.connect("table_2.db") as acc:
                cur = acc.cursor()
                cur.execute("""SELECT * FROM kartoteka""")
                res = cur.fetchall()
                len_res = len(res)
                root = Tk()
                root.resizable(height=False, width=False)
                total_rows = len(res)
                total_columns = len(res[0])
                for i in range(total_rows):
                    for j in range(total_columns):
                        self.lab = Label(root, text=f"{res[i][j]}",font=("Comic Sans MS",25))
                        self.lab.grid(row=i, column=j)
                root.protocol("WM_DELETE_WINDOW", close)
                root.mainloop()

    def close():
        window.destroy()
        main_window.maw()

    window = Tk()
    window.resizable(width=False,height=False)
    window.protocol("WM_DELETE_WINDOW", close)
    q = Kartoteka(window)
    window.mainloop()
# kartoteka()