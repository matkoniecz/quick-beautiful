import string
def text_into_word_array(text):
    for char in string.punctuation:
        text = text.replace(char, " ")
    return text.split()

filepath = "texts_for_processing/Six word story, by ErasedCitizen.txt"
with open(filepath, 'r') as book_file:
    book_text = book_file.read()
    print(book_text)
    print(text_into_word_array(book_text))