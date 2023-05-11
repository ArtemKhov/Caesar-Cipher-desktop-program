from tkinter import *
from tkinter import ttk
from alphabet import Alphabet

LANGUAGES = ["English", "Russian"]


english_alphabet = Alphabet("english.txt")

a = english_alphabet.encrypt_text("text_encr.txt", 2, 'decode')
shift = english_alphabet.count_letter_in_alphabet
print(shift)

# Set value when user choose one of the languages
def combo_click(event):
    if combobox.get() == "English":
        myLabel = Label(text="OK")
        myLabel.grid(column=0, row=2)

# Set value when user choose decode option
def radiobutton_click():
    if radiobutton.get() == 1:
        myLabel = Label(text="Decode")
        myLabel.grid(column=4, row=3)


windows = Tk()
windows.title("Caesar Cipher")
windows.config(padx=100, pady=5)

# Logo
canvas = Canvas(width=200,height=200)
logo_image = PhotoImage(file="img/caesar-cipher.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=0)

# Combobox: select cipher language
ttk.Label(windows, text="Select cipher language:").grid(column=1, row=1)
combobox = ttk.Combobox(values=LANGUAGES)
combobox.bind("<<ComboboxSelected>>", combo_click)
combobox.grid(column=1, row=2)

# Radiobutton: Encode and Decode
radiobutton = BooleanVar()
radiobutton.set(False)

encode_radiobutton = Radiobutton(text="Encode", variable=radiobutton, value=0)
encode_radiobutton.grid(column=0, row=3)

decode_radiobutton = Radiobutton(text="Decode", variable=radiobutton, value=1, command=radiobutton_click)
decode_radiobutton.grid(column=3, row=3)

# Scale: shift amount
scale_label = Label(text="Set cipher shift")
scale_label.grid(column=1, row=5)

shift_scale = Scale(from_=1, to=shift,
                    orient=HORIZONTAL)
shift_scale.grid(column=1, row=4)

# Button


windows.mainloop()





