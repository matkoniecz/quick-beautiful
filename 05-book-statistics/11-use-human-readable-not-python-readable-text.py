from PIL import ImageDraw
from PIL import ImageFont
from PIL import Image

import collections
import os


def main():
    filepath = os.path.join('texts_for_processing', 'Ania z Wyspy, Lucy Maud Montgomery, przełożył Andrzej Magórski.txt')
    statistics = load_text_and_describe_it(filepath)
    generate_image_with_text(['Ania z Wyspy', ''] + statistics)


def load_text_and_describe_it(filepath):
    returned = []
    with open(filepath, 'r', encoding='utf-8') as book_file:
        book_text = book_file.read()
        words = text_words(book_text)
        returned.append("ilość słów w książce: " + str(len(words)))
        longest_word = ''
        for word in words:
            if len(longest_word) < len(word):
                longest_word = word
        returned.append("najdłuższe słowo: " + longest_word)
        word_frequencies = collections.Counter()
        word_frequencies.update(words)
        returned.append("najczęstsze słowa: ")
        returned = returned + frequency_list_as_list_of_lines(word_frequencies.most_common(5))
        returned.append("ile znaków książce: " + str(len(book_text)))
        returned.append("ilość stron: " + str(len(book_text)//1800+1))
        unique_words = set(words)
        returned.append("ilość różnych słów: " + str(len(unique_words)))
    return returned


def frequency_list_as_list_of_lines(word_frequencies):
    returned = []
    for word, count in word_frequencies:
        returned.append("   " + word + " x" + str(count))
    return returned


def text_words(text):
    for_removal = ['.', ',', '!', ':', ';', '?', '(', ')', '—', '”', '“']
    for znak in for_removal:
        text = text.replace(znak, " ")
    return text.lower().split()


def generate_image_with_text(text_lines):
    width = 800
    height = 300
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    im = Image.new("RGB", (width, height), WHITE)
    y_line_anchor = 10
    font = ImageFont.truetype("SpaceGrotesk-SemiBold.otf", 14)
    for line in text_lines:
        ImageDraw.Draw(
            im
        ).text(
            (10, y_line_anchor),
            line,
            BLACK,
            font=font
        )
        y_line_anchor += 18

    im.show()
    im.save('text_description.png')


main()
