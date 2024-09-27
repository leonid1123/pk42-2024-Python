from tkinter import *
from tkinter import ttk
import sotrudnik

sotrudnikList = []


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
        s1 = sotrudnik.Sotrudnik(email, fname, name, sname, login, password)
        sotrudnikList.append(s1)
        itemList.delete(0, itemList.size())
        for item in sotrudnikList:
            #print(item.name)
            itemList.insert(0, item.getAllInfo())
    else:
        resLabel["text"] = "ТЫ ПОЧТУ МОЖЕШЬ\nНОРМАЛЬНО НАПИСАТЬ!?!"


root = Tk()  # создаем корневой объект - окно
root.title("Приложение ПАРОЛЬ")  # устанавливаем заголовок окна
root.geometry("700x450")  # устанавливаем размеры окна

ttk.Style().configure("TButton", padding=6, relief="flat",
                      background="#ccc", font="Arial 14")
ttk.Style().configure("TEntry", padding=6, relief="flat", font="Arial 16")
ttk.Style().configure("TLabel", padding=6, relief="flat", font="Arial 14")

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
itemList = Listbox(width=80)
searchField = ttk.Entry(width=35)

emailLable.pack(anchor=W, padx=5)
itemList.pack(anchor=N, side=RIGHT)
emailEntry.pack(anchor=W, padx=5)
nameLable.pack(anchor=W, padx=5)
nameEntry.pack(anchor=W, padx=5)
fnameLable.pack(anchor=W, padx=5)
fnameEntry.pack(anchor=W, padx=5)
snameLable.pack(anchor=W, padx=5)
snameEntry.pack(anchor=W, padx=5)
btn.pack(anchor=W, pady=6, padx=55)
resLabel.pack(anchor=W, padx=5)
searchField.place(x=220, y=210)
root.mainloop()
