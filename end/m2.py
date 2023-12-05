from tkinter import *
from tkinter import ttk
import numpy as np
import sympy
from sympy import * 
main_window = Tk()
main_window.geometry("900x750+20+20")
main_window.config(background="#16b775")
def add_matrix():
    window = Frame(main_window,background="#16b775")
    window.place(y=0,x=0,width=900,height=750)
    text_var1 = []
    entries1 = []
    text_var2 = []
    entries2 = []
    # frame = Tk()
    Button(window,text="Main menu",command=main).place(x=790,y=650)
    def get():
        Button(window,text="Заново",command=add_matrix).place(x=790,y=700)
        size = ttk.Combobox(window, width = 5, values=[1,2,3,4,5,6,7,8,9,10],state="readonly")
        size.place(x=46,y=56)
        size2 = ttk.Combobox(window, width = 5, values=[1,2,3,4,5,6,7,8,9,10],state="readonly")
        size2.place(x=110,y=56) 

        
        def matrix():
            x1 = 0
            y1 = 0
            x2 = 0
            y2 = 0
            rows,cols = (int(size.get()),int(size2.get()))
            sizes = []
            sizes.append(rows)
            sizes.append(cols)
            max_n = max(sizes)
            for i in range(rows):
                text_var1.append([])
                entries1.append([])
                for j in range(cols):
                    text_var1[i].append(StringVar())
                    entries1[i].append(Entry(window, textvariable=text_var1[i][j],width=3,font=50))
                    entries1[i][j].place(x=45 + x1, y=100 + y1)
                    x1 += 35
                y1 += 35
                x1 = 0
                def get_mat1():
                    matrix = []
                    for i in range(rows):
                        matrix.append([])
                        for j in range(cols):
                            matrix[i].append(text_var1[i][j].get())
                    return (matrix) 
            for i in range(rows):
                text_var2.append([])
                entries2.append([])
                for j in range(cols):
                    text_var2[i].append(StringVar())
                    entries2[i].append(Entry(window, textvariable=text_var2[i][j],width=3,font=50))
                    entries2[i][j].place(x=430 + x2, y=100 + y2)
                    x2 += 35
                y2 += 35
                x2 = 0
                def get_mat2():
                    matrix = []
                    for i in range(rows):
                        matrix.append([])
                        for j in range(cols):
                            matrix[i].append(text_var2[i][j].get())
                    return (matrix) 
                
                # b = get_mat2()
                def q():
                    def dest_brack(M):
                        s = [[str(e) for e in row] for row in M]
                        lens = [max(map(len, col)) for col in zip(*s)]
                        fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
                        table = [fmt.format(*row) for row in s]
                        r = '\n'.join(table)
                        return r
                    win_solution = Tk()
                    win_solution.config(background="#16b775")
                    win_solution.geometry("900x750+20+20")

                    frame_1 = Frame(win_solution)
                    frame_2 = Frame(win_solution)
                    frame_3 = Frame(win_solution)
                    frame_1.grid(row=0,column=0)
                    frame_2.grid(row=1,column=0)
                    frame_3.grid(row=2,column=0)
                    e = []
                    e1 = []
                    a=(get_mat1())
                    b=(get_mat2())
                    for x,i, in enumerate(a):
                        for k,j, in enumerate(i):
                            a[x][k] = int(j)
                    for x,i, in enumerate(b):
                        for k,j, in enumerate(i):
                            b[x][k] = int(j)
                    for i,j in zip(a,b):
                        for k,l in zip(i,j):
                            new_l = f'{k}+{l}'
                            e1.append(new_l)
                            new_s = k+l
                            e.append(new_s)
                    e1 =np.array(e1)
                    e = np.array(e)
                    e = np.array(e.reshape(rows,cols))
                    e1 = e1.reshape(rows,cols)  
                    print(e)
                    print(e1)
                    n = int(60/max_n)
                    Label(frame_1,text="Your input",font=f'Times {n}').grid(row=0,column=0,columnspan=3)
                    # for i,j in zip(a,b):
                    Label(frame_1,text=dest_brack(a),font=f'Times {n}',background='#16b775').grid(row=1,column=0)
                    Label(frame_1,text="    ",font=f'Times {n}').grid(row=1,column=1)
                    Label(frame_1,text=dest_brack(b),font=f'Times {n}',background='#16b775').grid(row=1,column=2)
                    Label(frame_2,text="Answer",font=f'Times {n}').grid(row=0,column=2)
                    # for z in e:
                    Label(frame_2,text=dest_brack(e),font=f'Times {n}',background='#16b775').grid(row=1,column=2)
                    Label(frame_3,text="Step By step",font=f'Times {n}').grid(row=0,column=3)
                    # for x in e1:
                    Label(frame_3,text=dest_brack(e1),font=f'Times {n}',background='#16b775').grid(row=1,column=3)
                    win_solution.mainloop()
            u = Button(window,text='Submit',command=lambda:(q(),u.destroy()),background="#128277")
            u.place(x=180,y=56)
        b = Button(window,text="Select",command=lambda:(matrix(),b.destroy()))
        b.place(x=46,y=80)
    button = Button(window,text="Start",command=lambda:(get(),button.destroy()))
    button.place(x=46,y = 80)    
