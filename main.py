import tkinter

english_alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                    'u', 'v', 'w', 'x', 'y', 'z']


def encrypt_text(text: str, shift_amount: int, cipher_direction:str):
    shift = shift_amount % 26
    final_encrypted_position = ''
    if cipher_direction == "decode":
        shift_amount *= -1
    for letter in text:
        if letter.lower() in english_alphabet:
            position = english_alphabet.index(letter.lower())
            new_position = position + shift
            final_encrypted_position += english_alphabet[new_position]
        else:
            final_encrypted_position += letter

    return final_encrypted_position

print(encrypt_text('AaA', 2))


