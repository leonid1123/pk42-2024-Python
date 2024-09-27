from tkinter import *
from tkinter import ttk
import sotrudnik


def myfun():
    if emailEntry.get().find("@") != -1 and len(nameEntry.get()) > 0 and len(fnameEntry.get()) > 0 and len(
            snameEntry.get()) > 0:
        email = emailEntry.get().strip()
        name = nameEntry.get().strip()
        fname = fnameEntry.get().strip()
        sname = snameEntry.get().strip()
        login = email[:email.find("@")]
        password = name[0] + name[len(name) - 1] + fname[0] + fname[len(fname) - 1] + sname[0] + sname[len(sname) - 1]
        resLabel["text"] = f"Ваш логин: {login} \nВаш пароль: {password}"
        s1=sotrudnik.Sotrudnik()
    else:
        resLabel["text"] = "ТЫ ПОЧТУ МОЖЕШЬ\nНОРМАЛЬНО НАПИСАТЬ!?!"


root = Tk()  # создаем корневой объект - окно
root.title("Приложение ПАРОЛЬ")  # устанавливаем заголовок окна
root.geometry("300x450")  # устанавливаем размеры окна

ttk.Style().configure("TButton", padding=6, relief="flat",
                      background="#ccc", font="Arial")
ttk.Style().configure("TEntry", padding=6, relief="flat", font="Arial")
ttk.Style().configure("TLabel", padding=6, relief="flat", font="Arial")

emailEntry = ttk.Entry(width=35)
nameEntry = ttk.Entry(width=35)
fnameEntry = ttk.Entry(width=35)
snameEntry = ttk.Entry(width=35)
emailLable = ttk.Label(text="Укажите адрес почты")
nameLable = ttk.Label(text="Укажите имя")
fnameLable = ttk.Label(text="Укажите фамилию")
snameLable = ttk.Label(text="Укажите отчество")
btn = ttk.Button(text="Внести", command=myfun)
resLabel = ttk.Label(text="Ваш логин: \nВаш пароль:")

emailLable.pack()
emailEntry.pack()
nameLable.pack()
nameEntry.pack()
fnameLable.pack()
fnameEntry.pack()
snameLable.pack()
snameEntry.pack()
btn.pack(pady=6)
resLabel.pack()

root.mainloop()