def matrix_multiplication():
    window = Frame(main_window,width=900,height=750)
    window.config(background="#16b775")
    window.place(x=0,y=0)
    frame = Frame(window)
    frame.place(x=50,y=450)
    text_var1 = []
    entries1 = []
    text_var2 = []
    entries2 = []

    size = ttk.Combobox(window, width = 5, values=[1,2,3,4,5,6,7,8,9,10],state="readonly")
    size2 = ttk.Combobox(window, width = 5, values=[1,2,3,4,5,6,7,8,9,10],state="readonly")
    size.place(x=46,y=56)
    size2.place(x=110,y=56) 
    Button(window,text="Main menu",command=main).place(x=800,y=650)
    Button(window,text="Заново",command=matrix_multiplication).place(x=800,y=700)   
    def get():
        
        # print(size.get(),size2.get())
        size1 = ttk.Combobox(window, width = 5,values =size2.get(), textvariable=size2.get(),state="readonly")
        size_2 = ttk.Combobox(window, width = 5, values=[1,2,3,4,5,6,7,8,9,10],state="readonly")
        size1.place(x=380,y=56)
        size_2.place(x=444,y=56) 
        sizes = []
        x2 = 0
        y2 = 0
        rows, cols = (int(size.get()),int(size2.get()))
        sizes.append(rows)
        sizes.append(cols)
        for i in range(rows):
            text_var1.append([])
            entries1.append([])
            for j in range(cols):
                text_var1[i].append(StringVar())
                entries1[i].append(Entry(window, textvariable=text_var1[i][j],width=3))
                entries1[i][j].place(x=45 + x2, y=100 + y2)
                x2 += 30
            y2 += 30
            x2 = 0
        def get_mat1():
                matrix = []
                for i in range(rows):
                    matrix.append([])
                    for j in range(cols):
                        matrix[i].append(text_var1[i][j].get())
                return matrix
        def get1():#print
            x2 = 0
            y2 = 0
            rows, cols = (int(size1.get()),int(size_2.get()))
            sizes.append(rows)
            sizes.append(cols)
            max_n = max(sizes)
            for i in range(rows):
                text_var2.append([])
                entries2.append([])
                for j in range(cols):
                    text_var2[i].append(StringVar())
                    entries2[i].append(Entry(window, textvariable=text_var2[i][j],width=3))
                    entries2[i][j].place(x=380 + x2, y=100 + y2)
                    x2 += 30
                y2 += 30
                x2 = 0
                def get_mat2():
                    matrix = []
                    for i in range(rows):
                        matrix.append([])
                        for j in range(cols):
                            matrix[i].append(text_var2[i][j].get())
                    return matrix
            a = get_mat1()
            b = get_mat2()
            
            
            def func_chunk(lst, n):
                for x in range(0, len(lst), n):
                    e_c = lst[x : n + x]

                    if len(e_c) < n:
                        e_c = e_c + [None for y in range(n - len(e_c))]
                    yield e_c
            for x,i, in enumerate(a):
                for k,j, in enumerate(i):
                    a[x][k] = int(j)
            for x,i, in enumerate(b):
                for k,j, in enumerate(i):
                    b[x][k] = int(j)
            def submit():
                def dest_brack(M):
                        s = [[str(e) for e in row] for row in M]
                        lens = [max(map(len, col)) for col in zip(*s)]
                        fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
                        table = [fmt.format(*row) for row in s]
                        r = '\n'.join(table)
                        return r
                win_solution = Tk()
                win_solution.config(background="#16b775")
                win_solution.geometry("900x750+20+20")

                frame_1 = Frame(win_solution)
                frame_2 = Frame(win_solution)
                frame_3 = Frame(win_solution)
                frame_1.pack()
                frame_2.pack()
                frame_3.pack()
                m2 = []
                matrix = []
                result = [[sum(f*g for f,g in zip(E_row, R_col)) for R_col in zip(*b)] for E_row in a]
                # for z in result:
                #     print(z)
                #     Label(frame_1,text=z,font= 200).pack()
                for E_row in a:
                    for R_col in zip(*b):
                        for f,g in zip(E_row,R_col):
                            if g<0:
                                v = f'({f}*({g}))'
                            else:
                                v = f'({f}*{g})'
                            # print(f'{f}*{g}')
                            matrix.append((f*g))
                            m2.append(v)

                m2 = (np.array(m2))
                matrix = (np.array(matrix))
                p = (list(func_chunk(m2.tolist(),int(size1.get()))))
                o = []
                n = int(60/max_n)
                for t in p:
                    o.append("+".join(t))
                Label(frame_1,text="Your input",font=f'Times {n}').grid(row=0,column=0,columnspan=3)
                    # for i,j in zip(a,b):
                Label(frame_1,text=dest_brack(a),font=f'Times {n}',background='#16b775').grid(row=1,column=0)
                Label(frame_1,text="    ",font=f'Times {n}').grid(row=1,column=1)
                Label(frame_1,text=dest_brack(b),font=f'Times {n}',background='#16b775').grid(row=1,column=2)
                Label(frame_2,text="Answer",font=f'Times {n}').grid(row=0,column=2)
                
                Label(frame_2,text=dest_brack(np.array(result)),font=f'Times {n}',background='#16b775').grid(row=1,column=2)
                Label(frame_3,text="Step By step",font=f'Times {n}').pack()
                if int(size_2.get()) == 1:
                    for i in o:
                        Label(frame_3,text=i,font=f'Times {n}').pack()
                if int(size_2.get()) == 2:
                    Label(frame_3,text=o[0:2],font=f'Times {n}').pack()
                    Label(frame_3,text=o[2:4],font=f'Times {n}').pack()
                if int(size_2.get()) == 3:
                    Label(frame_3,text=o[0:3],font=f'Times {n}').pack()
                    Label(frame_3,text=o[3:6],font=f'Times {n}').pack()
                    Label(frame_3,text=o[6:9],font=f'Times {n}').pack()
                if int(size_2.get()) == 4:
                    Label(frame_3,text=o[0:4],font=f'Times {n}').pack()
                    Label(frame_3,text=o[4:8],font=f'Times {n}').pack()
                    Label(frame_3,text=o[8:12],font=f'Times {n}').pack()
                    Label(frame_3,text=o[12:16],font=f'Times {n}').pack()
                if int(size_2.get()) == 5:
                    Label(frame_3,text=o[0:int(size_2.get())],font=f'Times {n}').pack()
                    Label(frame_3,text=o[int(size_2.get()):2*int(size_2.get())],font=f'Times {n}').pack()
                    Label(frame_3,text=o[2*int(size_2.get()):3*int(size_2.get())],font=f'Times {n}').pack()
                    Label(frame_3,text=o[3*int(size_2.get()):4*int(size_2.get())],font=f'Times {n}').pack()
                    Label(frame_3,text=o[4*int(size_2.get()):5*int(size_2.get())],font=f'Times {n}').pack()
                if int(size_2.get()) == 6:
                    Label(frame_3,text=o[0:int(size_2.get())],font=f'Times {n}').pack()
                    Label(frame_3,text=o[int(size_2.get()):2*int(size_2.get())],font=f'Times {n}').pack()
                    Label(frame_3,text=o[2*int(size_2.get()):3*int(size_2.get())],font=f'Times {n}').pack()
                    Label(frame_3,text=o[3*int(size_2.get()):4*int(size_2.get())],font=f'Times {n}').pack()
                    Label(frame_3,text=o[4*int(size_2.get()):5*int(size_2.get())],font=f'Times {n}').pack()
                    Label(frame_3,text=o[5*int(size_2.get()):6*int(size_2.get())],font=f'Times {n}').pack()
                if int(size_2.get()) == 7:
                    Label(frame_3,text=o[0:int(size_2.get())],font=f'Times {n}').pack()
                    Label(frame_3,text=o[int(size_2.get()):2*int(size_2.get())],font=f'Times {n}').pack()
                    Label(frame_3,text=o[2*int(size_2.get()):3*int(size_2.get())],font=f'Times {n}').pack()
                    Label(frame_3,text=o[3*int(size_2.get()):4*int(size_2.get())],font=f'Times {n}').pack()
                    Label(frame_3,text=o[4*int(size_2.get()):5*int(size_2.get())],font=f'Times {n}').pack()
                    Label(frame_3,text=o[5*int(size_2.get()):6*int(size_2.get())],font=f'Times {n}').pack()
                    Label(frame_3,text=o[6*int(size_2.get()):7*int(size_2.get())],font=f'Times {n}').pack()
                if int(size_2.get()) == 8:
                    Label(frame_3,text=o[0:int(size_2.get())],font=f'Times {n}').pack()
                    Label(frame_3,text=o[int(size_2.get()):2*int(size_2.get())],font=f'Times {n}').pack()
                    Label(frame_3,text=o[2*int(size_2.get()):3*int(size_2.get())],font=f'Times {n}').pack()
                    Label(frame_3,text=o[3*int(size_2.get()):4*int(size_2.get())],font=f'Times {n}').pack()
                    Label(frame_3,text=o[4*int(size_2.get()):5*int(size_2.get())],font=f'Times {n}').pack()
                    Label(frame_3,text=o[5*int(size_2.get()):6*int(size_2.get())],font=f'Times {n}').pack()
                    Label(frame_3,text=o[6*int(size_2.get()):7*int(size_2.get())],font=f'Times {n}').pack()
                    Label(frame_3,text=o[7*int(size_2.get()):8*int(size_2.get())],font=f'Times {n}').pack()
                if int(size_2.get()) == 9:
                    Label(frame_3,text=o[0:int(size_2.get())],font=f'Times {n}').pack()
                    Label(frame_3,text=o[int(size_2.get()):2*int(size_2.get())],font=f'Times {n}').pack()
                    Label(frame_3,text=o[2*int(size_2.get()):3*int(size_2.get())],font=f'Times {n}').pack()
                    Label(frame_3,text=o[3*int(size_2.get()):4*int(size_2.get())],font=f'Times {n}').pack()
                    Label(frame_3,text=o[4*int(size_2.get()):5*int(size_2.get())],font=f'Times {n}').pack()
                    Label(frame_3,text=o[5*int(size_2.get()):6*int(size_2.get())],font=f'Times {n}').pack()
                    Label(frame_3,text=o[6*int(size_2.get()):7*int(size_2.get())],font=f'Times {n}').pack()
                    Label(frame_3,text=o[7*int(size_2.get()):8*int(size_2.get())],font=f'Times {n}').pack()
                    Label(frame_3,text=o[8*int(size_2.get()):9*int(size_2.get())],font=f'Times {n}').pack()
                if int(size_2.get()) == 10:
                    Label(frame_3,text=o[0:int(size_2.get())],font=f'Times {n}').pack()
                    Label(frame_3,text=o[int(size_2.get()):2*int(size_2.get())],font=f'Times {n}').pack()
                    Label(frame_3,text=o[2*int(size_2.get()):3*int(size_2.get())],font=f'Times {n}').pack()
                    Label(frame_3,text=o[3*int(size_2.get()):4*int(size_2.get())],font=f'Times {n}').pack()
                    Label(frame_3,text=o[4*int(size_2.get()):5*int(size_2.get())],font=f'Times {n}').pack()
                    Label(frame_3,text=o[5*int(size_2.get()):6*int(size_2.get())],font=f'Times {n}').pack()
                    Label(frame_3,text=o[6*int(size_2.get()):7*int(size_2.get())],font=f'Times {n}').pack()
                    Label(frame_3,text=o[7*int(size_2.get()):8*int(size_2.get())],font=f'Times {n}').pack()
                    Label(frame_3,text=o[8*int(size_2.get()):9*int(size_2.get())],font=f'Times {n}').pack()
                    Label(frame_3,text=o[9*int(size_2.get()):10*int(size_2.get())],font=f'Times {n}').pack()
            u = Button(window,text="Submit",command=lambda:(submit(),u.destroy()))
            u.place(x=50,y=400)
        Button(window,text="select the size for the second matrix",command=get1).place(x=320,y = 20)
    first = Button(window,text="select the size for the first matrix",command=lambda:(get(),first.destroy()))
    first.place(x=20,y = 20)
