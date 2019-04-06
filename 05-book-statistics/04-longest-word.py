import string
import os


def text_into_word_array(text):
    for char in ['.', ',', '!', '(', ')', ':', ';', '?', '{', '}', '[', ']']:
        text = text.replace(char, " ")
    return text.split()

filepath = os.path.join('texts_for_processing', 'Ania z Wyspy, Lucy Maud Montgomery, przełożył Andrzej Magórski.txt')
with open(filepath, 'r', encoding='utf-8') as book_file:
    book_text = book_file.read()
    longest_word = ""
    for word in text_into_word_array(book_text):
        if len(longest_word) < len(word):
            longest_word = word
            print("new longest word", longest_word)
            print()
    print(longest_word)

print()
