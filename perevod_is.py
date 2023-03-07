from tkinter import *
from tkinter import messagebox
from Proekt import main_window

def perevodchik():
    class Vert:
        def __init__(self,main):
            self.label=Label(main,text="Перевод числа из 10 системы исчисления в 2-9 системы",
                             font=("Comic Sans MS",30),bg="black",fg="white")
            self.entry_1=Entry(main,font=("Comic Sans MS",30),bg="black",fg="white")
            self.entry_2=Entry(main,font=("Comic Sans MS",30),bg="black",fg="white")
            self.button=Button(main,text="Рассчитать",font=("Comic Sans MS",30))

            self.label.pack()
            self.entry_1.pack()
            self.entry_2.pack()
            self.button.pack()

            self.button.bind("<Button-1>",self.click)

        def click(self,event):
            try:
                self.a=int(self.entry_1.get())
                self.w=int(self.entry_2.get())
                if 2<self.w<9:
                    self.mes=messagebox.showerror("Ошибка","Неправильный ввод")
                self.n=""
                # self.kwhite
                while self.a>0:
                    self.n+=str(self.a%self.w)
                    self.a//=self.w
                self.n=list(reversed(self.n))
                for j in range(len(self.n)):
                    self.k+=self.n[j]
                self.mes=messagebox.showinfo("Ответ",f"Ваш ответ {self.k}")
            except ValueError:
                self.mes=messagebox.showinfo("Ответ","Неправильный ввод")

    def close():
        clos=messagebox.askokcancel("Выход","Вы точно хотите выйти? ")
        if clos:
            window.destroy()
            # main_window.maw()

    window=Tk()
    window.protocol("WM_DELETE_WINDOW",close)
    window["bg"]="black"
    q=Vert(window)


# perevodchik()
# https://disk.yandex.ru/d/JFq6QmmbagX7kg
# Вопрос максимально короткий и понятный. Как сделать проверку на запись в таблице?
# Например: у нас есть какая-то запись в бд. И мы хотим добавить в эту таблицу запись
# Как я это делаю: INSERT INTO нужная мне таблица VALUES (значения, которые надо добавить)
# Но вот вопрос: а если такая запись уже есть в таблице? Как на это сделать проврку в самом INSERT INTO
# И еще один вопрос: можно ли как-то перенести дедлаин проекта? Просто есть ощущение, что не успею написать(