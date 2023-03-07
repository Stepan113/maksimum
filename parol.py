import random
from tkinter import *
from tkinter import messagebox
from Proekt import main_window


# font=("Comic Sans MS",25)
def gen_par():
    class Randomizer:
        def __init__(self, main):
            self.label = Label(main, text="Рандомайзер паролей", font=("Comic Sans MS", 24))
            # self.label_1=Label(main,text="Сгенерировать пароль",font=("Times New Roman",24))
            self.label_1 = Label(main, text=f"Сгенерированный пароль:", font=("Comic Sans MS", 24))
            self.button = Button(main, text="Сгенерировать пароль", font=("Comic Sans MS", 24))
            self.copy_button = Button(main, text="Скопировать пароль в консоль", font=("Comic Sans MS", 24))

            self.label.pack()
            self.label_1.pack()
            self.button.pack()
            self.copy_button.pack()

            self.button.bind("<Button-1>", self.randomizer)
            self.copy_button.bind("<Button-1>", self.copy)

        def copy(self, event):
            cop = self.label_1["text"]
            if cop == "Сгенерированный пароль:":
                self.mes = messagebox.showerror("Ошибка", "Копировать нечего(")
            else:
                print(cop)

        def randomizer(self, event):
            alphabet = "abcdefghigklmnopqrstuwxyz"
            number = "0123456789"
            znak = "@#$%^&*()/*-+"
            password = ""
            while len(password) <= 8:
                random_num = random.choice(number)
                random_znak = random.choice(znak)
                random_alp = random.choice(alphabet)
                password += random_znak
                password += random_num
                password += random_alp

            self.label_1["text"] = password

    def close():
        clos = messagebox.askokcancel("Выход", "Вы точно хотите выйти?")
        if clos:
            window.destroy()
            main_window.maw()

    window = Tk()
    window.resizable(height=False, width=False)
    window.title("Рандомайзер")
    q = Randomizer(window)
    window.protocol("WM_DELETE_WINDOW", close)
    window.mainloop()
