import tkinter as tk
from tkinter import *

main = Tk()
main.title("text convertor")
main.minsize(400,400)
main.maxsize(400,400)

def widgets():
    lbl_start = Label(main, text="speak")
    lbl_start.config(font=("esthetique",22,"bold"), bg="blue", width=24)
    lbl_start.grid(row=0)

widgets()

main.mainloop()