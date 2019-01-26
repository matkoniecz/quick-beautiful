import collections
import string

def text_into_word_array(text):
    for char in string.punctuation:
        text = text.replace(char, " ")
    return text.split()

text = "Ala ma kota. Marysia ma rysia. Czyli Marysia też ma kota."

frequencies = collections.Counter()
frequencies.update(text_into_word_array(text))
print(frequencies)
