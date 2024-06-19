from tkinter import *
from tkinter import ttk
from tkinter import messagebox

root = Tk()
root.title = 'Счётчик'
root.resizable(False, False)
root.attributes("-topmost",True)
with open('count.csv', 'r') as file:
    hw_count = int(file.readline())
print(hw_count)


def write_file(line):
    with open('count.csv', 'w') as file:
        file.write(str(line))


def click_plus():
    global hw_count
    hw_count += 1
    lbl_count.config(text=str(hw_count))
    write_file(hw_count)


def click_minus():
    global hw_count
    hw_count -= 1
    lbl_count.config(text=str(hw_count))
    write_file(hw_count)


def reset():
    global hw_count
    reset_yesno = messagebox.askyesno('Подтверждение', 'Подтвердите сброс счётчика!')
    if reset_yesno:
        hw_count = 0
        lbl_count.config(text=str(hw_count))
        write_file(hw_count)


lbl = ttk.Label(root, text='CЧЁТЧИК ПРОВЕРКИ ДЗ', font=('Verdana', 14, 'bold'))
lbl.grid(row=1, columnspan=3, column=1)

btn_minus = ttk.Button(root, text='-', command=click_minus)
btn_minus.grid(row=2, column=1)

lbl_count = ttk.Label(root, text=str(hw_count), font=('Verdana', 20, 'bold'))
lbl_count.grid(row=2, column=2)

btn_plus = ttk.Button(root, text='+', command=click_plus)
btn_plus.grid(row=2, column=3)

btn_reset = ttk.Button(root, text='Сброс', command=reset)
btn_reset.grid(row=3, columnspan=3, column=1)

root.mainloop()