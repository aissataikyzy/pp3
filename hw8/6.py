from tkinter import *
from tkinter import messagebox
import re

def show_db():
    with open('database.txt', 'r') as file:
        all_data = file.read()
    messagebox.showinfo("Database Contents", all_data)

def add_user_window():
    def add_user():
        name = name_entry.get()
        password = password_entry.get()

        if not name or not password:
            messagebox.showerror("Error", "Name and password are required.")
            return

        if check_password(password):
            with open("database.txt", "r") as file:
                lines = file.readlines()
                for line in lines:
                    if line.startswith(name + ":"):
                        messagebox.showerror("Error", "A user with the same name already exists. Please choose another name.")
                        return

            new_user_line = name + ":" + password + "\n"
            with open("database.txt", "a") as file:
                file.write(new_user_line)
            messagebox.showinfo("Success", f"User {name} added successfully!")

            name_entry.delete(0, END)
            password_entry.delete(0, END)
        else:
            messagebox.showerror("Error", "Wrong password format.")

    window = Tk()
    window.title('Add User')
    window.geometry('200x200')

    name_label = Label(window, text='Name:')
    name_label.pack()
    name_entry = Entry(window)
    name_entry.pack()

    password_label = Label(window, text='Password:')
    password_label.pack()
    password_entry = Entry(window, show='*')
    password_entry.pack()

    add_button = Button(window, text='Add User', command=add_user)
    add_button.pack()


def change_name_window():
    def verify_password_and_change_name():
        name = name_entry.get()
        password = password_entry.get()

        if not name or not password:
            messagebox.showerror("Error", "Name and password are required.")
            return

        with open("database.txt", "r") as file:
            lines = file.readlines()

        found = False
        for line in lines:
            if line.startswith(name + ":") and line[len(name) + 1:].strip() == password:
                found = True
                break

        if found:
            open_name_change_window()
        else:
            messagebox.showerror("Error", "Incorrect name or password.")

    def open_name_change_window():
        change_name_window = Tk()
        change_name_window.title('Change Name')
        change_name_window.geometry('300x200')

        old_name_label = Label(change_name_window, text='Old Name:')
        old_name_label.pack()
        old_name_entry = Entry(change_name_window)
        old_name_entry.pack()

        new_name_label = Label(change_name_window, text='New Name:')
        new_name_label.pack()
        new_name_entry = Entry(change_name_window)
        new_name_entry.pack()

        def change_name():
            old_name = old_name_entry.get()
            new_name = new_name_entry.get()

            if not old_name or not new_name:
                messagebox.showerror("Error", "Old Name and New Name are required.")
                return

            with open("database.txt", "r") as file:
                lines = file.readlines()

            found = False
            for i, line in enumerate(lines):
                if line.startswith(old_name + ":"):
                    new_user_line = new_name + line[len(old_name):]
                    lines[i] = new_user_line
                    found = True
                    break

            if found:
                with open("database.txt", "w") as file:
                    file.writelines(lines)
                messagebox.showinfo("Success", "Name updated successfully!")
                old_name_entry.delete(0, END)
                new_name_entry.delete(0, END)
            else:
                messagebox.showerror("Error", "User not found.")

        change_button = Button(change_name_window, text='Change Name', command=change_name)
        change_button.pack()

    verify_password_window = Tk()
    verify_password_window.title('Verify Password')
    verify_password_window.geometry('300x200')

    name_label = Label(verify_password_window, text='Name:')
    name_label.pack()
    name_entry = Entry(verify_password_window)
    name_entry.pack()

    password_label = Label(verify_password_window, text='Password:')
    password_label.pack()
    password_entry = Entry(verify_password_window, show='*')
    password_entry.pack()

    verify_button = Button(verify_password_window, text='Verify Password', command=verify_password_and_change_name)
    verify_button.pack()

def change_password_window():
    def change_password():
        name = name_entry.get()
        old_password = old_password_entry.get()
        new_password = new_password_entry.get()

        if not name or not old_password or not new_password:
            messagebox.showerror("Error", "Name, Old Password, and New Password are required.")
            return

        with open("database.txt", "r") as file:
            lines = file.readlines()

        found = False
        for i, line in enumerate(lines):
            if line.startswith(name + ":") and line[len(name) + 1:] == old_password + "\n":
                lines[i] = name + ":" + new_password + "\n"
                found = True
                break

        if found:
            with open("database.txt", "w") as file:
                file.writelines(lines)
            messagebox.showinfo("Success", "Password updated successfully!")
            name_entry.delete(0, END)
            old_password_entry.delete(0, END)
            new_password_entry.delete(0, END)
        else:
            messagebox.showerror("Error", "User not found or incorrect old password.")

    change_password_window = Tk()
    change_password_window.title('Change Password')
    change_password_window.geometry('300x200')

    name_label = Label(change_password_window, text='Name:')
    name_label.pack()
    name_entry = Entry(change_password_window)
    name_entry.pack()

    old_password_label = Label(change_password_window, text='Old Password:')
    old_password_label.pack()
    old_password_entry = Entry(change_password_window, show='*')
    old_password_entry.pack()

    new_password_label = Label(change_password_window, text='New Password:')
    new_password_label.pack()
    new_password_entry = Entry(change_password_window, show='*')
    new_password_entry.pack()

    change_button = Button(change_password_window, text='Change Password', command=change_password)
    change_button.pack()

def check_password(password):
    if len(password) >= 6 and \
            re.search(r'[A-Z]', password) and \
            re.search(r'[a-z]', password) and \
            re.search(r'[@#$%^&*]', password) and \
            re.search(r'\d', password):
        return True
    else:
        return False

top = Tk()
top.title('Database')
top.geometry('400x400')
L1 = Label(top, text="Welcome to the users database!")
L1.pack()

button1 = Button(top, text='Show DB', command=show_db)
button1.pack()
button2 = Button(top, text='Add User', command=add_user_window)
button2.pack()
button3 = Button(top, text='Change Name', command=change_name_window)
button3.pack()
button4 = Button(top, text='Change Password', command=change_password_window)
button4.pack()

top.mainloop()

