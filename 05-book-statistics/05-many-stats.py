import collections
import os

# docs at https://github.com/amueller/word_cloud


def main():
    filepath = os.path.join('..', 'texts_for_processing', 'Ania z Wyspy, Lucy Maud Montgomery, przełożył Andrzej Magórski.txt')
    with open(filepath, 'r', encoding='utf-8') as book_file:
        book_text = book_file.read()
        words = text_words(book_text)
        print("ilość słów w książce:", len(words))
        longest_word = ''
        for word in words:
            if len(longest_word) < len(word):
                longest_word = word
        print("najdłuższe słowo:", longest_word)
        word_frequencies = collections.Counter()
        word_frequencies.update(words)
        print("najczęstsze słowa:", word_frequencies.most_common(50))
        print("najrzadsze słowa:", word_frequencies.most_common()[-10:-1])
        print("ile znaków książce:", len(book_text))
        print("ilość stron:", len(book_text)//1800+1)
        unique_words = set(words)
        print("ilość różnych słów:", len(unique_words))


def text_words(text):
    zlikwidować = ['.', ',', '!', ':', ';', '?', '(', ')', '—', '”', '“']
    for znak in zlikwidować:
        text = text.replace(znak, " ")
    return text.lower().split()


main()
