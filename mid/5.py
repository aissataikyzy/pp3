from tkinter import *
from datetime import *

temp=0
after_id=''

def tick():
    global temp, after_id
    after_id = root.after(1000, tick)
    f_temp = datetime.fromtimestamp(temp).strftime("%M:%S")
    l1.configure(text=str(f_temp))
    temp += 1

def start_tick():
    btnstart.pack_forget()
    btnstop.pack()
    tick()

def stop_tick():
    btnstop.pack_forget()
    btncontinue.pack()
    btnreset.pack()
    root.after_cancel(after_id)

def cont_tick():
    btncontinue.pack_forget()
    btnreset.pack_forget()
    btnstop.pack()
    tick()

def reset_tick():
    global temp
    temp=0
    l1.configure(text='00:00')
    btncontinue.pack_forget()
    btnreset.pack_forget()
    btnstart.pack()

root = Tk()
root.title('Секундамер')
root.resizable(width=False, height=False)
root.geometry('300x200')

l1 = Label(root, text='00:00', font=('Comic Sans MS', 30), width=10)
l1.pack()

btnstart = Button(root, text='Start', font=('Comic Sans MS', 20), width=15, command=start_tick)
btnstop = Button(root, text='Stop', font=('Comic Sans MS', 20), width=15, command=stop_tick)
btncontinue = Button(root, text='Continue', font=('Comic Sans MS', 20), width=15, command=cont_tick)
btnreset = Button(root, text='Reset', font=('Comic Sans MS', 20), width=15, command=reset_tick)

btnstart.pack()

root.mainloop()