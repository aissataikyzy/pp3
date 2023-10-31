from tkinter import *

root = Tk()
root.title('Тестовое приложение')
root.geometry('1280x720')
root.resizable(width=False, height=False)

root['bg']='black'

def add():
    e.insert(END, ' Hello ')

def de_l():
    e.delete(0, END)

def get():
    Label1['text']=e.get()

e = Entry(root, show="*")
e.pack()

e.insert(0,'Hello')
e.insert(END,' world')

btn1 = Button(root, font = 'Arial 15', text='insert', command=add)
btn1.pack()

btn2 = Button(root, font = 'Arial 15', text='delete', command=de_l)
btn2.pack()

btn3 = Button(root, font = 'Arial 15', text='get')
btn3.pack()

Label1= Label(root, bg='black', fg='white')
Label1.pack()

root.mainloop()