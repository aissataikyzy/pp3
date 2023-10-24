from tkinter import *
import math
import tkinter.messagebox

root = Tk()
root.title("Scientific Calculator")
root.configure(background="powder")
root.resizable(width = False, height=False)
root.geometry("480x568+0+0")

calc = Frame(root)
calc.grid