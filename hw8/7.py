from tkinter import *
from tkinter import messagebox, ttk
import mysql.connector as mysql
import re

names = []
passwords = []

db = mysql.connect(
    host = 'localhost',
    user = 'root',
    passwd = '78789',
    database = 'test'
)
cursor = db.cursor()

def check_password(password):
        if len(password) >= 6 and \
                re.search(r'[A-Z]', password) and \
                re.search(r'[a-z]', password) and \
                re.search(r'[@#$%^&*]', password) and \
                re.search(r'\d', password):
            return True
        else:
            return False

def information():
    query1 = 'SELECT name FROM users'
    cursor.execute(query1)
    name = cursor.fetchall()

    query2 = 'SELECT password FROM users'
    cursor.execute(query2)
    passw = cursor.fetchall()

    l = 0
    while l < len(name):
        passwords.append(passw[l][0])
        names.append(name[l][0])
        l += 1
    print(name)
    print(passwords)
    
def show_db():
    widget = Tk()
    widget.geometry('400x400')
    widget['bg'] = '#D8DCFF'
    information()
    tree = ttk.Treeview(widget, columns=('name'), show = 'headings')
    tree.heading("name", text='names')
    tree.pack()
    tree1 = ttk.Treeview(widget, columns=('passwords'), show='headings')
    tree1.heading('passwords', text = 'passwords')
    tree1.pack()
    for i in names:
        tree.insert("", END, values = i)
    for i in passwords:
        tree1.insert("", END, values=i)
    widget.mainloop()
    
def add_user():
    widget1 = Tk()
    widget1.geometry('400x400')
    widget1['bg'] = '#C5FFFD'
    widget1.title("Registration page")
    l0 = Label(widget1, bg ='#C5FFFD', text = 'Registrarion', fg = '#565676', font = ('Arial Black', 27))
    l0.place(relx = 0.2, rely = 0.1)
    l1 = Label(widget1, text = 'Name', bg = '#C5FFFD', fg = '#565676', font = ("Verdana", 13))
    l1.place(relx = 0.1, rely = 0.28)
    l2 = Label(widget1, text = 'Password', bg = '#C5FFFD', fg = '#565676', font = ("Verdana", 13))
    l2.place(relx = 0.1, rely = 0.38)

    e1 = Entry(widget1, font=("Arial", 13), fg = '#565676')
    e1.pack()
    e1.place(relx = 0.5, rely = 0.29)
    e2 = Entry(widget1, font=("Arial", 13), fg = '#565676')
    e2.pack()
    e2.place(relx = 0.5, rely = 0.39)
        
    def creator():
        a = e1.get()
        b = e2.get()
        values = (a, b)

        if check_password(b):
            cursor.execute('INSERT INTO users (name, password) VALUES (%s, %s)', values)
            db.commit()
            widget1.destroy()
            messagebox.showinfo("Success", 'New account created')

    go = Button(widget1, text='GO!', command = creator, bg = ['#88D9E6'], width=15)
    go.pack()
    go.place(relx = 0.37, rely = 0.8)
    widget1.mainloop()
    
def change_name():
    information()
    widget2 = Tk()
    widget2.geometry('400x400')
    widget2['bg'] = '#C5FFFD'
    l0 = Label(widget2, bg ='#C5FFFD', text = 'Registrarion', fg = '#565676', font = ('Arial Black', 27))
    l0.place(relx = 0.2, rely = 0.1)
    l1 = Label(widget2, text = 'Old Name', bg = '#C5FFFD', fg = '#565676', font = ("Verdana", 13))
    l1.place(relx = 0.1, rely = 0.28)
    l2 = Label(widget2, text = 'New Name', bg = '#C5FFFD', fg = '#565676', font = ("Verdana", 13))
    l2.place(relx = 0.1, rely = 0.38)
    l3 = Label(widget2, text = 'Password', bg = '#C5FFFD', fg = '#565676', font = ("Verdana", 13))
    l3.place(relx = 0.1, rely = 0.48)

    e3 = Entry(widget2, font=("Arial", 13), fg = '#565676')
    e3.pack()
    e3.place(relx = 0.5, rely = 0.29)
    e4 = Entry(widget2, font=("Arial", 13), fg = '#565676')
    e4.pack()
    e4.place(relx = 0.5, rely = 0.39)
    e_1 = Entry(widget2, font=("Arial", 13), fg = '#565676')
    e_1.pack()
    e_1.place(relx = 0.5, rely = 0.49)

    def name():
        old = e3.get()
        new = e4.get()
        passw= e_1.get()
        if old in names and passw in passwords:
            cursor.execute('UPDATE users SET name = %s WHERE name = %s', (new, old))
            messagebox.showinfo("Success", 'New name setted')
        else:
            messagebox.showinfo("Error", 'Something went wrong')
        
    go = Button(widget2, text='GO!', command = name, bg = ['#88D9E6'], width=15)
    go.pack()
    go.place(relx = 0.37, rely = 0.8)
    widget2.mainloop()
    
    
