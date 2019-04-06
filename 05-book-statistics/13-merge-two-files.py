from PIL import Image
import collections
from wordcloud import WordCloud
from PIL import ImageDraw
from PIL import ImageFont
import collections
import os


def main():
    filepath = os.path.join('texts_for_processing', 'Ania z Wyspy, Lucy Maud Montgomery, przełożył Andrzej Magórski.txt')
    make_word_cloud(filepath, 'word_cloud.png')
    statistics = load_text_and_describe_it(filepath)
    generate_image_with_text(['Ania z Wyspy', ''] + statistics, 'text_description.png')
    base = Image.open("text_description.png")
    word_cloud = Image.open("word_cloud.png")
    base.paste(word_cloud, (300, 40))
    base.show()


def make_word_cloud(book_file_filepath, output_filepath):
    with open(book_file_filepath, 'r', encoding='utf-8') as book_file:
        book_text = book_file.read()
        words = text_words(book_text)
        word_frequencies = collections.Counter()
        word_frequencies.update(words)

        # Generate a word cloud image
        wordcloud = WordCloud().generate_from_frequencies(word_frequencies)

        # Display the generated image:
        image = wordcloud.to_image()
        image.save(output_filepath)


def text_words(text):
    for_removal = ['.', ',', '!', ':', ';', '?', '(', ')', '—', '”', '“']
    for znak in for_removal:
        text = text.replace(znak, " ")
    return text.lower().split()


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
    zlikwidować = ['.', ',', '!', ':', ';', '?', '(', ')', '—', '”', '“']
    for znak in zlikwidować:
        text = text.replace(znak, " ")
    return text.lower().split()


def generate_image_with_text(text_lines, output_filepah):
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

    im.save(output_filepah)


main()
