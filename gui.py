from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox

class Application(Frame):

    def __init__(self, master):
        """ Initialize the Frame """
        Frame.__init__(self, master)
        self.create_widgets()
        self.grid()

    def create_widgets(self):
        # Logo
        self.canvas = Canvas(width=200, height=200)
        self.logo_image = PhotoImage(file="img/caesar-cipher.png")
        self.canvas.create_image(100, 100, image=self.logo_image)
        self.canvas.grid(column=0, row=0)

        # Combobox: select cipher language
        self.language_label = ttk.Label(text="Select cipher language:")
        self.language_label.grid(column=0, row=1)

        self.languages = ["English", "Russian"]
        self.combobox = ttk.Combobox(values=self.languages)
        self.combobox.bind("<<ComboboxSelected>>", self.combobox_click)
        self.combobox.grid(column=0, row=2)

        # Cipher Method label
        self.method = Label(self, text="Choose method:")
        self.method.grid(column=1, row=1)

        # Radiobutton: Encode and Decode
        self.radiobutton = IntVar()

        self.option = Radiobutton(self, text="Encode", variable=self.radiobutton, value=0)
        self.option.grid(column=0, row=2)

        self.option = Radiobutton(self, text="Decode", variable=self.radiobutton, value=1)
        self.option.grid(column=2, row=2)

        # Button: Open file
        self.open_button = Button(self, text='Open file', command=self.open_user_file)
        self.open_button.grid(column=1, row=3)

        # Key label
        self.instruction = Label(self, text=f"Set cipher shift:")

        # Scale: shift amount
        self.shift_var = IntVar()
        self.shift = Scale(self, variable=self.shift_var, from_=0, to=1, orient=HORIZONTAL, command=self.change_scale)

        # Button: Encode/Decode
        self.submit_button = Button(self, text="Encode/Decode", command=self.caesar)
        self.submit_button.grid(row=8, column=1, padx=5)

        # Button: Save File
        self.save_button = Button(self, text='Save file', command=self.save_file)
        self.save_button.grid(column=1, row=10)

    def combobox_click(self, event):
        if self.combobox.get() == "English":
            self.file = open("alphabets/english.txt", "r")
            self.alphabet = []
            self.count_letter_in_alphabet = ""
            for letter in self.file:
                self.alphabet += letter.split(",")
                self.count_letter_in_alphabet += "".join(letter.split(","))
            if int(len(self.count_letter_in_alphabet)) % 2 == 0:
                self.count_letter_in_alphabet = len(self.alphabet) // 2
            else:
                self.count_letter_in_alphabet = len(self.alphabet) // 2 + 1

            # show shift scale when user select language
            self.instruction.config(text=f"Set cipher shift (1-{self.count_letter_in_alphabet}): ")
            self.instruction.grid(row=6, column=1, padx=5)
            self.shift.grid(column=1, row=7)

        elif self.combobox.get() == "Russian":
            self.file = open("alphabets/russian.txt", "r")
            self.alphabet = []
            self.count_letter_in_alphabet = ""
            for letter in self.file:
                self.alphabet += letter.split(",")
                self.count_letter_in_alphabet += "".join(letter.split(","))
            if int(len(self.count_letter_in_alphabet)) % 2 == 0:
                self.count_letter_in_alphabet = len(self.alphabet) // 2
            else:
                self.count_letter_in_alphabet = len(self.alphabet) // 2 + 1

            # show shift scale when user select language
            self.instruction.config(text=f"Set cipher shift (1-{self.count_letter_in_alphabet}): ")
            self.instruction.grid(row=6, column=1, padx=5)
            self.shift.grid(column=1, row=7)


    # Change Scale according to length of the selected alphabet
    def change_scale(self, another_parameter):
        self.shift.config(to=self.count_letter_in_alphabet)

    # Open and read file
    def open_user_file(self):
        self.text_editor = Text()
        filepath = filedialog.askopenfilename()
        if filepath != "":
            with open(filepath, "r") as file:
                text = file.read()
                self.text_editor.delete("1.0", END)
                self.text_editor.insert("1.0", text)
                success_message = messagebox.showinfo(title="Success", message="File downloaded successfully")
                return self.text_editor

    # Save the final file
    def save_file(self):
        files = [('All Files', '*.*'),
                 ('Text Document', '*.txt')]
        filepath = filedialog.asksaveasfilename(filetypes=files, defaultextension=".txt")
        if filepath != "":
            text = self.ciphertext
            with open(filepath, "w") as file:
                file.write(text)
                success_message = messagebox.showinfo(title="Success", message="File was saved successfully")

    def caesar(self):
        m = self.text_editor.get("1.0", END)
        print(m)

        # k = int(self.key.get())
        k = self.shift_var.get()
        print(k)

        if self.radiobutton.get() == 1:
            k = -k

        # Empty text container
        self.ciphertext = ''

        for symbol in m:

            if symbol.isalpha():
                num = ord(symbol) + k

                if symbol.isupper():
                    if num > ord('Z'):
                        num -= 26
                    elif num < ord('A'):
                        num += 26

                elif symbol.islower():
                    if num > ord('z'):
                        num -= 26
                    elif num < ord('a'):
                        num += 26

                self.ciphertext += chr(num)
            else:
                self.ciphertext += symbol

        return self.ciphertext


window = Tk()
window.title("Caesar Cipher")
window.config(padx=50, pady=5)
app = Application(window)


window.mainloop()


