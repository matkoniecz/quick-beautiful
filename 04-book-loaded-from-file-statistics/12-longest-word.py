import string


def text_into_word_array(text):
    for char in string.punctuation:
        text = text.replace(char, " ")
    return text.split()


text = "Ala ma kota. Marysia ma rysia. Czyli Marysia też ma kota."


print("longest word")
longest_word = None
longest_word_length = 0
for word in text_into_word_array(text):
    print(word)
    print(len(word))
    if(longest_word_length < len(word)):
        print("new longest word")
        longest_word = word
        longest_word_length = len(word)
    print()

print()