def scalar_matrix_multiplication():
    window = Frame(main_window,width=900,height=750)
    window.config(background="#16b775")
    window.place(x=0,y=0)
    frame1 = Frame(window)
    frame1.place(x=50,y=450)
    text_var1 = []
    entries1 = []
    Button(window,text="Main menu",command=main).place(x=800,y=650)
    def get():
        Button(window,text="Заново",command=scalar_matrix_multiplication).place(x=790,y=700)
        size = ttk.Combobox(window, width = 5, values=[1,2,3,4,5,6,7,8,9,10],state="readonly")
        size.place(x=46,y=56)
        size2 = ttk.Combobox(window, width = 5, values=[1,2,3,4,5,6,7,8,9,10],state="readonly")
        size2.place(x=110,y=56) 
        Label(window,text="x",background='#16b775').place(x=100,y=56)
        Label(window,text="Size of matrix",width=16).place(x=46,y=30)
        Label(window,text="Scalar",width=5).place(x=250,y=30)
        entry = Entry(window,width=5)
        entry.place(x=250,y=56)
        def matrix():
            x1 = 0
            y1 = 0
            sizes = []
            rows,cols = (int(size.get()),int(size2.get()))
            sizes.append(rows)
            sizes.append(cols)
            max_n = max(sizes)
            for i in range(rows):
                text_var1.append([])
                entries1.append([])
                for j in range(cols):
                    text_var1[i].append(StringVar())
                    entries1[i].append(Entry(window, textvariable=text_var1[i][j],width=3))
                    entries1[i][j].place(x=45 + x1, y=100 + y1)
                    x1 += 30
                y1 += 30
                x1 = 0
                def get_mat1():
                    matrix = []
                    for i in range(rows):
                        matrix.append([])
                        for j in range(cols):
                            matrix[i].append(text_var1[i][j].get())
                    return (matrix) 
                def q():
                    
                    b = entry.get()
                    e = []
                    e1 = []
                    a=(get_mat1())
                    for i in a:
                        for k in i:
                            q = f'{int(k)}*{int(entry.get())}'
                            r = int(k)*int(entry.get())
                            e1.append(q)
                            e.append(r)
                    e = np.array(e)
                    e = (e.reshape(rows,cols))
                    e1 = np.array(e1)
                    e1 = e1.reshape(rows,cols) 
                    
                    for x in np.array(e):
                        Label(frame1,text=x,font=20).pack()
                    def step():
                        def dest_brack(M):
                            s = [[str(e) for e in row] for row in M]
                            lens = [max(map(len, col)) for col in zip(*s)]
                            fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
                            table = [fmt.format(*row) for row in s]
                            r = '\n'.join(table)
                            return r
                        win_solution = Tk()
                        win_solution.config(background="#16b775")
                        win_solution.geometry("900x750+20+20")
                        n = int(60/max_n)
                        frame_1 = Frame(win_solution,background='#16b775')
                        frame_2 = Frame(win_solution)
                        frame_3 = Frame(win_solution)
                        frame_1.pack()
                        frame_2.pack()
                        frame_3.pack()
                    # for x in np.array(e1):
                    #     Label(frame1,text=x,font=20).pack()
                        Label(frame_1,text="Your input",font=f'Times {n}').grid(row=0,column=0,columnspan=3)
                        # for i,j in zip(a,b):
                        Label(frame_1,text=dest_brack(np.array(a)),font=f'Times {n}',background='#16b775').grid(row=1,column=0)
                        Label(frame_1,text="    ",font=f'Times {n}').grid(row=1,column=1)
                        Label(frame_1,text=((b)),font=f'Times {n}',background='#16b775').grid(row=1,column=2)
                        Label(frame_2,text="Answer",font=f'Times {n}').grid(row=0,column=2)
                        # for z in e:
                        Label(frame_2,text=dest_brack(e),font=f'Times {n}',background='#16b775').grid(row=1,column=2)
                        Label(frame_3,text="Step By step",font=f'Times {n}').pack()
                        # for x in e1:
                        Label(frame_3,text=dest_brack(e1),font=f'Times {n}',background='#16b775').pack()
                        win_solution.mainloop()
                    Button(frame1,text="Show step",command=step).pack()
            u = Button(window,text='Submit',command=lambda:(q(),u.destroy()))
            u.place(x=180,y=56)
        b = Button(window,text="Select",command=lambda:(matrix(),b.destroy()))
        b.place(x=46,y=80)
    button = Button(window,text="Start",command=lambda:(get(),button.destroy()))
    button.place(x=46,y = 80)
