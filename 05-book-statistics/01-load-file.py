import os

filepath = os.path.join('texts_for_processing', 'Six word story, by Newtonswig.txt')
with open(filepath, 'r', encoding='utf-8') as book_file:
    book_text = book_file.read()
    print(book_text)