from tkinter import *
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import pyttsx3
import os

# GUI interface 'window'
window = tk.Tk()
window.title('Vocalify')
window.geometry('900x450+200+200')

# Initialize the engine for text to speech
engine = pyttsx3.init()

def speak_now():
    text = textu.get("1.0", END).strip()
    gender = gender_combobox.get()
    speed = speed_combobox.get()
    voices = engine.getProperty('voices')

    def set_voice():
        if gender == 'Male':
            engine.setProperty('voice', voices[0].id)
        else:
            engine.setProperty('voice', voices[1].id)
        engine.say(text)
        engine.runAndWait()

    if text:
        if speed == 'Fast':
            engine.setProperty('rate', 250)
        elif speed == 'Normal':
            engine.setProperty('rate', 150)
        else:
            engine.setProperty('rate', 60)
        set_voice()

def download_now():
    text = textu.get("1.0", END).strip()
    gender = gender_combobox.get()
    speed = speed_combobox.get()
    voices = engine.getProperty('voices')

    def set_voice():
        if gender == 'Male':
            engine.setProperty('voice', voices[0].id)
        else:
            engine.setProperty('voice', voices[1].id)
        path = filedialog.askdirectory()
        if path:
            os.chdir(path)
            engine.save_to_file(text, 'text.mp3')
            engine.runAndWait()

    if text:
        if speed == 'Fast':
            engine.setProperty('rate', 250)
        elif speed == 'Normal':
            engine.setProperty('rate', 150)
        else:
            engine.setProperty('rate', 60)
        set_voice()

# Icon
icon = PhotoImage(file='TTS icon.png')
window.iconphoto(True, icon)
window.configure(background='#2516A4')
window.resizable(True, True)

# Top frame
top_frame = Frame(window, bg='white', width=900, height=100).place(x=0, y=0)
logo = PhotoImage(file='speaker logo.png')
Label(top_frame, image=logo, bg='white').place(x=10, y=5)
Label(top_frame, text='TEXT->SPEECH', font='Rockwell 20 bold', bg='white', fg='black').place(x=100, y=30)

# Text area
textu = Text(window, font='Calibri 15 bold', bg='white', relief=GROOVE, wrap=WORD)
textu.place(x=10, y=150, width=500, height=250)

# Gender & Speed
Label(window, text='VOICE', font='Arial 15 bold', bg='#2516A4', fg='white').place(x=580, y=160)
Label(window, text='SPEED', font='Arial 15 bold', bg='#2516A4', fg='white').place(x=760, y=160)

gender_combobox = ttk.Combobox(window, values=['Male', 'Female'], font='Arial 14', state='readonly', width=10)
gender_combobox.place(x=550, y=200)
gender_combobox.current(0)

speed_combobox = ttk.Combobox(window, values=['Fast', 'Normal', 'Slow'], font='Arial 14', state='readonly', width=10)
speed_combobox.place(x=730, y=200)
speed_combobox.current(1)

# Buttons for Speak and Download options
btn_image1 = PhotoImage(file='speak.png')
btn1 = Button(window, text='Speak', compound=LEFT, image=btn_image1, width=130, font='Arial 14 bold', command=speak_now)
btn1.place(x=550, y=280)

btn_image2 = PhotoImage(file='download.png')
btn2 = Button(window, text='Download & Save', compound=LEFT, image=btn_image2, width=130, bg='#39c790',
              font='Arial 6 bold', command=download_now)
btn2.place(x=730, y=280)

window.mainloop()
