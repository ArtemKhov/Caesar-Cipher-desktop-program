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
        self.iconbitmap("images/icon_app.ico")
        self.create_widgets()

    # Create elements on the screen
    def create_widgets(self):
        # Logo
        self.logo = CTk.CTkImage(light_image=Image.open("images/caesar_cipher_light.png"),
                                 dark_image=Image.open("images/caesar_cipher_dark.png"),
                                 size=(150, 150))
        self.logo = CTk.CTkLabel(master=self, text="", image=self.logo)
        self.logo.grid(column=1, row=2)

        # Switch Dark/Light mode slider
        self.appearance_mode_slider = CTk.CTkOptionMenu(master=self, values=["Light", "Dark"], width=70,
                                                        text_color=("white", "black"),
                                                        fg_color=("grey", "white"),
                                                        button_color=("#69676E", "#ECF0F1"),
                                                        button_hover_color=("#2c3e50", "#95a5a6"),
                                                        command=self.change_appearance_mode)
        self.appearance_mode_slider.grid(column=1, row=0, pady=(10, 20), sticky="ne")


        # Language frame
        self.language_frame = CTk.CTkFrame(master=self, fg_color=("grey", "#ECF0F1"))
        self.language_frame.grid(column=1, row=3, pady=(35,0), padx=50, sticky="nsew")

        # Select cipher Label
        self.language_label = CTk.CTkLabel(master=self.language_frame, text="Select cipher language:",
                                           text_color=("white", "black"),
                                           font=("Lucida Unicode", 18, "bold"))
        self.language_label.grid(column=0, row=0, pady=5, padx=30)

        # Combobox: select cipher language
        self.combobox_var = CTk.StringVar()
        self.languages = ["English", "French", "German", "Russian"]
        self.combobox = CTk.CTkComboBox(master=self.language_frame, values=self.languages,
                                        text_color=("black", "white"),
                                        font=("Lucida Sans Unicode", 14),
                                        fg_color=("white", "#69676E"),
                                        border_color=("white", "grey"),
                                        button_color=("#ECF0F1", "grey"),
                                        button_hover_color="#18bc9c",
                                        variable=self.combobox_var, command=self.select_cipher_language)
        self.combobox.grid(column=0, row=1, pady=(0, 25))


        # Cipher Method label
        self.method_label = CTk.CTkLabel(master=self, text="Choose method:",
                                   text_color=("black", "white"),
                                   font=("Lucida Sans Unicode", 14, "bold"))
        self.method_label.grid(column=1, row=5, pady=(20, 0))

        # Radiobutton: Encode and Decode
        self.cipher_direction = IntVar()

        self.option = CTk.CTkRadioButton(master=self, text="Encode",
                                         text_color=("black", "white"),
                                         font=("Lucida Sans Unicode", 14),
                                         fg_color="#18bc9c",
                                         hover_color="#3498db",
                                         variable=self.cipher_direction, value=0)
        self.option.grid(column=1, row=6, padx=(5,150), pady=10)

        self.option = CTk.CTkRadioButton(master=self, text="Decode",
                                         text_color=("black", "white"),
                                         fg_color="#18bc9c",
                                         hover_color="#3498db",
                                         font=("Lucida Sans Unicode", 14),
                                         variable=self.cipher_direction, value=1)
        self.option.grid(column=1, row=6, padx=(210, 0), pady=10)

        # Button: Open file
        self.open_button = CTk.CTkButton(master=self, text='Open TXT File',
                                         text_color="#002B5B",
                                         font=("Lucida Sans Unicode", 14, "bold"),
                                         fg_color="white",
                                         border_color="#3498db",
                                         border_width=2,
                                         state="disabled",
                                         command=self.open_and_read_user_file)
        self.open_button.grid(column=1, row=7, ipadx=5, pady=25)

        # Scale frame
        self.scale_frame = CTk.CTkFrame(master=self, fg_color=("grey", "#ECF0F1"))

        # Scale: shift amount
        self.shift_var = IntVar()
        self.shift = CTk.CTkSlider(master=self.scale_frame, variable=self.shift_var, from_=1, to=50,
                                   fg_color="#3498db",
                                   button_color=("white", "grey"),
                                   button_hover_color="#18bc9c",
                                   orientation=HORIZONTAL,
                                   command=self.change_scale)
        self.shift.set(1)


        # Scale Entry frame
        self.scale_entry = CTk.CTkEntry(master=self.scale_frame, width=30,
                                        text_color="black",
                                        fg_color="white")
        self.scale_entry.insert(0, "1")
        self.scale_entry.configure(state="disabled")

        # Shift label
        self.set_cipher_label = CTk.CTkLabel(master=self.scale_frame, text=f"Set cipher shift",
                                        text_color=("white", "black"),
                                        font=("Lucida Sans Unicode", 14))

        # Button: Encode/Decode
        self.encode_decode_button = CTk.CTkButton(master=self, text="Encode/Decode",
                                           text_color="white",
                                           font=("Lucida Sans Unicode", 14, "bold"),
                                           fg_color="#f39c12",
                                           hover_color="#d05e2f",
                                           height=40,
                                           corner_radius=20,
                                           command=lambda: [self.switch_buttons_state(0), self.encrypt_user_file()])

        # Button: Save File
        self.save_button = CTk.CTkButton(master=self, text='Save file',
                                         fg_color="white",
                                         font=("Lucida Sans Unicode", 14, "bold"),
                                         border_width=2,
                                         border_color="#18bc9c",
                                         height=30,
                                         state="disabled",
                                         command=self.save_file)

    # Change Light/Dark mode
    def change_appearance_mode(self, new_appearance_mode):
        CTk.set_appearance_mode(new_appearance_mode)

    def select_cipher_language(self, event):
        if self.combobox_var.get() == "English":
            self.switch_buttons_state(1)
            self.file = open("alphabets/english.txt", "r", encoding="UTF-8")
            self.alphabet = []

            for letter in self.file:
                self.alphabet += letter.split(",")

            self.get_amount_alphabet_letters()

            self.show_shift_elements()

        elif self.combobox_var.get() == "French":
            self.switch_buttons_state(1)
            self.file = open("alphabets/french.txt", "r", encoding="UTF-8")
            self.alphabet = []

            for letter in self.file:
                self.alphabet += letter.split(",")

            self.get_amount_alphabet_letters()

            self.show_shift_elements()

        elif self.combobox_var.get() == "German":
            self.switch_buttons_state(1)
            self.file = open("alphabets/german.txt", "r", encoding="UTF-8")
            self.alphabet = []

            for letter in self.file:
                self.alphabet += letter.split(",")

            self.get_amount_alphabet_letters()

            self.show_shift_elements()

        elif self.combobox_var.get() == "Russian":
            self.switch_buttons_state(1)
            self.file = open("alphabets/russian.txt", "r", encoding="UTF-8")
            self.alphabet = []

            for letter in self.file:
                self.alphabet += letter.split(",")

            self.get_amount_alphabet_letters()

            self.show_shift_elements()

    def get_amount_alphabet_letters(self):
        self.count_letter_in_alphabet = len(self.alphabet) // 2

    # Change Scale according to the length of the selected alphabet
    def change_scale(self, another_parameter):
        self.shift.configure(to=int(self.count_letter_in_alphabet))

        # Put shift_value into Scale Entry
        self.scale_entry.configure(state="normal")
        self.scale_entry.delete(0, "end")
        self.scale_entry.insert(0, self.shift_var.get())
        self.scale_entry.configure(state="disabled")

    # Show shift frame, shift scale, scale entry box and shift text
    def show_shift_elements(self):
        self.scale_frame.grid(column=1, row=8, padx=20)
        self.shift.grid(column=0, row=0, padx=(20, 5), pady=(10, 0))
        self.scale_entry.grid(column=1, row=0, padx=(0, 20), pady=(10, 0))
        self.set_cipher_label.configure(text=f"Set cipher shift (1-{self.count_letter_in_alphabet})")
        self.set_cipher_label.grid(column=0, row=2, padx=(20, 0), pady=(0, 8))

    def open_and_read_user_file(self):
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
                    self.encode_decode_button.grid(column=1, row=9, ipadx=15, pady=(20,20))
                    self.save_button.grid(column=1, row=10, ipadx=15)

                    return self.text_editor
            except UnicodeDecodeError:
                warning_message = messagebox.showwarning(title="Wrong file extension!",
                                                         message="The file must have a .txt extension")

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
        # Make the "Save file" button active
        if button_key == 0:
            if self.encode_decode_button:
                self.save_button.configure(state="normal",
                                           text_color="white",
                                           fg_color="#18bc9c",
                                           hover_color="#128A72",
                                           border_width=0)

        # Make the "Open File" button active
        if button_key == 1:
            if self.select_cipher_language:
                self.open_button.configure(state="normal",
                                           text_color="white",
                                           fg_color="#3498db",
                                           hover_color="#375a7f",
                                           border_width=0)

    # Encoding/Decoding user file
    def encrypt_user_file(self):
        user_file = self.text_editor.get("1.0", END)
        print(user_file) #debug
        shift_amount = self.shift_var.get()

        # If the user select "Decode" shift == -shift
        if self.cipher_direction.get() == 1:
            shift_amount *= -1

        self.ciphertext = ""
        for line in user_file:
            for char in line:
                if char.lower() in self.alphabet:
                    position = self.alphabet.index(char.lower())
                    new_position = position + (shift_amount % (int(self.count_letter_in_alphabet)))
                    self.ciphertext += self.alphabet[new_position]
                else:
                    self.ciphertext += char
        print(self.ciphertext) #debug
        return self.ciphertext

if __name__ == '__main__':
    # Initialize app window
    window = App()
    window.configure(padx=10, pady=15)
    window.mainloop()