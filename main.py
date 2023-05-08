import tkinter
from alphabet import Alphabet

english_alphabet = Alphabet("english.txt")

a = english_alphabet.encrypt_text("aaA", 2, 'ere')

print(a)


