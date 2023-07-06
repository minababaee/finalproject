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

    btn_start = Button(main, text="start")
    btn_start.config(font=("Babell Bold",20), bg="lime", fg="white", width=10)
    btn_start.grid(row=1, pady=10)


widgets()

main.mainloop()