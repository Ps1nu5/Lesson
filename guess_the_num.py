import tkinter as tk
from tkinter import messagebox


def update_display():
    global bomb
    global score
    if bomb >= 80:
        bomb_label.config(image=img_1)
    elif 50 <= bomb < 80:
        bomb_label.config(image=img_2)
    elif 0 < bomb < 50:
        bomb_label.config(image=img_3)
    else:
        bomb_label.config(image=img_4)
    fuse_label.config(text='Fuse: ' + str(bomb))
    score_label.config(text='Score: ' + str(score))
    fuse_label.after(100, update_display)


def is_alive():
    global bomb
    global press_return
    if bomb <= 0:
        bomb = 0
        label.config(text='Bang! Bang! Bang!')
        press_return = True
        messagebox.showinfo('Game over', f'Game over!\nScore: {score}')
        return False
    else:
        return True


def update_bomb():
    global bomb
    bomb -= 5
    if is_alive():
        fuse_label.after(400, update_bomb)


def update_score():
    global score
    if is_alive():
        score += 1
        score_label.after(3000, update_score)


def start(event):
    global press_return, bomb, score
    if not press_return:
        pass
    else:
        bomb = 100
        score = 0
        update_bomb()
        update_score()
        update_display()
        label.config(text='')
        press_return = False


def click():
    global bomb
    if is_alive():
        bomb += 1


bomb = 100
score = 0
press_return = True
root = tk.Tk()
root.title("Game")
root.geometry("600x600+500+400")
root.iconbitmap("images/bomb.ico")

label = tk.Label(root, text='Press [enter] to start the game', font=('Comic Sans MS', 12))
label.pack()

fuse_label = tk.Label(root, text=f'Fuse: {str(bomb)}', font=('Comic Sans MS', 14))
fuse_label.pack()

score_label = tk.Label(root, text=f'Score: {str(score)}', font=('Comic Sans MS', 14))
score_label.pack()

img_1 = tk.PhotoImage(file="images/1.gif")
img_2 = tk.PhotoImage(file="images/2.gif")
img_3 = tk.PhotoImage(file="images/3.gif")
img_4 = tk.PhotoImage(file="images/4.gif")

bomb_label = tk.Label(image=img_1)
bomb_label.pack()

click_button = tk.Button(root, text='Click me', bg='black', fg='white', width=15, font=('Comic Sans MS', 14), command=click)
click_button.pack()

root.bind('<Return>', start)
root.mainloop()