def change_passwd():
    information()
    widget3 = Tk()
    widget3.geometry('400x400')
    widget3['bg'] = '#C5FFFD'
    l0 = Label(widget3, bg ='#C5FFFD', text = 'Registrarion', fg = '#565676', font = ('Arial Black', 27))
    l0.place(relx = 0.2, rely = 0.1)
    l3 = Label(widget3, text = 'Name', bg = '#C5FFFD', fg = '#565676', font = ("Verdana", 13))
    l3.place(relx = 0.1, rely = 0.28)
    l1 = Label(widget3, text = 'Old Password', bg = '#C5FFFD', fg = '#565676', font = ("Verdana", 13))
    l1.place(relx = 0.1, rely = 0.38)
    l2 = Label(widget3, text = 'New Password', bg = '#C5FFFD', fg = '#565676', font = ("Verdana", 13))
    l2.place(relx = 0.1, rely = 0.48)
    

    e5 = Entry(widget3, font=("Arial", 13), fg = '#565676')
    e5.pack()
    e5.place(relx = 0.5, rely = 0.39)
    e6 = Entry(widget3, font=("Arial", 13), fg = '#565676')
    e6.pack()
    e6.place(relx = 0.5, rely = 0.49)
    e7 = Entry(widget3, font=("Arial", 13), fg = '#565676')
    e7.pack()
    e7.place(relx = 0.5, rely = 0.29)

    def passwrd():
        n = e7.get()
        old = e5.get()
        new = e6.get()
        if old in passwords and check_password(new) and n in names:
            cursor.execute('UPDATE users SET password = %s WHERE password = %s', (new, old))
            messagebox.showinfo("Success", 'New password setted')
        else:
            messagebox.showinfo("Error", 'Something went wrong')
        
    go = Button(widget3, text='GO!', command = passwrd, bg = ['#88D9E6'], width=15)
    go.pack()
    go.place(relx = 0.37, rely = 0.8)
    widget3.mainloop()


root = Tk()
root.title('Authorization page')
root.geometry('500x500')
root['bg'] = '#AB81CD'

labell = Label(root, text = 'Database', font = ('Arial Black', 30), bg = '#AB81CD', fg = '#F1E3E4').place(relx = 0.15, rely = 0.2)
b1 = Button(root, text='Show database', font=('Verdana', 15), bg = '#574AE2' , command=show_db, fg = '#F1E3E4', width=25, height=2)
b1.pack()
b1.place(relx = 0.16, rely = 0.45)

b2 = Button(root, text='Add user', font=('Verdana', 15), bg = '#222A68' , command=add_user, fg = '#F1E3E4', width=25, height=2)
b2.pack()
b2.place(relx = 0.16, rely = 0.55)

b3 = Button(root, text='Change name', font=('Verdana', 15), bg = '#574AE2' , command=change_name, fg = '#F1E3E4', width=25, height=2)
b3.pack()
b3.place(relx = 0.16, rely = 0.65)

b4 = Button(root, text='Change password', font=('Verdana', 15), bg = '#574AE2' , command=change_passwd, fg = '#F1E3E4', width=25, height=2)
b4.pack()
b4.place(relx = 0.16, rely = 0.75)

root.mainloop()

# def login():
#     widget = Tk()
#     widget.geometry('400x400')
#     widget['bg'] = '#D8DCFF'
#     widget.title("Log in page")
#     l1 = Label(widget, text = 'Login', bg = '#D8DCFF', fg = '#565676', font=("Verdana", 15))
#     l1.place(relx = 0.11, rely = 0.45)
#     l2 = Label(widget, text = 'Password', bg = '#D8DCFF', fg = '#565676', font=("Verdana", 15))
#     l2.place(relx = 0.07, rely = 0.55)
#     e1 = Entry(widget, font=("Arial", 15), fg = '#565676')
#     e1.place(relx = 0.35, rely = 0.46)
#     e2 = Entry(widget, font=("Arial", 15), fg = '#565676', show='•')
#     e2.place(relx = 0.35, rely = 0.56)

