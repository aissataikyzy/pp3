from tkinter import *
import numpy as np
from PIL import ImageTk, Image
import random

row1 = []
row2 = []
row3 = []

def matrix_entr():        
    def three():
        def get_matrix(event):
            row1.append(int(e.get())) 
            row1.append(int(e1.get()))
            row1.append(int(e2.get()))
            row2.append(int(e3.get()))
            row2.append(int(e4.get()))
            row2.append(int(e5.get()))
            row3.append(int(e6.get()))
            row3.append(int(e7.get()))
            row3.append(int(e8.get()))
            global A 
            A = np.array([row1, row2, row3])
            SVD(window)

        for i in window.winfo_children():
            i.destroy()

        e = Entry(window, width = 3)
        e.pack()
        e.place(relx = 0.1, rely = 0.1)

        e1 = Entry(window, width = 3)
        e1.pack()
        e1.place(relx = 0.2, rely = 0.1)

        e2 = Entry(window, width = 3)
        e2.pack()
        e2.place(relx = 0.3, rely = 0.1)

        e3 = Entry(window, width =3)
        e3.pack()
        e3.place(relx = 0.1, rely = 0.2)

        e4 = Entry(window, width = 3)
        e4.pack()
        e4.place(relx = 0.2, rely = 0.2)

        e5 = Entry(window, width = 3)
        e5.pack()
        e5.place(relx = 0.3, rely = 0.2)

        e6 = Entry(window, width = 3)
        e6.pack()
        e6.place(relx = 0.1, rely = 0.3)

        e7 = Entry(window, width = 3)
        e7.pack()
        e7.place(relx = 0.2, rely = 0.3)

        e8 = Entry(window, width = 3)
        e8.pack()
        e8.place(relx = 0.3, rely = 0.3)

        c_button = Button(window, text = 'Calculate')
        c_button.pack()
        c_button.place(relx = 0.13, rely = 0.4)
        c_button.bind('<Button - 1>', get_matrix)

    def two():
        def get_matrix(event):
            row1.append(int(e1.get()))
            row1.append(int(e2.get()))
            row2.append(int(e3.get()))
            row2.append(int(e4.get()))
            global A
            A = np.array([row1, row2])
            SVD(window)

        for i in window.winfo_children():
            i.destroy()

        e1 = Entry(window, width = 3)
        e1.pack()
        e1.place(relx = 0.1, rely = 0.1)

        e2 = Entry(window, width = 3)
        e2.pack()
        e2.place(relx = 0.2, rely = 0.1)

        e3 = Entry(window, width = 3)
        e3.pack()
        e3.place(relx = 0.1, rely = 0.2)

        e4 = Entry(window, width = 3)
        e4.pack()
        e4.place(relx = 0.2, rely  = 0.2)

        c_button = Button(window, text = 'Calculate')
        c_button.pack()
        c_button.place(relx = 0.1, rely = 0.3)
        c_button.bind('<Button - 1>', get_matrix)

    root.destroy()
    window = Tk()
    window.geometry('300x300')
    window.title('SVD calculator')

    buttn1 = Button(window, text = 'Enter 2x2 matrix', command = two, font = ('Courier New', 15), bg = '#FACA5D', fg = '#1A3259')
    buttn1.pack()
    buttn1.place(relx = 0.13, rely = 0.3)
    buttn2 = Button(window, text = 'Enter 3x3 matrix', command = three, font = ('Courier New', 15), bg = '#FACA5D', fg = '#1A3259')
    buttn2.pack()
    buttn2.place(relx = 0.13, rely = 0.55)
    

    window.mainloop()


def SVD(window):
    global B, U, V, D
    def z5(a):
        if a < 0:
            b = 5 - a     
            return b%5
        elif isinstance(a, int) == False:
            b = int(a*10)
            while (a*b)%5 == 1:
                b += 1
            return (a*b)%5
        return a%5

    def det_2(a):
        return a[0][0]*a[1][1] - a[0][1]*a[1][0]

    def minor(a, i, j):
        b = [row for k, row in enumerate(a) if k != i]
        b = [col for k, col in enumerate(zip(*b)) if k != j]
        return b

    def Det(a):
        if len(a) == 2:
            return det_2(a)
        return sum(((-1)**j)*a[0][j]*Det(minor(a, 0, j))
                for j in range(len(a)))

    def Norm(v):
        sqs = 0
        for i in v:
            sqs += (i**2)
        return np.sqrt(sqs)
    
    def rel_err(x1, x0):
        return abs((x1 - x0)/x1)*100

    def ev(a):
        x = np.array([[random.random() for i in range(len(a))]])
        max_iter = 10
        old_eigval = 0
        tlr = 0.5
        for i in range(max_iter):
            x = np.dot(a, x.T)
            eigval = Norm(x.T)
            error = rel_err(eigval, old_eigval)
            x = x/eigval
            e, res = [eigval, x]
            if tlr < 0.5:
                break
            old_eigval = eigval
        return e, res

    B = A.T@A
    eig, V = ev(B)

    if len(A) == 2:
        u0 = A@V[:, 0]/Norm(A@V[:, 0])
        u1 = A@V[:, 1]/Norm(A@V[:, 1])
        U = np.array([u0, u1])
    else:
        u0 = A@V[:, 0]/Norm(A@V[:, 0])
        u1 = A@V[:, 1]/Norm(A@V[:, 1])
        u2 = A@V[:, 2]/Norm(A@V[:, 2])
        U = np.array([u0, u1, u2])
    U = U.T
    

    D = np.round(U.T@A@V, decimals = 5)
    D = np.where(np.eye(D.shape[0], dtype=bool), D, 0)

    # SVD is U*D*V_transpose
    
    window.destroy()
    widget = Tk()
    widget.geometry(['800x300'])
    la1 = Label(widget, text = 'A = U*D*V^T').grid(row = 0, columnspan=3)
    la2 = Label(widget, text = U).grid(row = 1, column= 0)
    la3 = Label(widget, text = D).grid(row = 1, column= 1)
    la4 = Label(widget, text = V).grid(row = 1, column= 3)
    bttn = Button(widget, text = 'Enter another matrix', command=matrix_entr).pack()
    bttn1 = Button(widget, text = 'Show step-by-step solution', command=show_step_by_step_sol).pack()
    widget.mainloop()
    
def show_step_by_step_sol():
    pass

root = Tk()
root.title('SVD calculator')
root.geometry('300x300')
root['bg'] = '#DD7736'

img = ImageTk.PhotoImage(Image.open('pic.jpg'))
lbl = Label(root, image = img, bg = '#FEFCE6').place(relx = 0.23, rely = 0.38)

label = Label(root, text = ' Singular Value \nDecomposition', font = ('Elephant', 20), bg = '#FEFCE6', fg = '#1A3259').place(relx = 0.132, rely = 0.1)
button = Button(root, text = 'Enter your matrix', command = matrix_entr, font = ('Courier New', 15), bg = '#FACA5D', fg = '#1A3259')
button.pack()
button.place(relx = 0.13, rely = 0.76)

root.mainloop()

