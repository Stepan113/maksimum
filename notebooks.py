from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from Proekt import main_window


def notbook():
    def change_theme(theme):
        text_fild["bg"] = view_colors[theme]["text_bg"]
        text_fild["fg"] = view_colors[theme]["text_fg"]
        text_fild["insertbackground"] = view_colors[theme]["cursor"]
        text_fild["selectbackground"] = view_colors[theme]["select_bg"]

    def change_fonts(fontss):
        text_fild["font"] = fonts[fontss]["font"]

    def close():
        answer = messagebox.askokcancel("Выход", "Вы точно хотите выйти? ")
        if answer:
            window.destroy()
            main_window.maw()

    def open():
        file_path = filedialog.askopenfilename(title="Выбор файла",
                                               filetypes=(
                                               ('Текстовые документы (*.txt)', '*.txt'), ('Все файлы', '*.*')))
        if file_path:
            text_fild.delete('1.0', END)
            text_fild.insert('1.0', open(file_path, encoding="utf-8").read())

    def save():
        file_path = filedialog.asksaveasfilename(
            filetypes=(('Текстовые документы (*.txt)', '*.txt'), ('Все файлы', '*.*')))
        f = open(file_path, "w", encoding="utf-8")
        text = text_fild.get('1.0', END)
        f.write(text)
        f.close()

    window = Tk()
    window.title("Текстовый редактор")
    window.geometry("600x700")

    view_colors = {
        "dark": {
            "text_bg": "black", "text_fg": "lime", "cursor": "brown", "select_bg": "gray"
        },
        "light": {
            "text_bg": "white", "text_fg": "black", "cursor": "red", "select_bg": "green"
        }
    }

    fonts = {
        "Arial": {
            "font": "Arial"
        },
        "Times New Roman": {
            "font": ("Times New Roman", 14, "bold")
        },
        "CSMS": {
            "font": ("Comic Sans MS", 14, "bold")
        }
    }

    main_menu = Menu(window)
    window.config(menu=main_menu)

    file_menu = Menu(main_menu, tearoff=0)
    file_menu.add_command(label="Открыть", command=open)
    file_menu.add_command(label="Сохранить", command=save)
    file_menu.add_separator()
    file_menu.add_command(label="Закрыть", command=close)
    window.config(menu=file_menu)

    # dolbannoe menu
    view_menu = Menu(main_menu, tearoff=0)
    view_menu_sub = Menu(view_menu, tearoff=0)
    font_menu_sub = Menu(view_menu, tearoff=0)
    view_menu_sub.add_command(label="Светлая", command=lambda: change_theme("light"))
    view_menu_sub.add_command(label="Темная", command=lambda: change_theme("dark"))
    view_menu.add_cascade(label="Тема", menu=view_menu_sub)
    # view_menu.add_command(label="Тема")
    # view_menu.add_command(label="Шрифт")
    # shrift
    font_menu_sub.add_command(label="Arial", command=lambda: change_fonts("Arial"))
    font_menu_sub.add_command(label="Comic Sans MS", command=lambda: change_fonts("CSMS"))
    font_menu_sub.add_command(label="Times New Roman", command=lambda: change_fonts("Times New Roman"))
    view_menu.add_cascade(label="Шрифт...", menu=font_menu_sub)
    window.config(menu=view_menu)

    main_menu.add_cascade(label="Файл", menu=file_menu)
    main_menu.add_cascade(label="Вид", menu=view_menu)
    window.config(menu=main_menu)

    window.config(menu=main_menu)

    f_text = Frame(window)
    f_text.pack(fill=BOTH, expand=1)

    text_fild = Text(f_text, bg="black", fg="lime", padx=10, pady=10,
                     wrap=WORD, insertbackground="brown", selectbackground="grey",
                     spacing3=10, width=30, font=("Times New Roman", 14))
    text_fild.pack(expand=1, fill=BOTH, side=LEFT)
    scroll = Scrollbar(f_text, command=text_fild.yview)
    scroll.pack(side=LEFT, fill=Y)
    text_fild.config(yscrollcommand=scroll.set)

    window.protocol("WM_DELETE_WINDOW", close)
    window.mainloop()
