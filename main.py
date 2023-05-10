from tkinter import *
from tkinter import ttk
from alphabet import Alphabet

LANGUAGES = ["English", "Russian"]

english_alphabet = Alphabet("english.txt")

a = english_alphabet.encrypt_text("text_encr.txt", 2, 'encode')

def combo_click(event):
    if combobox.get() == "English":
        myLabel = Label(text=a)
        myLabel.grid(column=1, row=3)


windows = Tk()
windows.title("Caesar Cipher")
windows.config(padx=100, pady=5)

# Logo
canvas = Canvas(width=200,height=200)
logo_image = PhotoImage(file="img/caesar-cipher.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=0)

# Combobox
ttk.Label(windows, text="Select cipher language:").grid(column=1, row=1)
combobox = ttk.Combobox(values=LANGUAGES)
combobox.bind("<<ComboboxSelected>>", combo_click)
combobox.grid(column=1, row=2)

# Button


windows.mainloop()





