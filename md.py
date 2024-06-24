import tkinter as tk
from tkinter import filedialog


def file_new():
    save_or_not = tk.Tk()
    save_or_not.geometry("150x70+700+550")
    save_or_not.resizable(False, False)
    save_or_not.grid_columnconfigure(0, minsize=75)
    save_or_not.grid_columnconfigure(1, minsize=75)
    saving_label = tk.Label(save_or_not, text="Save file?")
    saving_label.grid(columnspan=2)

    def without_saving():
        save_or_not.destroy()
        global text
        text.delete('1.0', tk.END)

    def saving():
        file_save()
        save_or_not.destroy()
        global text
        text.delete('1.0', tk.END)

    yes_button = tk.Button(save_or_not, text="Yes", command=saving, width=8)
    no_button = tk.Button(save_or_not, text="No", command=without_saving, width=8)
    yes_button.grid(column=0, row=1)
    no_button.grid(column=1, row=1)


def file_open():
    file_name = filedialog.askopenfilename(initialdir='/', title='Open file', filetypes=(('Text Documents', '*.txt'),
                                                                                         ('all files', '*.*')))
    if file_name:
        with open(file_name, 'r') as f:
            text_open = f.read()
            if text_open != tk.NONE:
                text.delete(1.0, tk.END)
                text.insert(tk.END, text_open)
            else:
                text.delete(1.0, tk.END)


def file_save():
    file_name = filedialog.asksaveasfilename(initialdir='/', title='Select file', filetypes=(('Text Documents', '*.txt'),
                                                                                             ('all files', '*.*')))
    print(file_name)
    if file_name:
        with open(file_name+".txt", 'w') as f:
            text_save = str(text.get(1.0, tk.END))
            f.write(text_save+'\n')


def file_exit():
    root.destroy()


def help_function():
    help_window = tk.Tk()
    help_window.geometry("300x70+700+550")
    help_window.resizable(False, False)
    help_label = tk.Label(help_window, text="Link to instructions\nhttps://www.wikihow.com/Use-Notepad")
    help_label.pack()

    def back():
        help_window.destroy()

    back_button = tk.Button(help_window, text="Back", command=back, width=10)
    back_button.pack()


def about():
    about_window = tk.Tk()
    about_window.geometry("300x70+700+550")
    about_window.resizable(False, False)
    help_label = tk.Label(about_window, text="Thanks for using!")
    help_label.pack()

    def back():
        about_window.destroy()

    back_button = tk.Button(about_window, text="Back", command=back, width=10)
    back_button.pack()


root = tk.Tk()
root.geometry("600x400+500+400")
root.title("Notebook")
root.iconbitmap("images/Note.ico")

root.minsize(200, 100)
root.maxsize(1920, 1080)

menu = tk.Menu(root)
root.config(menu=menu)

file_menu = tk.Menu(menu, tearoff=False)
file_menu.add_command(label='New', command=file_new)
file_menu.add_command(label='Open.', command=file_open)
file_menu.add_command(label='Save as.', command=file_save)
file_menu.add_command(label='Exit', command=file_exit)
menu.add_cascade(label='File', menu=file_menu)

help_menu = tk.Menu(menu, tearoff=False)
help_menu.add_command(label='Help', command=help_function)
help_menu.add_command(label='About', command=about)
menu.add_cascade(label='Help', menu=help_menu)

text = tk.Text(root)
text.pack(expand=tk.YES, fill=tk.BOTH)

root.mainloop()
