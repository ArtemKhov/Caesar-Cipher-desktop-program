class Alphabet():
    def __init__(self, file_name):
        self.file = open(file_name, "r")
        self.language = []
        for letter in self.file:
            self.language += letter.split(",")

        self.count_letter_in_alphabet = len(self.language)
        if self.count_letter_in_alphabet % 2 == 0:
            self.count_letter_in_alphabet = len(self.language) // 2
        else:
            self.count_letter_in_alphabet = len(self.language) // 2 + 1

    def encrypt_text(self, user_file, shift_amount: int, cipher_direction: str):
        self.user_file = open(user_file, "r")

        if cipher_direction == "decode":
            shift_amount *= -1

        self.shift_scale(shift_amount)

        final_text = ""
        for line in self.user_file:
            for char in line:
                if char.lower() in self.language:
                    position = self.language.index(char.lower())
                    new_position = position + self.shift
                    final_text += self.language[new_position]
                else:
                    final_text += char

        with open("result.txt", "w") as result_file:
            result_file.write(final_text)
        return final_text

    def shift_scale(self, shift_amount: int):
        self.shift = shift_amount % self.count_letter_in_alphabet



