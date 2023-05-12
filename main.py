from tkinter import *
from tkinter import ttk
from alphabet import Alphabet
from tkinter import filedialog

LANGUAGES = ["English", "Russian"]

english_alphabet = Alphabet('alphabets/english.txt')
shift = english_alphabet.count_letter_in_alphabet
english_cipher = english_alphabet.encrypt_text("text_encr.txt", 2, 'decode')


windows = Tk()
windows.title("Caesar Cipher")
windows.config(padx=100, pady=5)

text_editor = Text()

# Set value when user choose one of the languages
def combo_click(event):
    if combobox.get() == "English":
        english_alphabet = Alphabet("alphabets/english.txt")
        return english_alphabet
    elif combobox.get() == "Russian":
        russian_alphabet = Alphabet("alphabets/russian.txt")
        return russian_alphabet


# Set value when user choose decode option
def radiobutton_click():
    if radiobutton.get() == 1:
        decrypt = Label(text="Decrypt")
        decrypt.grid(column=4, row=3)
        return "decode"
    return 'encode'

# Get value from Scale of the shift
def get_scale_value(event):
    # TODO: if scale == 0 popup alert that need to select shift differ from 0
    scale_value = str(scale_variable.get())
    myLabel = Label(text=scale_value)
    myLabel.grid(column=1, row=6)
    return int(scale_value)

# Open and read file
def open_file():
    filepath = filedialog.askopenfilename()
    if filepath != "":
        with open(filepath, "r") as file:
            text = file.read()
            text_editor.delete("1.0", END)
            text_editor.insert("1.0", text)
            myLabel = Label(text="File downloaded successfully")
            myLabel.grid(column=1, row=8)
            return text_editor

# Save the final file
def save_file():
    filepath = filedialog.asksaveasfilename()
    if filepath != "":
        text = text_editor.get("1.0", END)
        with open(filepath, "w") as file:
            file.write(text)

# Switch state of the "Save file" button
def switch():
    if save_button["state"] == "disabled":
        save_button["state"] = "normal"


# Encode/Decode function
def encrypt():
    return Alphabet.encrypt_text(open_file, get_scale_value, radiobutton_click())


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

alphabet = combo_click(combobox)

# Radiobutton: Encode and Decode
radiobutton = BooleanVar()
radiobutton.set(False)

encode_radiobutton = Radiobutton(text="Encode", variable=radiobutton, value=0)
encode_radiobutton.grid(column=0, row=3)

decode_radiobutton = Radiobutton(text="Decode", variable=radiobutton, value=1, command=radiobutton_click)
decode_radiobutton.grid(column=3, row=3)

# Scale: shift amount
scale_variable = Variable()
shift_scale = Scale(variable=scale_variable, from_=0, to=shift, orient=HORIZONTAL, command=get_scale_value)
shift_scale.grid(column=1, row=4)

scale_label = Label(text="Set cipher shift")
scale_label.grid(column=1, row=5)

# Button: Open file
open_button = Button(text='Open file', command=open_file)
open_button.grid(column=1, row=7)

# Button: Encode/Decode
encrypt_button = Button(text="Encode/Decode", command=lambda: [switch(),
                                                               encrypt()])
encrypt_button.grid(column=1, row=9)

# Button: Save File
save_button = Button(text='Save file', state="disabled", command=save_file)
save_button.grid(column=1, row=10)


windows.mainloop()





