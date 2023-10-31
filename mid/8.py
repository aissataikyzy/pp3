import tkinter as tk
from datetime import datetime

def update_time():
    current_time = datetime.now().strftime("%H:%M:%S %p")
    time_label.config(text="Текущее время: " + current_time)

root = tk.Tk()
root.title("Приложение c текущим временем")

time_label = tk.Label(root, text="Текущее время: ")
time_label.pack()

update_button = tk.Button(root, text="Обновить", command=update_time)
update_button.pack()

update_time()  # Инициализация времени при запуске приложения

root.mainloop()
