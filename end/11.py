from tkinter import *

class MatrixCalculator:

    def __init__(self, master):
        self.master = master
        self.master.title('Calculate SVD and PD')
        self.master["bg"] = '#F5EFF6'

        self.window_width = 500
        self.window_height = 500
        self.screen_width = self.master.winfo_screenwidth()
        self.screen_height = self.master.winfo_screenheight()
        self.x_position = (self.screen_width - self.window_width) // 2
        self.y_position = (self.screen_height - self.window_height) // 2

        self.master.geometry(f'{self.window_width}x{self.window_height}+{self.x_position}+{self.y_position}')

        self.welcome_label = Label(self.master, text='Welcome!', font=('Comic Sans Ms', 50), fg='#bb88d3', bg='#F5EFF6')
        self.welcome_label.place(x=125, y=90)

        self.start_button = Button(self.master, text='Start', font=('Comic Sans Ms', 15), fg='#bb88d3', bg='white', command=self.choose)
        self.start_button.place(x=200, y=180)

        self.result = StringVar()
        self.frame1 = None
        self.frame2 = None

    def go_back(self):
        if self.frame1:
            self.frame1.destroy()
            self.frame1 = None

        if self.frame2:
            self.frame2.place_forget()
        self.welcome_label.place(x=125, y=90)
        self.start_button.place(x=200, y=180)

    def calculate(self, method):

        def solve(self):
            pass

        if self.frame1:
            self.frame1.destroy()

        size = int(self.size_var.get()[0])
        entries = []

        cell_size = 50
        cell_padding = 10
        dx = 120
        dy = 150

        for i in range(size):
            for j in range(size):
                x = j * cell_size + cell_padding + dx
                y = i * cell_size + cell_padding + dy

                entry = Entry(self.frame2, width=3)
                entry.place(x=x, y=y)
                entries.append(entry)

        matrix_label = Label(self.frame2, text=f"Calculate {method} for {size}x{size} matrix", font=('Comic Sans Ms', 14), fg='#bb88d3', bg='#F5EFF6')
        matrix_label.place(x=40, y=300)

        calculate_button = Button(self.frame2, text="Calculate", font=('Comic Sans Ms', 14), fg='#bb88d3', command=solve)
        calculate_button.place(x=150, y=350)



    def select(self, method):
        if self.frame1:
            self.frame1.destroy()

        self.result.set(f"Performing {method}...")

        self.frame2 = Frame(self.master, bg='#F5EFF6', width=500, height=500)
        self.frame2.place(x=50, y=20)

        select_size_label = Label(self.frame2, text='Please select size of matrix!', font=('Comic Sans Ms', 24), fg='#bb88d3', bg='#F5EFF6')
        select_size_label.place(x=30, y=30)

        self.size_var = StringVar(value="2x2")

        option_menu = OptionMenu(self.frame2, self.size_var, "2x2", "3x3")
        option_menu.place(x=150, y=75)

        select1_button = Button(self.frame2, text="Select", font=('Comic Sans Ms', 12), fg='#bb88d3', command=lambda: self.calculate(method))
        select1_button.place(x=250, y=75)

    def choose(self):
        self.welcome_label.place_forget()
        self.start_button.place_forget()

        self.frame1 = Frame(self.master, bg='#F5EFF6', width=500, height=500)
        self.frame1.place(x=50, y=20)

        choose_label = Label(self.frame1, text='Please select one!', font=('Comic Sans Ms', 24), fg='#bb88d3', bg='#F5EFF6')
        choose_label.place(x=100, y=80)

        options = ["Singular value decomposition", "Polar decomposition"]
        var = StringVar(value=options[0])

        option_menu = OptionMenu(self.frame1, var, *options)
        option_menu.place(x=100, y=130)

        self.back_button = Button(self.frame1, text="Main menu", font=('Comic Sans Ms', 12), fg='#bb88d3',  command=self.go_back)
        self.back_button.place(x=10, y=300)

        self.result_label = Label(self.frame1, textvariable=self.result)
        self.result_label.place(x=50, y=150)

        select_button = Button(self.frame1, text="Select", font=('Comic Sans Ms', 12), fg='#bb88d3', command=lambda: self.select(var.get()))
        select_button.place(x=300, y=300)

root = Tk()
app = MatrixCalculator(root)
root.mainloop()

