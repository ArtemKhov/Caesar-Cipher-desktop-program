class Alphabet():
    def __init__(self, file_name):
        self.file = open(file_name, "r")
        self.language = []
        for letter in self.file:
            self.language += letter.split(",")

    def encrypt_text(self, user_file, shift_amount: int, cipher_direction: str):
        count_letter_in_alphabet = len(self.language) // 2
        self.user_file = open(user_file, "r")

        if cipher_direction == "decode":
            shift_amount *= -1

        shift = shift_amount % count_letter_in_alphabet

        final_text = ""
        for line in self.user_file:
            for char in line:
                if char.lower() in self.language:
                    position = self.language.index(char.lower())
                    new_position = position + shift
                    final_text += self.language[new_position]
                else:
                    final_text += char

        with open("result.txt", "w") as result_file:
            result_file.write(final_text)
        return final_text


