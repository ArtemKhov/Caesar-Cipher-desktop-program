class Alphabet():
    def __init__(self, file_name):
        self.file = open(file_name, 'r')
        self.language = []
        for letter in self.file:
            self.language += letter.split(",")

    # сделать, считывание файла, а не передачу строки
    def encrypt_text(self, text: str, shift_amount: int, cipher_direction: str):
        length_alphabet = len(self.language)
        shift = shift_amount % length_alphabet
        final_encrypted_position = ''
        if cipher_direction == "decode":
            shift_amount *= -1
        for letter in text:
            if letter.lower() in self.language:
                position = self.language.index(letter.lower())
                new_position = position + shift
                final_encrypted_position += self.language[new_position]
            else:
                final_encrypted_position += letter

        return final_encrypted_position
