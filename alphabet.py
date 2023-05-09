class Alphabet():
    def __init__(self, file_name):
        self.file = open(file_name, "r")
        self.language = []
        for letter in self.file:
            self.language += letter.split(",")

    def encrypt_text(self, user_file, shift_amount: int, cipher_direction: str):
        self.user_file = open(user_file, "r")

        if cipher_direction == "decode":
            shift_amount *= -1

        shift = shift_amount % 26

        final_encrypted_position = ''
        for line in self.user_file:
            for char in line:
                if char.lower() in self.language:
                    position = self.language.index(char.lower())
                    new_position = position + shift
                    final_encrypted_position += self.language[new_position]
                else:
                    final_encrypted_position += char

        return final_encrypted_position
