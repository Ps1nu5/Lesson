from tkinter import *

gameRun = False
def click(text):
    global gameRun
    btn.config(text=str(text))
    gameRun = not gameRun
    timer()

def timer():
    global time
    if gameRun:
        time -= 1
        lbl.config(text=str(time))
        btn.after(1000, timer)

time = 10
root = Tk()
lbl = Label(root, text=str(time))
lbl.pack()

btn = Button(root, text='CLICK ME!', command=lambda : click('123'))
btn.pack()
root.mainloop()