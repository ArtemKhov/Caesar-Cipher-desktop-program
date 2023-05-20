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
        self.logo_image = PhotoImage(file="img/caesar-cipher_logo.png")
        self.canvas.create_image(100, 100, image=self.logo_image)
        self.canvas.grid(column=0, row=0)

        # Combobox: select cipher language
        self.language_label = ttk.Label(text="Select cipher language:", foreground="#002B5B", font=("Lucida Sans Unicode", 12, "bold"))
        self.language_label.grid(column=0, row=1, pady=5)

        self.languages = ["English", "French", "German", "Russian"]
        self.combobox = ttk.Combobox(values=self.languages, foreground="#002B5B", font=("Lucida Sans Unicode", 12))
        self.combobox.bind("<<ComboboxSelected>>", self.combobox_click)
        self.combobox.grid(column=0, row=2, pady=(0, 25))

        # Separator
        self.separator = ttk.Separator(orient=HORIZONTAL)
        self.separator.grid(column=0, row=3, sticky="ew")

        # Cipher Method label
        self.method = Label(self, text="Choose method:", foreground="#002B5B", font=("Lucida Sans Unicode", 12, "bold"))
        self.method.grid(column=1, row=1, pady=(10,0))

        # Radiobutton: Encode and Decode
        self.cipher_direction = IntVar()

        self.option = Radiobutton(self, text="Encode", foreground="#002B5B", font=("Lucida Sans Unicode", 11),
                                  variable=self.cipher_direction, value=0)
        self.option.grid(column=0, row=2)

        self.option = Radiobutton(self, text="Decode", foreground="#002B5B", font=("Lucida Sans Unicode", 11),
                                  variable=self.cipher_direction, value=1)
        self.option.grid(column=2, row=2)

        # Button: Open file
        self.open_button = Button(self, text='Open TXT File', foreground="#002B5B", font=("Lucida Sans Unicode", 12, "bold"),
                                  state="disabled", command=self.open_user_file)
        self.open_button.grid(column=1, row=3, ipadx=5, pady=25)

        # Shift label
        self.instruction = Label(self, text=f"Set cipher shift", foreground="#002B5B", font=("Lucida Sans Unicode", 10))

        # Scale: shift amount
        self.shift_var = IntVar()
        self.shift = Scale(self, variable=self.shift_var, from_=1, foreground="#002B5B", font=("Lucida Sans Unicode", 10),
                           orient=HORIZONTAL, command=self.change_scale)

        # Button: Encode/Decode
        self.submit_button = Button(self, text="Encode/Decode", background="#002B5B", foreground="white", font=("Lucida Sans Unicode", 12, "bold"),
                                    command=lambda: [self.switch_buttons_state(0), self.caesar()])

        # Button: Save File
        self.save_button = Button(self, text='Save file', foreground="white", font=("Lucida Sans Unicode", 12, "bold"),
                                  state="disabled", command=self.save_file)


    # Select language of the cipher
    def combobox_click(self, event):

        if self.combobox.get() == "English":
            self.switch_buttons_state(1)
            self.file = open("alphabets/english.txt", "r", encoding="UTF-8")
            self.alphabet = []
            self.count_letter_in_alphabet = ""

            # Return an alphabet and length of the alphabet into variables
            for letter in self.file:
                self.alphabet += letter.split(",")
                self.count_letter_in_alphabet += "".join(letter.split(","))

            # Correct alphabet to the cipher shift
            if int(len(self.count_letter_in_alphabet)) % 2 == 0:
                self.count_letter_in_alphabet = len(self.alphabet) // 2

            # Show shift scale when the user select language
            self.shift.grid(column=1, row=6)
            self.instruction.config(text=f"Set cipher shift (1-{self.count_letter_in_alphabet}) ")
            self.instruction.grid(column=1, row=7, padx=5)

        elif self.combobox.get() == "French":
            self.german_lng = 0
            self.switch_buttons_state(1)
            self.file = open("alphabets/french.txt", "r", encoding="UTF-8")
            self.alphabet = []
            self.count_letter_in_alphabet = ""

            # Return an alphabet and length of the alphabet into variables
            for letter in self.file:
                self.alphabet += letter.split(",")
                self.count_letter_in_alphabet += "".join(letter.split(","))

            # Correct alphabet to the cipher shift
            if int(len(self.count_letter_in_alphabet)) % 2 == 0:
                self.count_letter_in_alphabet = len(self.alphabet) // 2

            # Show shift scale when the user select language
            self.shift.grid(column=1, row=6)
            self.instruction.config(text=f"Set cipher shift (1-{self.count_letter_in_alphabet}) ")
            self.instruction.grid(column=1, row=7, padx=5)

        elif self.combobox.get() == "German":
            self.switch_buttons_state(1)
            self.file = open("alphabets/german.txt", "r", encoding="UTF-8")
            self.alphabet = []
            self.count_letter_in_alphabet = ""

            # Return an alphabet and length of the alphabet into variables
            for letter in self.file:
                self.alphabet += letter.split(",")
                self.count_letter_in_alphabet += "".join(letter.split(","))

            # Correct alphabet to the cipher shift
            if int(len(self.count_letter_in_alphabet)) % 2 == 0:
                self.count_letter_in_alphabet = len(self.alphabet) // 2

            # Show shift scale when the user select language
            self.shift.grid(column=1, row=6)
            self.instruction.config(text=f"Set cipher shift (1-{self.count_letter_in_alphabet}) ")
            self.instruction.grid(row=7, column=1, padx=5)

        elif self.combobox.get() == "Russian":
            self.switch_buttons_state(1)
            self.file = open("alphabets/russian.txt", "r", encoding="UTF-8")
            self.alphabet = []
            self.count_letter_in_alphabet = ""

            # Return an alphabet and length of the alphabet into variables
            for letter in self.file:
                self.alphabet += letter.split(",")
                self.count_letter_in_alphabet += "".join(letter.split(","))

            # Correct alphabet to the cipher shift
            if int(len(self.count_letter_in_alphabet)) % 2 == 0:
                self.count_letter_in_alphabet = len(self.alphabet) // 2

            # Show shift scale when the user select language
            self.shift.grid(column=1, row=6)
            self.instruction.config(text=f"Set cipher shift (1-{self.count_letter_in_alphabet}) ")
            self.instruction.grid(row=7, column=1, padx=5)

    # Change Scale according to the length of the selected alphabet
    def change_scale(self, another_parameter):
        self.shift.config(to=int(self.count_letter_in_alphabet))

    # Open and read user file
    def open_user_file(self):
        self.text_editor = Text()
        filepath = filedialog.askopenfilename()
        if filepath != "":
            try:
                with open(filepath, "r", encoding="UTF-8") as file:
                    text = file.read()
                    self.text_editor.delete("1.0", END)
                    self.text_editor.insert("1.0", text)
                    success_message = messagebox.showinfo(title="File downloaded successfully",
                                                          message="For correct Encode/Decode: make sure that the selected cipher language matches the language of the file.")

                    # Show "Encode/Decode" and "Save file" buttons when the user open your file
                    self.submit_button.grid(column=1, row=8, ipadx=15, pady=15)
                    self.save_button.grid(column=1, row=10, ipadx=15)

                    # Return value
                    return self.text_editor
            except UnicodeDecodeError:
                warning_message = messagebox.showwarning(title="Wrong file extension!",
                                                         message="The file must have a .txt extension")


    # Save the final file
    def save_file(self):
        files = [('All Files', '*.*'),
                 ('Text Document', '*.txt')]
        filepath = filedialog.asksaveasfilename(filetypes=files, defaultextension=".txt")
        if filepath != "":
            try:
                text = self.ciphertext
                with open(filepath, "w", encoding="UTF-8") as file:
                    file.write(text)
                    success_message = messagebox.showinfo(title="Success", message="File was saved successfully")
            except AttributeError:
                warning_message = messagebox.showwarning(title="Warning",
                                                         message="Make sure that you select the cipher language or download your file")

    # Switch state of the buttons
    def switch_buttons_state(self, button_key):
        # Make the "Save file" button active and change bg-color when the user click "Encode/Decode" button
        if button_key == 0:
            if self.submit_button:
                self.save_button["state"] = "normal"
                self.save_button.config(background="#5F8D4E")

        # Make the "Open File" button active and change bg-color when the user select one of the cipher language
        if button_key == 1:
            if self.combobox_click:
                self.open_button["state"] = "normal"
                self.open_button.config(background="#F6FFDE")

    # Main func to Encode/Decode user file
    def caesar(self):
        # Get the user's text
        user_file = self.text_editor.get("1.0", END)

        # Get the user-selected shift
        shift_amount = self.shift_var.get()

        # If the user select "Decode" shift == -shift
        if self.cipher_direction.get() == 1:
            shift_amount *= -1

        # Encode/Decode user file
        self.ciphertext = ""
        for line in user_file:
            for char in line:
                if char.lower() in self.alphabet:
                    position = self.alphabet.index(char.lower())
                    new_position = position + (shift_amount % (int(self.count_letter_in_alphabet)))
                    self.ciphertext += self.alphabet[new_position]
                else:
                    self.ciphertext += char

        # Return final text
        return self.ciphertext


# Initialize app window
window = Tk()
window.title("Caesar Cipher")
icon_app = PhotoImage(file="img/icon-app.png")
window.wm_iconphoto(False, icon_app)
window.config(padx=50, pady=5)
app = Application(window)


window.mainloop()



