import tkinter as tk
from tkinter import *
import speech_recognition as sr
from translate import Translator

global counter
counter = 2

main = Tk()
main.title("text convertor")
main.minsize(400,400)
main.maxsize(400,400)

def widgets():
    lbl_start = Label( main, text="speak")
    lbl_start.config(font=("esthetique",22,"bold"), bg="blue", width=24)
    lbl_start.grid(row=0)

    btn_start = Button(main, text="start", command=get_voice)
    btn_start.config(font=("Babell Bold",20), bg="lime", fg="white", width=10)
    btn_start.grid(row=1, pady=10)

r = sr.Recognizer()

def get_voice():
    try:
        with sr.Microphone() as src:
            audio = r.listen(src)
            text = r.recognize_google(audio)
            text = text.lower()
            translator = Translator(to_lang="fa")
            text = translator.translate(text)
            show_text(text)
    except:
        pass

def show_text(text):   
    global counter
    lbl_name = f"lbl_{counter}"
    lbl_name = Label(text=text)
    lbl_name.config(font=("Mitra",16))
    lbl_name.grid(row=counter)     

widgets()

main.mainloop()