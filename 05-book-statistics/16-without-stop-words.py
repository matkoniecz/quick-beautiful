from PIL import Image
import collections
from wordcloud import WordCloud
from PIL import ImageDraw
from PIL import ImageFont
import collections
import os


def main():
    filepath = os.path.join('texts_for_processing', 'Ania z Wyspy, Lucy Maud Montgomery, przełożył Andrzej Magórski.txt')
    make_word_cloud(filepath, polish_stop_words(), 'word_cloud.png')
    statistics = load_text_and_describe_it(filepath)
    generate_image_with_text(['Ania z Wyspy', ''] + statistics, 'text_description.png')
    base = Image.open("text_description.png")
    word_cloud = Image.open("word_cloud.png")
    x_anchor = result_image_size()[0]-word_cloud_size()[0]
    y_anchor = int((result_image_size()[1]-word_cloud_size()[1])/2)
    base.paste(word_cloud, (x_anchor, y_anchor))
    base.show()


def background_color():
    return (255, 255, 255)


def text_color():
    return (28, 28, 28)


def result_image_size():
    return (800, 300)


def word_cloud_size():
    return (int(result_image_size()[0]*2/3), int(result_image_size()[1]*0.9))


def font_filepath():
    return "SpaceGrotesk-SemiBold.otf"


def word_to_color(word, **kwargs):
    return text_color()


def make_word_cloud(book_file_filepath, stop_words, output_filepath):
    with open(book_file_filepath, 'r', encoding='utf-8') as book_file:
        book_text = book_file.read()
        words = text_words(book_text)
        filtered = []
        for word in words:
            if word not in stop_words:
                filtered.append(word)
        word_frequencies = collections.Counter()
        word_frequencies.update(filtered)
        # Generate a word cloud image
        wordcloud = WordCloud(
            background_color=background_color(),
            repeat=False,
            font_path=font_filepath(),
            width=word_cloud_size()[0],
            height=word_cloud_size()[1],
        )
        wordloud = wordcloud.generate_from_frequencies(word_frequencies)
        wordcloud.recolor(color_func=word_to_color)

        # Display the generated image:
        image = wordcloud.to_image()
        image.save(output_filepath)


def polish_stop_words():
    return ['się', 'nie', 'i', 'w', 'że', 'z', 'na', 'to', 'do', 'o', 'a',
            'jest', 'tak', 'jak', 'gdy', 'za', 'co', 'była', 'już', 'po', 'mnie',
            'go', 'był', 'od', 'aby', 'ale', 'jej']


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


def generate_image_with_text(text_lines, output_filepath):
    im = Image.new("RGB", result_image_size(), background_color())
    y_line_anchor = 10
    font = ImageFont.truetype(font_filepath(), 14)
    for line in text_lines:
        ImageDraw.Draw(
            im
        ).text(
            (10, y_line_anchor),
            line,
            text_color(),
            font=font
        )
        y_line_anchor += 18

    im.save(output_filepath)


main()
