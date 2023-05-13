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
    sh = shift_var.get()
    print(sh)
    dir = radiobutton.get()
    print(dir)
    return alphabet.encrypt_text(open_file, sh, dir)


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
radiobutton = IntVar()

encode_radiobutton = Radiobutton(text="Encode", variable=radiobutton, value=0)
encode_radiobutton.grid(column=0, row=3)

decode_radiobutton = Radiobutton(text="Decode", variable=radiobutton, value=1)
decode_radiobutton.grid(column=3, row=3)

# Scale: shift amount
shift_var = IntVar()
shift_scale = Scale(variable=shift_var, from_=0, to=shift, orient=HORIZONTAL)
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





