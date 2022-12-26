import sqlite3
from tkinter import ttk
import tkinter as tk
import tkinter.messagebox
from login_form import LoginForm
class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.init_main()
    def init_main(self):
        toolbar=tk.Frame(bg='green',bd=2)
        toolbar.pack(side=tk.TOP)

        btn_open_inf = tk.Button(toolbar,text="пользователи",command=self.open_dialog,compound=tk.TOP,height=3,width=12)
        btn_open_inf.pack(side=tk.LEFT)
        btn_open_inf = tk.Button(toolbar, text="персонал", command=self.open_dialog2, compound=tk.TOP,height=3,width=10)
        btn_open_inf.pack(side=tk.LEFT)
        btn_open_inf = tk.Button(toolbar, text="должность", command=self.open_dialog1, compound=tk.TOP,height=3,width=10)
        btn_open_inf.pack(side=tk.LEFT)
        btn = tk.Button(text="Login", command=self.open_login,height=5,width=15)
        btn.pack(pady=20, padx=50)

    def open_login(self):
        MainWindow()

    def open_dialog(self):
        Child()

    def open_dialog1(self):
        Child1()

    def open_dialog2(self):
        Child2()

class Child2(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.init_child()
        self.db=db
        self.records_2()

    def init_child(self):
        self.title('Информация бд персонал')
        self.geometry('800x350')
        self.resizable(False,False)
        self.tree=ttk.Treeview(self, columns=('ID','id_user','name','surname','id_post'),height=15,show='headings')
        self.tree.column('ID',width=150,anchor=tk.CENTER)
        self.tree.column('id_user',width=150,anchor=tk.CENTER)
        self.tree.column('name', width=150, anchor=tk.CENTER)
        self.tree.column('surname',width=150,anchor=tk.CENTER)
        self.tree.column('id_post', width=150, anchor=tk.CENTER)
        self.tree.heading('ID',text='ID')
        self.tree.heading('id_user', text='id_user')
        self.tree.heading('name',text='name')
        self.tree.heading('surname', text='surname')
        self.tree.heading('id_post',text='id_post')
        self.tree.pack()
        self.focus_set()

    def records_2(self):
        self.db.c.execute('''SELECT * FROM staff ''')
        [self.tree.insert('','end',values=row)for row in self.db.c.fetchall()]

class Child1(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.init_child()
        self.db=db
        self.records_1()

    def init_child(self):
        self.title('Информация бд должности')
        self.geometry('350x350')
        self.resizable(False,False)
        self.tree=ttk.Treeview(self, columns=('ID','post'),height=15,show='headings')
        self.tree.column('ID',width=150,anchor=tk.CENTER)
        self.tree.column('post', width=150, anchor=tk.CENTER)
        self.tree.heading('ID',text='ID')
        self.tree.heading('post', text='post')
        self.tree.pack()


    def records_1(self):
        self.db.c.execute('''SELECT * FROM post ''')
        [self.tree.insert('','end',values=row)for row in self.db.c.fetchall()]

class Child(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.init_child()
        self.db=db
        self.records()

    def init_child(self):
        self.title('Информация бд')
        self.geometry('650x300')
        self.resizable(False,False)

        self.tree=ttk.Treeview(self, columns=('ID','login','password','post'),height=15,show='headings')

        self.tree.column('ID',width=150,anchor=tk.CENTER)
        self.tree.column('login', width=150, anchor=tk.CENTER)
        self.tree.column('password', width=150, anchor=tk.CENTER)
        self.tree.column('post', width=150, anchor=tk.CENTER)

        self.tree.heading('ID',text='ID')
        self.tree.heading('login', text='login')
        self.tree.heading('password', text='password')
        self.tree.heading('post', text='post')

        self.tree.pack()
        self.focus_set()
    def records(self):
        self.db.c.execute('''SELECT * FROM users ''')
        [self.tree.insert('','end',values=row)for row in self.db.c.fetchall()]

class DB():
    def __init__(self):
        self.conn=sqlite3.connect("D:/pythonProject/f1/src/base.db")
        self.c=self.conn.cursor()
        self.conn.commit()
class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.open_login()

    def open_login(self):
        login_form = LoginForm()
        post = login_form.open()
        if post:
            print("Login ok")
        else:
            tk.messagebox.showerror(title="Wrong login",
                                          message="Логин или пароль не верны"
                                          )

if __name__ == '__main__':
    root = tk.Tk()
    db = DB()
    app=Main(root)
    app.pack()
    root.title("База формулы 1")
    root.geometry('400x200')
    root.resizable(False, False)
    root.mainloop()
