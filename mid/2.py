from tkinter import *

root = Tk()
root.title('Счетчик кликов')
root.geometry('200x200')
root.resizable(width=False, height=False)

count=0

def clicked():
    global count
    count+=1
    Click.configure(text=count)

Click = Label(root, text='0', font='Arial 35')
Click.pack()

btn = Button(root, text='Кликни на меня', padx='20', pady='20', command=clicked)
btn.pack()

root.mainloop()