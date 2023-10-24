from tkinter import *
import math

root = Tk()
root.title("Calculator")


E = Entry(root, font=("Arial", 15))
E.grid(row=0, column=0, columnspan=7, sticky='we')

button_list = [
    '(', ')', '1/x', 'C', '/', '*', 'Del',
    'x²', 'xⁿ', 'x!', '7', '8', '9', '-',
    'π', '√', 'n√x', '4', '5', '6', '+',
    'e', 'ln', 'log', '1', '2', '3','=',
    'sin', 'cos', 'tan','%', '0', '.' ]

r = 1
c = 0
for i in button_list:
    func = lambda x = i: calc(x)
    Button(text = i,command= func, font=("Arial", 15)).grid(row=r, column=c, sticky='wens', padx = 5, pady=5)
    c += 1
    if c > 6:
        r += 1
        c = 0
    if i == '=':
        Button(text = i,command= func, font=("Arial", 15)).grid(row=4, column=6, rowspan=2, sticky='wens', padx = 5, pady=5)


def calc(key):
    if key == '=':
        t = "-+0123456789.*/)(ln" 
        if E.get()[0] not in t:
            E.insert(END, "First symbol is not number!")
        try:
            result = eval(E.get())
            E.delete(0, END)
            E.insert(END, str(result))
        except:
            E.insert(END, "Error!")
    elif key == 'C':
        E.delete(0, END)
    elif key == 'Del':
        E.delete(E.get()[-2], END)
    elif key == 'π':
        E.insert(END, math.pi)
    elif key == 'e':
        E.insert(END, math.e)
    elif key == 'x²':
        E.insert(END, '**2') 
    elif key == "xⁿ":
        E.insert(END, '**')
    elif key == '1/x':
        E.insert(END, '**-1')
    elif key == '%':
        E.insert(END, '/100')
    elif key == 'ln':
        E.insert(0, str(math.log(int(E.get()), math.e)))
        E.insert(END, eval(str(math.log(int(E.get()), math.e))))
    elif key == 'log':
        q = E.get()
        E.delete(0, END)
        E.insert(END, eval(str(math.log(int(q), 10))))
    elif key == "sin":
        E.insert(END, "=" + str(math.sin(float(E.get()))))
    elif key == "cos":
        E.insert(END, "=" + str(math.cos(float(E.get()))))
    elif key == 'tan':
        E.insert(END, '=' + str(math.tan(float(E.get()))))
    elif key == "(":
        E.insert(END, "(")
    elif key == ")":
        E.insert(END, ")")
    elif key == "x!":
        E.insert(END, "!=" + str(math.factorial(int(E.get()))))
    elif key == "√":
        E.insert(END, "=" + str(math.sqrt(int(E.get()))))
    elif key == 'n√x':
        E.insert(END, '**(1/')
    else:
        if "=" in E.get():
            E.delete(0, END)
        E.insert(END, key)

root.mainloop()