#     def checker():
#         information()
#         if e1.get() in logins and e2.get() in passwords:
#             widget.destroy()
#             messagebox.showinfo('Success!', 'You entered system successfully!')
        
#             root.destroy()
#             new_window()
#         else:
#             widget.destroy()
#             messagebox.showerror('ERROR!','Incorrect user name or password!')
#     go = Button(widget, text='GO!', bg = '#565676', fg = '#D8DCFF', command = checker, width=20)
#     go.pack()
#     go.place(relx = 0.3, rely = 0.7)
#     #imag = ImageTk.PhotoImage(Image.open('avatar.jpg'))
#     #l0 = Label(widget, image=imag)
#     #l0.place(relx = 0.2, rely = 0.2)
#     widget.mainloop()

# def reg():
#     widget1 = Tk()
#     widget1.geometry('400x400')
#     widget1['bg'] = '#C5FFFD'
#     widget1.title("Registration page")
#     l0 = Label(widget1, bg ='#C5FFFD', text = 'Registrarion', fg = '#565676', font = ('Arial Black', 27))
#     l0.place(relx = 0.2, rely = 0.1)
#     l1 = Label(widget1, text = 'Name', bg = '#C5FFFD', fg = '#565676', font = ("Verdana", 13))
#     l1.place(relx = 0.1, rely = 0.28)
#     l2 = Label(widget1, text = 'Phone number', bg = '#C5FFFD', fg = '#565676', font = ("Verdana", 13))
#     l2.place(relx = 0.1, rely = 0.38)
#     l20 = Label(widget1, text = "Address", bg = '#C5FFFD', fg = '#565676', font = ('Verdana', 13))
#     l20.place(relx = 0.1, rely = 0.48)
#     l3 = Label(widget1, text = 'Login', bg = '#C5FFFD', fg = '#565676', font = ("Verdana", 13))
#     l3.place(relx = 0.1, rely = 0.58)
#     l4 = Label(widget1, text = 'Password', bg = '#C5FFFD', fg = '#565676', font = ("Verdana", 13))
#     l4.place(relx = 0.1, rely = 0.68)
#     e1 = Entry(widget1, font=("Arial", 13), fg = '#565676')
#     e1.pack()
#     e1.place(relx = 0.5, rely = 0.29)
#     e2 = Entry(widget1, font=("Arial", 13), fg = '#565676')
#     e2.pack()
#     e2.place(relx = 0.5, rely = 0.39)
#     e20 = Entry(widget1, font=("Arial", 13), fg = '#565676')
#     e20.pack()
#     e20.place(relx = 0.5, rely = 0.49)
#     e3 = Entry(widget1, font=("Arial", 13), fg = '#565676')
#     e3.pack
#     e3.place(relx = 0.5, rely = 0.59)
#     e4 = Entry(widget1, font=("Arial", 13), fg = '#565676')
#     e4.pack()
#     e4.place(relx = 0.5, rely = 0.69)
#     def creator():
#         information()
#         if e3.get() not in logins and e2.get() not in numbers:
#             a = e1.get()
#             b = e2.get()
#             b0 = e20.get()
#             c = e3.get()
#             d = e4.get()            
#             values = (a, b, c, d, b0)
#             cursor.execute('INSERT INTO info (name, number,login, password, address) VALUES (%s, %s, %s, %s, %s)', values)
#             db.commit()
#             widget1.destroy()
#             messagebox.showinfo("Success", 'New account created')
#             print(values)
#             #root.destroy()
#             #new_window()
#         else:
#             messagebox.showerror("ERROR!", "Such accout already exist!")
#     go = Button(widget1, text='GO!', command = creator, bg = ['#88D9E6'], width=15)
#     go.pack()
#     go.place(relx = 0.37, rely = 0.8)
#     widget1.mainloop()

# root = Tk()
# root.title('Authorization page')
# root.geometry('500x500')
# root['bg'] = '#AB81CD'

# labell = Label(root, text = 'Database', font = ('Arial Black', 30), bg = '#AB81CD', fg = '#F1E3E4').place(relx = 0.15, rely = 0.2)
# b1 = Button(root, text='Sign in', font=('Verdana', 15), bg = '#574AE2' , command=login, fg = '#F1E3E4', width=25, height=2)
# b1.pack()
# b1.place(relx = 0.16, rely = 0.45)
# b2 = Button(root, text='Sign up', font=('Verdana', 15), bg = '#222A68' , command=reg, fg = '#F1E3E4', width=25, height=2)
# b2.pack()
# b2.place(relx = 0.16, rely = 0.65)

# root.mainloop()