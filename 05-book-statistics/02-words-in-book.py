import string
import os


def text_into_word_array(text):
    for char in ['.', ',', '!', '(', ')', ':', ';', '?', '{', '}', '[', ']']:
        text = text.replace(char, " ")
    return text.split()

filepath = os.path.join('texts_for_processing', 'Six word story, by ErasedCitizen.txt')
with open(filepath, 'r', encoding='utf-8') as book_file:
    book_text = book_file.read()
    print(book_text)
    print(text_into_word_array(book_text))
