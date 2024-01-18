from tkinter import*
from tkinter.ttk import*

from time import strftime

root = Tk()
root.title("clock")

def time():
    string = strftime('%H:%M:%S %p')
    labe1.config(text=string)
    labe1.after(1000, time)

labe1 =Label(root,font=("ds-digital",80), background = "black", foreground = "cyan")
labe1.pack(anchor='center')
time()

mainloop()
