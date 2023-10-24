from tkinter import *

top = Tk()
L1 = Label(top, text="Welcome to the users database!")
L1.pack()

def take_db():
    with open ('db.txt', 'r') as file:
        all = file.read()
        print(all)

def nw():
    window = Tk()
    L2 = Label(window, text="What would you like to do?")
    L2.pack()

    def show_db():
        window1 = Tk()
        L3 = Label(window1, text="What would you like to do?")
        L3.pack()

    button1 = Button(window, text='show db', command = show_db)
    button1.pack()
    window.mainloop()

button = Button(top, text='Start',  command = nw)
button.pack()
top.mainloop()