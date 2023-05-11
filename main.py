from tkinter import *
from tkinter import ttk
from alphabet import Alphabet
from tkinter import filedialog

LANGUAGES = ["English", "Russian"]


english_alphabet = Alphabet("english.txt")

a = english_alphabet.encrypt_text("text_encr.txt", 2, 'decode')
shift = english_alphabet.count_letter_in_alphabet
print(shift)

windows = Tk()
windows.title("Caesar Cipher")
windows.config(padx=100, pady=5)

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

# Get value from Scale of the shift
def get_scale_value(event):
    # TODO: if scale == 0 popup alert that need to select shift differ from 0
    scale_value = str(scale_variable.get())
    myLabel = Label(text=scale_value)
    myLabel.grid(column=1, row=6)

# Open and read file
def open_file():
    filepath = filedialog.askopenfilename()
    if filepath != "":
        with open(filepath, "r") as file:
            text = file.read()
            myLabel = Label(text="File downloaded successfully")
            myLabel.grid(column=1, row=8)

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
scale_variable = Variable()
shift_scale = Scale(variable=scale_variable, from_=0, to=shift, orient=HORIZONTAL, command=get_scale_value)
shift_scale.grid(column=1, row=4)

scale_label = Label(text="Set cipher shift")
scale_label.grid(column=1, row=5)

# Button Open file
open_button = Button(text='Open file', command=open_file)
open_button.grid(column=1, row=7)


windows.mainloop()