def matrix_transpose():
    window = Frame(main_window,width=900,height=750)
    window.config(background="#16b775")
    window.place(x=0,y=0)
    frame = Frame(window,background="#16b775")
    frame.place(x=50,y=450)
    text_var1 = []
    entries1 = []
    Button(window,text="Main menu",command=main).place(x=790,y=650)
    def get():
        Button(window,text="Заново",command=matrix_transpose).place(x=790,y=700)
        Label(window,text="x",background='#16b775').place(x=100,y=56)
        Label(window,text="Size of matrix",width=16).place(x=46,y=30)
        size = ttk.Combobox(window, width = 5, values=[1,2,3,4,5,6,7,8,9,10],state="readonly")
        size.place(x=46,y=56)
        size2 = ttk.Combobox(window, width = 5, values=[1,2,3,4,5,6,7,8,9,10],state="readonly")
        size2.place(x=110,y=56) 
        def matrix():
            x1 = 0
            y1 = 0
            rows,cols = (int(size.get()),int(size2.get()))

            for i in range(rows):
                text_var1.append([])
                entries1.append([])
                for j in range(cols):
                    text_var1[i].append(StringVar())
                    entries1[i].append(Entry(window, textvariable=text_var1[i][j],width=3))
                    entries1[i][j].place(x=45 + x1, y=100 + y1)
                    x1 += 30
                y1 += 30
                x1 = 0
                def get_mat1():
                    matrix = []
                    for i in range(rows):
                        matrix.append([])
                        for j in range(cols):
                            matrix[i].append(text_var1[i][j].get())
                    return (matrix) 
            
                def q():
                    def dest_brack(M):
                        s = [[str(e) for e in row] for row in M]
                        lens = [max(map(len, col)) for col in zip(*s)]
                        fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
                        table = [fmt.format(*row) for row in s]
                        r = '\n'.join(table)
                        return r
                    a=(get_mat1())
                    a_t = [list(x) for x in zip(*a)]
                    Label(frame,text="Your input",font=("Arial", 14),background="#16b775").grid(row=0,column=0)
                    Label(frame,text=dest_brack(np.array(a)),font=("Arial", 14),background="#16b775").grid(row=1,column=0)
                    Label(frame,text="Transpose",font=("Arial", 14),background="#16b775").grid(row=0,column=2)
                    # for x in a_t:
                    Label(frame,text="=>",font=("Arial", 14),background="#16b775").grid(row=1,column=1)
                    Label(frame,text=dest_brack(a_t),font=("Arial", 14),background="#16b775").grid(row=1,column=2)
            u = Button(window,text='Submit',command=lambda:(q(),u.destroy()))
            u.place(x=180,y=56)
        b = Button(window,text="Select",command=lambda:(matrix(),b.destroy()))
        b.place(x=46,y=80)
    button = Button(window,text="Start",command=lambda:(get(),button.destroy()))
    button.place(x=46,y = 80)
def matrix_rank():
    window = Frame(main_window,width=900,height=750)
    window.config(background="#16b775")
    window.place(x=0,y=0)
    frame = Frame(window,background="#16b775")
    frame.place(x=50,y=450)
    text_var1 = []
    entries1 = []
    Button(window,text="Main menu",command=main).place(x=800,y=650)
    def get():
        Button(window,text="Заново",command=matrix_rank).place(x=790,y=700)
        Label(window,text="x",background='#16b775').place(x=100,y=56)
        Label(window,text="Size of matrix",width=16).place(x=46,y=30)
        size = ttk.Combobox(window, width = 5, values=[1,2,3,4,5,6,7,8,9,10],state="readonly")
        size.place(x=46,y=56)
        size2 = ttk.Combobox(window, width = 5, values=[1,2,3,4,5,6,7,8,9,10],state="readonly")
        size2.place(x=110,y=56) 
        def matrix():
            x1 = 0
            y1 = 0
            rows,cols = (int(size.get()),int(size2.get()))
            for i in range(rows):
                text_var1.append([])
                entries1.append([])
                for j in range(cols):
                    text_var1[i].append(StringVar())
                    entries1[i].append(Entry(window, textvariable=text_var1[i][j],width=3))
                    entries1[i][j].place(x=45 + x1, y=100 + y1)
                    x1 += 30
                y1 += 30
                x1 = 0
                def get_mat1():
                    matrix = []
                    for i in range(rows):
                        matrix.append([])
                        for j in range(cols):
                            matrix[i].append(text_var1[i][j].get())
                    return (matrix) 
            
                def q():
                    def dest_brack(M):
                        s = [[str(e) for e in row] for row in M]
                        lens = [max(map(len, col)) for col in zip(*s)]
                        fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
                        table = [fmt.format(*row) for row in s]
                        r = '\n'.join(table)
                        return r
                    a=(get_mat1())
                    M_rref = Matrix(a).rref()
                    cnt_r = 0
                    arr_of_rr = np.array(M_rref[0])
                    for x in arr_of_rr:
                        if sum(list(x)) != 0:
                            cnt_r+= 1
                    Label(frame,text="Rank of Matrix:",font=20).grid(row=0,column=0)
                    Label(frame,text=f'<{cnt_r}>',font=20,background="#16b775").grid(row=0,column=1)
                    Label(frame,text="because RREF form is",font=20).grid(row=1,column=0)
                    
                    Label(frame,text=dest_brack(arr_of_rr),font=20,background="#16b775").grid(row=1,column=1)
            u = Button(window,text='Submit',command=lambda:(q(),u.destroy()))
            u.place(x=180,y=56)
        b = Button(window,text="Select",command=lambda:(matrix(),b.destroy()))
        b.place(x=46,y=80)
    button = Button(window,text="Start",command=lambda:(get(),button.destroy()))
    button.place(x=46,y = 80)    

