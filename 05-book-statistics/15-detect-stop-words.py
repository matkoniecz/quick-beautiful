import collections
import os


def filepath_of_file(file_name):
    return os.path.join('..', 'texts_for_processing', file_name)


def top_words_in_file(text_filename, n=50):
    with open(filepath_of_file(text_filename), 'r', encoding='utf-8') as book_file:
        book_text = book_file.read()
        words = text_words(book_text)
        word_frequencies = collections.Counter()
        word_frequencies.update(words)
        common = word_frequencies.most_common(n)
        return [a[0] for a in common]
        return common


def main():
    polish_text_filename_a = 'Ania z Wyspy, Lucy Maud Montgomery, przełożył Andrzej Magórski.txt'
    polish_text_filename_b = 'Anhelli, Juliusz Słowacki.txt'
    common_a = top_words_in_file(polish_text_filename_a)
    common_b = top_words_in_file(polish_text_filename_b)
    stop_words = []
    for candidate_word in common_a:
        if candidate_word in common_b:
            stop_words.append(candidate_word)
    print(stop_words)


def text_words(text):
    zlikwidować = ['.', ',', '!', ':', ';', '?', '(', ')', '—', '”', '“']
    for znak in zlikwidować:
        text = text.replace(znak, " ")
    return text.lower().split()


main()
