from tkinter import *

root = Tk()
root.title('Текстовое поле')
root.geometry('500x500')
root.resizable(width=False, height=False)

root['bg']='black'

#l1 = Label(root, text='1', font='15', fg='black', bg='red', width=8, height=4).pack(expand=1, fill=Y)
l1 = Label(root, text='Привет', fg='white', bg='brown', padx=20, pady=20)
l1.place(x=10, y=10)
root.mainloop()