def det():
    window = Frame(main_window,width=900,height=750)
    window.config(background="#16b775")
    window.place(x=0,y=0)
    frame1 = Frame(window)
    frame1.place(x=50,y=300)
    text_var1 = []
    entries1 = []
    Button(window,text="Main menu",command=main).place(x=800,y=650)
    def get():
        Button(window,text="Заново",command=det).place(x=790,y=700)
        size = ttk.Combobox(window, width = 5, values=[1,2,3,4,5],state="readonly")
        size.place(x=46,y=56)
        Label(window,text="Size of matrix",width=16).place(x=46,y=30)
        def matrix():
            x1 = 0
            y1 = 0
            sizes = []
            rows,cols = (int(size.get()),int(size.get()))
            sizes.append(rows)
            sizes.append(cols)
            max_n = max(sizes)
            for i in range(rows):
                text_var1.append([])
                entries1.append([])
                for j in range(cols):
                    text_var1[i].append(StringVar())
                    entries1[i].append(Entry(window, textvariable=text_var1[i][j],width=3))
                    entries1[i][j].place(x=45 + x1, y=100 + y1)
                    x1 += 30
                y1 += 30
                x1 = 0
                def get_mat1():
                    matrix = []
                    for i in range(rows):
                        matrix.append([])
                        for j in range(cols):
                            matrix[i].append(int(text_var1[i][j].get()))
                    return (matrix) 
                def q():
                    
                    a = get_mat1()
                    if int(size.get()) == 1:
                        n = int(45/int(size.get()))
                        Label(frame1,text=a,font= f'Times {n}').pack()
                    if int(size.get()) == 2:
                        n = int(45/int(size.get()))
                        for_2 = (a[0])[0]*(a[1])[1]-(a[0])[1]*(a[1])[0]
                        for_2_step = f'[{(a[0])[0]}*{(a[1])[1]}]-[{(a[0])[1]}*{(a[1])[0]}] = {for_2}'
                        Label(frame1,text=for_2_step,font= f'Times {n}').pack()
                        print(for_2)
                    if int(size.get()) == 3:
                        # img = ImageTk.PhotoImage(Image.open("triangle_method1.png"))
                        # Label(i,image=img).pack()
                        n = int(45/int(size.get()))
                        def for_3(a):
                            for_3 = (((a[0])[0]*(a[1])[1] * (a[2])[2]) + ((a[0])[1]*(a[1])[2] * (a[2])[0]) + ((a[0])[2]*(a[1])[0] * (a[2])[1]))-( ((a[0])[2]*(a[1])[1] * (a[2])[0]) + ((a[0])[1]*(a[1])[0] * (a[2])[2]) + ((a[0])[0]*(a[1])[2] * (a[2])[1]) )
                            for_3_step = f'[({(a[0])[0]}*{(a[1])[1]} * {(a[2])[2]}) + ({(a[0])[1]}*{(a[1])[2]} * {(a[2])[0]}) + ({(a[0])[2]}*{(a[1])[0]} * {(a[2])[1]})] - [({(a[0])[2]}*{(a[1])[1]} * {(a[2])[0]}) + ({(a[0])[1]}*{(a[1])[0]} * {(a[2])[2]}) + ({(a[0])[0]}*{(a[1])[2]} * {(a[2])[1]})] = {for_3}'
                            return for_3_step
                        Label(frame1,text="With triangular method",font=f'Times {n}').pack()
                        Label(frame1,text=for_3(a),font=f'Times {n}').pack()
                        # print(for_3)
                    if int(size.get()) == 4:
                        def determinant(a):
                            n = int(45/int(size.get()))
                            def ind(n,m):
                                l = []
                                for i in range(len(a)):
                                    for j in range(len(a[i])):
                                        if i!=n and j != m:
                                            l.append((a[i][j]))
                                o = (np.array(l)).reshape(len(a)-1,len(a)-1)
                                p = []
                                for i in o:
                                    p.append(i)
                                return p
                            arr1 = ind(0,0)
                            arr2 = ind(0,1)
                            arr3 = ind(0,2)
                            arr4 = ind(0,3)

                            def for_3(a):
                                for_3 = (((a[0])[0]*(a[1])[1] * (a[2])[2]) + ((a[0])[1]*(a[1])[2] * (a[2])[0]) + ((a[0])[2]*(a[1])[0] * (a[2])[1]))-( ((a[0])[2]*(a[1])[1] * (a[2])[0]) + ((a[0])[1]*(a[1])[0] * (a[2])[2]) + ((a[0])[0]*(a[1])[2] * (a[2])[1]) )
                                for_3_step = f'[({(a[0])[0]}*{(a[1])[1]} * {(a[2])[2]}) + ({(a[0])[1]}*{(a[1])[2]} * {(a[2])[0]}) + ({(a[0])[2]}*{(a[1])[0]} * {(a[2])[1]})] - [({(a[0])[2]}*{(a[1])[1]} * {(a[2])[0]}) + ({(a[0])[1]}*{(a[1])[0]} * {(a[2])[2]}) + ({(a[0])[0]}*{(a[1])[2]} * {(a[2])[1]})] = {for_3}'
                                return for_3
                            def for_3_step(a):
                                for_3 = (((a[0])[0]*(a[1])[1] * (a[2])[2]) + ((a[0])[1]*(a[1])[2] * (a[2])[0]) + ((a[0])[2]*(a[1])[0] * (a[2])[1]))-( ((a[0])[2]*(a[1])[1] * (a[2])[0]) + ((a[0])[1]*(a[1])[0] * (a[2])[2]) + ((a[0])[0]*(a[1])[2] * (a[2])[1]) )
                                for_3_step = f'[({(a[0])[0]}*{(a[1])[1]} * {(a[2])[2]}) + ({(a[0])[1]}*{(a[1])[2]} * {(a[2])[0]}) + ({(a[0])[2]}*{(a[1])[0]} * {(a[2])[1]})] - [({(a[0])[2]}*{(a[1])[1]} * {(a[2])[0]}) + ({(a[0])[1]}*{(a[1])[0]} * {(a[2])[2]}) + ({(a[0])[0]}*{(a[1])[2]} * {(a[2])[1]})]'
                                
                                return for_3_step

                            mat1 = int(for_3(arr1))
                            mat2 = int(for_3(arr2))
                            mat3 = int(for_3(arr3))
                            mat4 = int(for_3(arr4))
                            step_mat1 = (for_3_step(arr1))
                            step_mat2 = (for_3_step(arr2))
                            step_mat3 = (for_3_step(arr3))
                            step_mat4 = (for_3_step(arr4))
                            sol_frame = Frame(frame1)
                            sol_frame.pack()
                            Label(sol_frame,text=f'{a[0][0]}*').grid(row=0,column=0)
                            Label(sol_frame,text=f'{a[0][1]}*').grid(row=0,column=3)
                            Label(sol_frame,text=f'{a[0][2]}*').grid(row=0,column=6)
                            Label(sol_frame,text=f'{a[0][3]}*').grid(row=0,column=9)
                            Label(sol_frame,text=(np.array(arr1))).grid(row=0,column=1)
                            Label(sol_frame,text=(np.array(arr2))).grid(row=0,column=4)
                            Label(sol_frame,text=(np.array(arr3))).grid(row=0,column=7)
                            Label(sol_frame,text=(np.array(arr4))).grid(row=0,column=10)
                            Label(sol_frame,text='-').grid(row=0,column=2)
                            Label(sol_frame,text='+').grid(row=0,column=5)
                            Label(sol_frame,text='-').grid(row=0,column=8)
                            solution = a[0][0]*mat1-a[0][1]*mat2 + a[0][2]*mat3 - a[0][3]*mat4
                            solution2 = f'{a[0][0]}*{(np.array(arr1))}-{a[0][1]}*{(np.array(arr2))} + {a[0][2]}*{(np.array(arr3))} - {a[0][3]}*{(np.array(arr4))}'
                            # print(a[0][0]*mat1-a[0][1]*mat2 + a[0][2]*mat3 - a[0][3]*mat4 )
                            step = f'{a[0][0]}*{step_mat1}-\n{a[0][1]}*{step_mat2} + \n{a[0][2]}*{step_mat3} - \n{a[0][3]}*{step_mat4} = {solution}'
                            print(f'({a[0][0]}*{step_mat1}-{a[0][1]}*{step_mat2} + {a[0][2]}*{step_mat3} - {a[0][3]}*{step_mat4} = {solution} )')
                            # Label(frame1,text=solution2,font=f'Times {n}').pack()
                            Label(frame1,text=step,font=f'Times {n}').pack()
                        determinant(a)                      
                    if int(size.get()) == 5:
                            def determinant5(a):
                                n = int(45/int(size.get()))
                                def determinant4(a):
                                    def ind(n,m):
                                        l = []
                                        for i in range(len(a)):
                                            for j in range(len(a[i])):
                                                if i!=n and j != m:
                                                    l.append((a[i][j]))
                                        o = (np.array(l)).reshape(len(a)-1,len(a)-1)
                                        p = []
                                        for i in o:
                                            p.append(i)
                                        return p
                                    arr1 = ind(0,0)
                                    arr2 = ind(0,1)
                                    arr3 = ind(0,2)
                                    arr4 = ind(0,3)

                                    def for_3(a):
                                        for_3 = (((a[0])[0]*(a[1])[1] * (a[2])[2]) + ((a[0])[1]*(a[1])[2] * (a[2])[0]) + ((a[0])[2]*(a[1])[0] * (a[2])[1]))-( ((a[0])[2]*(a[1])[1] * (a[2])[0]) + ((a[0])[1]*(a[1])[0] * (a[2])[2]) + ((a[0])[0]*(a[1])[2] * (a[2])[1]) )
                                        for_3_step = f'[({(a[0])[0]}*{(a[1])[1]} * {(a[2])[2]}) + ({(a[0])[1]}*{(a[1])[2]} * {(a[2])[0]}) + ({(a[0])[2]}*{(a[1])[0]} * {(a[2])[1]})] - [({(a[0])[2]}*{(a[1])[1]} * {(a[2])[0]}) + ({(a[0])[1]}*{(a[1])[0]} * {(a[2])[2]}) + ({(a[0])[0]}*{(a[1])[2]} * {(a[2])[1]})] = {for_3}'
                                        return for_3
                                    def for_3_step(a):
                                        for_3 = (((a[0])[0]*(a[1])[1] * (a[2])[2]) + ((a[0])[1]*(a[1])[2] * (a[2])[0]) + ((a[0])[2]*(a[1])[0] * (a[2])[1]))-( ((a[0])[2]*(a[1])[1] * (a[2])[0]) + ((a[0])[1]*(a[1])[0] * (a[2])[2]) + ((a[0])[0]*(a[1])[2] * (a[2])[1]) )
                                        for_3_step = f'[({(a[0])[0]}*{(a[1])[1]} * {(a[2])[2]}) + ({(a[0])[1]}*{(a[1])[2]} * {(a[2])[0]}) + ({(a[0])[2]}*{(a[1])[0]} * {(a[2])[1]})] - [({(a[0])[2]}*{(a[1])[1]} * {(a[2])[0]}) + ({(a[0])[1]}*{(a[1])[0]} * {(a[2])[2]}) + ({(a[0])[0]}*{(a[1])[2]} * {(a[2])[1]})]'
                                        
                                        return for_3_step

                                    mat1 = int(for_3(arr1))
                                    mat2 = int(for_3(arr2))
                                    mat3 = int(for_3(arr3))
                                    mat4 = int(for_3(arr4))
                                    step_mat1 = (for_3_step(arr1))
                                    step_mat2 = (for_3_step(arr2))
                                    step_mat3 = (for_3_step(arr3))
                                    step_mat4 = (for_3_step(arr4))

                                    solution = a[0][0]*mat1-a[0][1]*mat2 + a[0][2]*mat3 - a[0][3]*mat4

                                    # print(a[0][0]*mat1-a[0][1]*mat2 + a[0][2]*mat3 - a[0][3]*mat4 )
                                    # print(f'({a[0][0]}*{step_mat1}-{a[0][1]}*{step_mat2} + {a[0][2]}*{step_mat3} - {a[0][3]}*{step_mat4} = {solution} )')
                                    return solution

                                def determinant4_for_step(a):

                                    def ind(n,m):
                                        l = []
                                        for i in range(len(a)):
                                            for j in range(len(a[i])):
                                                if i!=n and j != m:
                                                    l.append((a[i][j]))
                                        o = (np.array(l)).reshape(len(a)-1,len(a)-1)
                                        p = []
                                        for i in o:
                                            p.append(i)
                                        return p
                                    arr1 = ind(0,0)
                                    arr2 = ind(0,1)
                                    arr3 = ind(0,2)
                                    arr4 = ind(0,3)

                                    def for_3(a):
                                        for_3 = (((a[0])[0]*(a[1])[1] * (a[2])[2]) + ((a[0])[1]*(a[1])[2] * (a[2])[0]) + ((a[0])[2]*(a[1])[0] * (a[2])[1]))-( ((a[0])[2]*(a[1])[1] * (a[2])[0]) + ((a[0])[1]*(a[1])[0] * (a[2])[2]) + ((a[0])[0]*(a[1])[2] * (a[2])[1]) )
                                        for_3_step = f'[({(a[0])[0]}*{(a[1])[1]} * {(a[2])[2]}) + ({(a[0])[1]}*{(a[1])[2]} * {(a[2])[0]}) + ({(a[0])[2]}*{(a[1])[0]} * {(a[2])[1]})] - [({(a[0])[2]}*{(a[1])[1]} * {(a[2])[0]}) + ({(a[0])[1]}*{(a[1])[0]} * {(a[2])[2]}) + ({(a[0])[0]}*{(a[1])[2]} * {(a[2])[1]})] = {for_3}'
                                        return for_3
                                    def for_3_step(a):
                                        for_3 = (((a[0])[0]*(a[1])[1] * (a[2])[2]) + ((a[0])[1]*(a[1])[2] * (a[2])[0]) + ((a[0])[2]*(a[1])[0] * (a[2])[1]))-( ((a[0])[2]*(a[1])[1] * (a[2])[0]) + ((a[0])[1]*(a[1])[0] * (a[2])[2]) + ((a[0])[0]*(a[1])[2] * (a[2])[1]) )
                                        for_3_step = f'[({(a[0])[0]}*{(a[1])[1]} * {(a[2])[2]}) + ({(a[0])[1]}*{(a[1])[2]} * {(a[2])[0]}) + ({(a[0])[2]}*{(a[1])[0]} * {(a[2])[1]})] - [({(a[0])[2]}*{(a[1])[1]} * {(a[2])[0]}) + ({(a[0])[1]}*{(a[1])[0]} * {(a[2])[2]}) + ({(a[0])[0]}*{(a[1])[2]} * {(a[2])[1]})]'
                                        
                                        return for_3_step

                                    mat1 = int(for_3(arr1))
                                    mat2 = int(for_3(arr2))
                                    mat3 = int(for_3(arr3))
                                    mat4 = int(for_3(arr4))
                                    step_mat1 = (for_3_step(arr1))
                                    step_mat2 = (for_3_step(arr2))
                                    step_mat3 = (for_3_step(arr3))
                                    step_mat4 = (for_3_step(arr4))

                                    solution = (f'({a[0][0]}*{step_mat1}-\n{a[0][1]}*{step_mat2} + \n{a[0][2]}*{step_mat3} - \n{a[0][3]}*{step_mat4})')

                                    # print(a[0][0]*mat1-a[0][1]*mat2 + a[0][2]*mat3 - a[0][3]*mat4 )
                                    # print(f'({a[0][0]}*{step_mat1}-{a[0][1]}*{step_mat2} + {a[0][2]}*{step_mat3} - {a[0][3]}*{step_mat4} = {solution} )')
                                    return solution


                                def ind(n,m):
                                        l = []
                                        for i in range(len(a)):
                                            for j in range(len(a[i])):
                                                if i!=n and j != m:
                                                    l.append((a[i][j]))
                                        o = (np.array(l)).reshape(len(a)-1,len(a)-1)
                                        p = []
                                        for i in o:
                                            p.append(i)
                                        return p
                                arr1 = ind(0,0)
                                arr2 = ind(0,1)
                                arr3 = ind(0,2)
                                arr4 = ind(0,3)
                                arr5 = ind(0,4)
                                mat1 = int(determinant4(arr1))
                                mat2 = int(determinant4(arr2))
                                mat3 = int(determinant4(arr3))
                                mat4 = int(determinant4(arr4))
                                mat5 = int(determinant4(arr5))
                                step_mat1 = (determinant4_for_step(arr1))
                                step_mat2 = (determinant4_for_step(arr2))
                                step_mat3 = (determinant4_for_step(arr3))
                                step_mat4 = (determinant4_for_step(arr4))
                                step_mat5 = (determinant4_for_step(arr5))
                                sol_frame = Frame(frame1)
                                sol_frame.pack()
                                Label(sol_frame,text=f'{a[0][0]}*').grid(row=0,column=0)
                                Label(sol_frame,text=f'{a[0][1]}*').grid(row=0,column=3)
                                Label(sol_frame,text=f'{a[0][2]}*').grid(row=0,column=6)
                                Label(sol_frame,text=f'{a[0][3]}*').grid(row=0,column=9)
                                Label(sol_frame,text=f'{a[0][4]}*').grid(row=0,column=12)
                                Label(sol_frame,text=(np.array(arr1))).grid(row=0,column=1)
                                Label(sol_frame,text=(np.array(arr2))).grid(row=0,column=4)
                                Label(sol_frame,text=(np.array(arr3))).grid(row=0,column=7)
                                Label(sol_frame,text=(np.array(arr4))).grid(row=0,column=10)
                                Label(sol_frame,text=(np.array(arr5))).grid(row=0,column=13)
                                Label(sol_frame,text='-').grid(row=0,column=2)
                                Label(sol_frame,text='+').grid(row=0,column=5)
                                Label(sol_frame,text='-').grid(row=0,column=8)
                                Label(sol_frame,text='+').grid(row=0,column=11)
                                solution_5x5 = (a[0][0]*mat1-a[0][1]*mat2 + a[0][2]*mat3 - a[0][3]*mat4 + a[0][4]*mat5)
                                STEP = f'({a[0][0]}*{step_mat1}-\n{a[0][1]}*{step_mat2} + \n{a[0][2]}*{step_mat3} - \n{a[0][3]}*{step_mat4} + \n{a[0][4]}*{step_mat5} = {solution_5x5} )'
                                print(a[0][0]*mat1-a[0][1]*mat2 + a[0][2]*mat3 - a[0][3]*mat4 + a[0][4]*mat5)
                                print(f'({a[0][0]}*{step_mat1}-{a[0][1]}*{step_mat2} + {a[0][2]}*{step_mat3} - {a[0][3]}*{step_mat4} + {a[0][4]}*{step_mat5} = {solution_5x5} )')
                                Label(frame1,text=STEP,font=f'Times {n}').pack()
                            determinant5(a)
            u = Button(window,text='Submit',command=lambda:(q(),u.destroy()))
            u.place(x=180,y=56)
        b = Button(window,text="Select",command=lambda:(matrix(),b.destroy()))
        b.place(x=46,y=80)
    button = Button(window,text="Start",command=lambda:(get(),button.destroy()))
    button.place(x=46,y = 80)

