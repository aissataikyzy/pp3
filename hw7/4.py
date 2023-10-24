from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import math
import sys

root = Tk() 
root.title("Calculator")

bttn_list = [
"7", "8", "9", "*", "2ⁿᵈ", "x²", "x³", "xʸ", "eˣ", "10ˣ", "Exit",
"4", "5", "6", "-", "1/x", "²√x", "³√x", "ʸ√x", "ln", "log₁₀", "±",
"1", "2", "3",  "+", "x!", "sin", "cos", "tan", "e", "(", ")",
"0", "C", "=",  "/", "Rad", "sinh", "cosh", "tanh", "π", "%", ",",]
r = 1
c = 0
for i in bttn_list:
    rel = ""
    cmd=lambda x=i: calc(x)
    ttk.Button(root, text=i, command = cmd, width = 10).grid(row=r, column = c)
    c += 1
    if c > 10:
        c = 0
        r += 1
    
calc_entry = Entry(root, width = 60)
calc_entry.grid(row=0, column=0, columnspan=5)

def calc(key):
    global memory
    if key == "=":

        str1 = "-+0123456789.*/)(" 
        if calc_entry.get()[0] not in str1:
            calc_entry.insert(END, "First symbol is not number!")
            messagebox.showerror("Error!", "You did not enter the number!")

        try:
            result = eval(calc_entry.get())
            calc_entry.insert(END, "=" + str(result))
        except:
            calc_entry.insert(END, "Error!")
            messagebox.showerror("Error!", "Check the correctness of data")


    elif key == "C":
        calc_entry.delete(0, END)


    elif key == "±":
        if "=" in calc_entry.get():
            calc_entry.delete(0, END)
        try:
            if calc_entry.get()[0] == "-":
                calc_entry.delete(0)
            else:
                calc_entry.insert(0, "-")
        except IndexError:
            pass

    elif key == "π":
        calc_entry.insert(END, math.pi)

    elif key == "Exit":
        root.after(1,root.destroy)
        sys.exit    

    elif key == "x²":
        calc_entry.insert(END, "**")

    elif key == "x³":
        calc_entry.insert(END, "**")
        
    elif key == "xʸ":
        calc_entry.insert(END, "**")

    elif key == "eˣ":
        calc_entry.insert(END, math.exp(calc_entry.get()))

    elif key == "sin":
        calc_entry.insert(END, "=" + str(math.sin(int(calc_entry.get()))))

    elif key == "cos":
        calc_entry.insert(END, "=" + str(math.cos(int(calc_entry.get()))))

    elif key == "(":
        calc_entry.insert(END, "(")
    elif key == ")":
        calc_entry.insert(END, ")")

    elif key == "x!":
        calc_entry.insert(END, "=" + str(math.factorial(int(calc_entry.get()))))

    elif key == "√2":
        calc_entry.insert(END, "=" + str(math.sqrt(int(calc_entry.get()))))

    else:
        if "=" in calc_entry.get():
            calc_entry.delete(0, END)
        calc_entry.insert(END, key)

root.mainloop()