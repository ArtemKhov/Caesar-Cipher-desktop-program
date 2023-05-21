import customtkinter as CTk
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image

class App(CTk.CTk):

    def __init__(self):
        super().__init__()
        self.title("Caesar Cipher")
        self.resizable(False,False)
        self.iconbitmap("img/icon-app.ico")
        self.create_widgets()

    def create_widgets(self):
        # Logo
        self.logo = CTk.CTkImage(light_image=Image.open("img/caesar-cipher_light.png"),
                                 dark_image=Image.open("img/caesar-cipher_dark.png"),
                                 size=(150, 150))
        self.logo = CTk.CTkLabel(master=self, text="", image=self.logo)
        self.logo.grid(column=1, row=2)

        # Switch Dark/Light mode slider
        self.appearance_mode_slider = CTk.CTkOptionMenu(master=self, values=["Light", "Dark"],
                                                        width=70, fg_color="grey", button_color="grey",
                                                        command=self.change_appearance_mode)
        self.appearance_mode_slider.grid(column=1, row=0, pady=(15, 25), sticky="ne")


        # Language frame
        self.language_frame = CTk.CTkFrame(master=self, bg_color="transparent")
        self.language_frame.grid(column=1, row=3, pady=(15,0), padx=50, sticky="nsew")

        # Combobox: select cipher language
        self.language_label = CTk.CTkLabel(master=self.language_frame, text="Select cipher language:", text_color="#002B5B",
                                        font=("Lucida Sans Unicode", 18, "bold"))
        self.language_label.grid(column=0, row=0, pady=5, padx=30)

        self.combobox_var = CTk.StringVar()
        self.languages = ["English", "French", "German", "Russian"]
        self.combobox = CTk.CTkComboBox(master=self.language_frame, values=self.languages, text_color="#002B5B", font=("Lucida Sans Unicode", 12),
                                        variable=self.combobox_var, command=self.combobox_click)
        self.combobox.grid(column=0, row=1, pady=(0, 25))


        # Cipher Method label
        self.method = CTk.CTkLabel(master=self, text="Choose method:", text_color="#002B5B", font=("Lucida Sans Unicode", 14, "bold"))
        self.method.grid(column=1, row=5, pady=(20, 0))

        # Radiobutton: Encode and Decode
        self.cipher_direction = IntVar()
        # encode button
        self.option = CTk.CTkRadioButton(master=self, text="Encode", text_color="#002B5B", font=("Lucida Sans Unicode", 14),
                                  variable=self.cipher_direction, value=0)
        self.option.grid(column=1, row=6, padx=(5,150), pady=10)
        # decode button
        self.option = CTk.CTkRadioButton(master=self, text="Decode", text_color="#002B5B", font=("Lucida Sans Unicode", 14),
                                  variable=self.cipher_direction, value=1)
        self.option.grid(column=1, row=6, padx=(210, 0), pady=10)

        # Button: Open file
        self.open_button = CTk.CTkButton(master=self, text='Open TXT File', text_color="#002B5B",
                                         font=("Lucida Sans Unicode", 12, "bold"), state="disabled", command=self.open_user_file)
        self.open_button.grid(column=1, row=7, ipadx=5, pady=25)


        # Scale frame
        self.scale_frame = CTk.CTkFrame(master=self)

        # Scale: shift amount
        self.shift_var = IntVar()
        self.shift = CTk.CTkSlider(master=self.scale_frame, variable=self.shift_var, from_=1, to=50, fg_color="#002B5B",
                                   orientation=HORIZONTAL, command=self.change_scale)

        # Scale Entry frame
        self.scale_entry = CTk.CTkEntry(master=self.scale_frame, width=30)

        # Shift label
        self.instruction = CTk.CTkLabel(master=self.scale_frame, text=f"Set cipher shift", text_color="#002B5B", font=("Lucida Sans Unicode", 10))

        # Button: Encode/Decode
        self.submit_button = CTk.CTkButton(master=self, text="Encode/Decode", fg_color="white", font=("Lucida Sans Unicode", 12, "bold"),
                                    command=lambda: [self.switch_buttons_state(0), self.caesar()])

        # Button: Save File
        self.save_button = CTk.CTkButton(master=self, text='Save file', fg_color="white", font=("Lucida Sans Unicode", 12, "bold"),
                                  state="disabled", command=self.save_file)

    # Change Light/Dark mode
    def change_appearance_mode(self, new_appearance_mode):
        CTk.set_appearance_mode(new_appearance_mode)

    # Select language of the cipher
    def combobox_click(self, event):
        if self.combobox_var.get() == "English":
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

            # Show Scale Frame
            self.scale_frame.grid(column=1, row=8, padx=20)

            # Show shift scale when the user select language
            self.shift.grid(column=0, row=0, padx=(20,5), pady=(10,0))
            self.scale_entry.grid(column=1, row=0, padx=(0,20), pady=(10,0))
            self.instruction.configure(text=f"Set cipher shift (1-{self.count_letter_in_alphabet}) ")
            self.instruction.grid(column=0, row=2, padx=(20,0))

        elif self.combobox_var.get() == "French":
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

            # Show Scale Frame
            self.scale_frame.grid(column=1, row=8, padx=20)

            # Show shift scale when the user select language
            self.shift.grid(column=0, row=0, padx=(20, 5), pady=(10, 0))
            self.scale_entry.grid(column=1, row=0, padx=(0, 20), pady=(10, 0))
            self.instruction.configure(text=f"Set cipher shift (1-{self.count_letter_in_alphabet}) ")
            self.instruction.grid(column=0, row=2, padx=(20, 0))

        elif self.combobox_var.get() == "German":
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

            # Show Scale Frame
            self.scale_frame.grid(column=1, row=8, padx=20)

            # Show shift scale when the user select language
            self.shift.grid(column=0, row=0, padx=(20, 5), pady=(10, 0))
            self.scale_entry.grid(column=1, row=0, padx=(0, 20), pady=(10, 0))
            self.instruction.configure(text=f"Set cipher shift (1-{self.count_letter_in_alphabet}) ")
            self.instruction.grid(column=0, row=2, padx=(20, 0))

        elif self.combobox_var.get() == "Russian":
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

            # Show Scale Frame
            self.scale_frame.grid(column=1, row=8, padx=20)

            # Show shift scale when the user select language
            self.shift.grid(column=0, row=0, padx=(20, 5), pady=(10, 0))
            self.scale_entry.grid(column=1, row=0, padx=(0, 20), pady=(10, 0))
            self.instruction.configure(text=f"Set cipher shift (1-{self.count_letter_in_alphabet}) ")
            self.instruction.grid(column=0, row=2, padx=(20, 0))


    # Change Scale according to the length of the selected alphabet
    def change_scale(self, another_parameter):
        self.shift.configure(to=int(self.count_letter_in_alphabet))

        # Put shift_value into Scale Entry
        self.scale_entry.configure(state="normal")
        self.scale_entry.delete(0, "end")
        self.scale_entry.insert(0, self.shift_var.get())
        self.scale_entry.configure(state="disabled")


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
                    self.submit_button.grid(column=1, row=9, ipadx=15, pady=(30,15))
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
                self.save_button.configure(state="normal", fg_color="#5F8D4E")

        # Make the "Open File" button active and change bg-color when the user select one of the cipher language
        if button_key == 1:
            if self.combobox_click:
                self.open_button.configure(state="normal", fg_color="#F6FFDE")

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
window = App()
window.configure(padx=10, pady=15)
window.mainloop()