def eigenvalues():
    window = Frame(main_window,width=900,height=750)
    window.config(background="#16b775")
    window.place(x=0,y=0)
    frame1 = Frame(window)
    frame1.place(x=50,y=300)
    text_var1 = []
    entries1 = []
    Button(window,text="Main menu",command=main).place(x=800,y=650)
    def get():
        Button(window,text="Заново",command=eigenvalues).place(x=790,y=700)
        size = ttk.Combobox(window, width = 5, values=[1,2,3,4,5],state="readonly")
        size.place(x=46,y=56)
        Label(window,text="Size of matrix",width=16).place(x=46,y=30)
        def matrix():
            x1 = 0
            y1 = 0
            sizes = []
            rows,cols = (int(size.get()),int(size.get()))
            sizes.append(rows)
            sizes.append(cols)
            max_n = max(sizes)
            for i in range(rows):
                text_var1.append([])
                entries1.append([])
                for j in range(cols):
                    text_var1[i].append(StringVar())
                    entries1[i].append(Entry(window, textvariable=text_var1[i][j],width=3))
                    entries1[i][j].place(x=45 + x1, y=100 + y1)
                    x1 += 30
                y1 += 30
                x1 = 0
                
                def get_mat1():
                    matrix = []
                    for i in range(rows):
                        matrix.append([])
                        for j in range(cols):
                            matrix[i].append(int(text_var1[i][j].get()))
                    return (matrix) 
                def q():
                    def dest_brack(M):
                        s = [[str(e) for e in row] for row in M]
                        lens = [max(map(len, col)) for col in zip(*s)]
                        fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
                        table = [fmt.format(*row) for row in s]
                        r = '\n'.join(table)
                        return r
                    x = Symbol('x')
                    a = get_mat1()
                    n = int(45/int(size.get()))
                    for i in range(len(a)):
                        for j in range(len(a[i])):
                            if i == j:
                                a[i][j] = (a[i][j]-x)
                    print(np.array(a))
                    Label(frame1,text='Starting with subtracting x:',font= f'Times {n}').grid(row=0,column=0)
                    Label(frame1,text=dest_brack(np.array(a)),font= f'Times {n}').grid(row=0,column=1)
                    Label(frame1,text='The determinant of the obtained matrix is' ,font= f'Times {n}').grid(row=1,column=0)
                    Label(frame1,text='These are the eigenvalues' ,font= f'Times {n}').grid(row=2,column=0)
                    if int(size.get()) == 1:
                        n = int(40/int(size.get()))
                        x1 = sympy.solve(a[0][0],x)
                        print(x1)
                        Label(frame1,text=x1,font= f'Times {n}').grid(row=2,column=1)
                    if int(size.get()) == 2:
                        n = int(40/int(size.get()))
                        for_2 = (a[0])[0]*(a[1])[1]-(a[0])[1]*(a[1])[0]
                        Label(frame1,text=for_2,font= f'Times {n}').grid(row=1,column=1)
                        print(for_2)
                        x1 = sympy.solve(for_2,x)
                        print(x1)
                        Label(frame1,text=x1,font= f'Times {n}').grid(row=2,column=1)
                    if int(size.get()) == 3:
                        def for_3(a):
                            for_3 = (((a[0])[0]*(a[1])[1] * (a[2])[2]) + ((a[0])[1]*(a[1])[2] * (a[2])[0]) + ((a[0])[2]*(a[1])[0] * (a[2])[1]))-( ((a[0])[2]*(a[1])[1] * (a[2])[0]) + ((a[0])[1]*(a[1])[0] * (a[2])[2]) + ((a[0])[0]*(a[1])[2] * (a[2])[1]) )
                            return for_3
                        Label(frame1,text=for_3(a),font=f'Times {n}').grid(row=1,column=1)
                        x1 = sympy.solve(for_3(a),x)
                        Label(frame1,text=x1,font= f'Times {n}').grid(row=2,column=1)
                        # print(for_3)
                    if int(size.get()) == 4:
                        n = int(40/int(size.get()))
                        def determinant(a):
                            
                            def ind(n,m):
                                l = []
                                for i in range(len(a)):
                                    for j in range(len(a[i])):
                                        if i!=n and j != m:
                                            l.append((a[i][j]))
                                o = (np.array(l)).reshape(len(a)-1,len(a)-1)
                                p = []
                                for i in o:
                                    p.append(i)
                                return p
                            arr1 = ind(0,0)
                            arr2 = ind(0,1)
                            arr3 = ind(0,2)
                            arr4 = ind(0,3)

                            def for_3(a):
                                for_3 = (((a[0])[0]*(a[1])[1] * (a[2])[2]) + ((a[0])[1]*(a[1])[2] * (a[2])[0]) + ((a[0])[2]*(a[1])[0] * (a[2])[1]))-( ((a[0])[2]*(a[1])[1] * (a[2])[0]) + ((a[0])[1]*(a[1])[0] * (a[2])[2]) + ((a[0])[0]*(a[1])[2] * (a[2])[1]) )
                                return for_3
                            mat1 = (for_3(arr1))
                            mat2 = (for_3(arr2))
                            mat3 = (for_3(arr3))
                            mat4 = (for_3(arr4))

                            solution = a[0][0]*mat1-a[0][1]*mat2 + a[0][2]*mat3 - a[0][3]*mat4
                            return solution
                        print(determinant(a))   
                        Label(frame1,text=(f'{determinant(a)}=0'),font=f'Times {n}').grid(row=1,column=1)
                        x1 = sympy.solve((determinant(a)),x)
                        Label(frame1,text=x1,font= f'Times {n}').grid(row=2,column=1)
                    if int(size.get()) == 5:
                            n = int(40/int(size.get()))
                            def determinant5(a):         
                                def determinant4(a):

                                    def ind(n,m):
                                        l = []
                                        for i in range(len(a)):
                                            for j in range(len(a[i])):
                                                if i!=n and j != m:
                                                    l.append((a[i][j]))
                                        o = (np.array(l)).reshape(len(a)-1,len(a)-1)
                                        p = []
                                        for i in o:
                                            p.append(i)
                                        return p
                                    arr1 = ind(0,0)
                                    arr2 = ind(0,1)
                                    arr3 = ind(0,2)
                                    arr4 = ind(0,3)

                                    def for_3(a):
                                        for_3 = (((a[0])[0]*(a[1])[1] * (a[2])[2]) + ((a[0])[1]*(a[1])[2] * (a[2])[0]) + ((a[0])[2]*(a[1])[0] * (a[2])[1]))-( ((a[0])[2]*(a[1])[1] * (a[2])[0]) + ((a[0])[1]*(a[1])[0] * (a[2])[2]) + ((a[0])[0]*(a[1])[2] * (a[2])[1]) )
                                        for_3_step = f'[({(a[0])[0]}*{(a[1])[1]} * {(a[2])[2]}) + ({(a[0])[1]}*{(a[1])[2]} * {(a[2])[0]}) + ({(a[0])[2]}*{(a[1])[0]} * {(a[2])[1]})] - [({(a[0])[2]}*{(a[1])[1]} * {(a[2])[0]}) + ({(a[0])[1]}*{(a[1])[0]} * {(a[2])[2]}) + ({(a[0])[0]}*{(a[1])[2]} * {(a[2])[1]})] = {for_3}'
                                        return for_3

                                    mat1 = (for_3(arr1))
                                    mat2 = (for_3(arr2))
                                    mat3 = (for_3(arr3))
                                    mat4 = (for_3(arr4))

                                    solution = a[0][0]*mat1-a[0][1]*mat2 + a[0][2]*mat3 - a[0][3]*mat4

                                    return solution

                                def ind(n,m):
                                        l = []
                                        for i in range(len(a)):
                                            for j in range(len(a[i])):
                                                if i!=n and j != m:
                                                    l.append((a[i][j]))
                                        o = (np.array(l)).reshape(len(a)-1,len(a)-1)
                                        p = []
                                        for i in o:
                                            p.append(i)
                                        return p
                                arr1 = ind(0,0)
                                arr2 = ind(0,1)
                                arr3 = ind(0,2)
                                arr4 = ind(0,3)
                                arr5 = ind(0,4)
                                mat1 = (determinant4(arr1))
                                mat2 = (determinant4(arr2))
                                mat3 = (determinant4(arr3))
                                mat4 = (determinant4(arr4))
                                mat5 = (determinant4(arr5))

                                solution_5x5 = (a[0][0]*mat1-a[0][1]*mat2 + a[0][2]*mat3 - a[0][3]*mat4 + a[0][4]*mat5)
                                return solution_5x5
                            Label(frame1,text=(f'{determinant5(a)}=0'),font=f'Times {n}').grid(row=1,column=1)
                            x1 = sympy.solve((determinant5(a)),x)
                            Label(frame1,text=x1,font= f'Times {n}').grid(row=2,column=1)                            
                                         
            u = Button(window,text='Submit',command=lambda:(q(),u.destroy()))
            u.place(x=180,y=56)
        b = Button(window,text="Select",command=lambda:(matrix(),b.destroy()))
        b.place(x=46,y=80)
    button = Button(window,text="Start",command=lambda:(get(),button.destroy()))
    button.place(x=46,y = 80)

def main():
    mainmain = Frame(main_window,width=900,height=750,background="#16b775")
    mainmain.place(x=0,y=0)
    Button(mainmain,text="Add matrix",bd=4,width=20,command=add_matrix).place(y=100,x=300)
    Button(mainmain,text="matrix multiplication",bd=4,width=20,command=matrix_multiplication).place(y=140,x=300)
    Button(mainmain,text="scalar matrix multiplication",bd=4,width=20,command=scalar_matrix_multiplication).place(y=180,x=300)
    Button(mainmain,text="matrix transpose",bd=4,width=20,command=matrix_transpose).place(y=220,x=300)
    Button(mainmain,text="matrix rank",bd=4,width=20,command=matrix_rank).place(y=260,x=300)
    Button(mainmain,text="Matrix determinant",bd=4,width=20,command=det).place(y=300,x=300)
    Button(mainmain,text="Eigenvalues",bd=4,width=20,command=eigenvalues).place(y=340,x=300)
main()

main_window.mainloop()