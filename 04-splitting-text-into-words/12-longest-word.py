def text_into_word_array(text):
    for char in ['.', ',', '!', '(', ')', ':', ';', '?', '{', '}', '[', ']']:
        text = text.replace(char, " ")
    return text.split()


def show_longest_word(text):
    print("longest word in " + text)
    words = text_into_word_array(text)
    if len(words) == 0:
        print("no words in text")
        return
    longest_word = words[0]
    for word in text_into_word_array(text):
        print(word)
        print(len(word))
        if len(longest_word) < len(word):
            print("new longest word")
            longest_word = word
        print()
    print(longest_word)

show_longest_word("Ala ma kota. Marysia ma rysia. Czyli Marysia też ma kota.")
show_longest_word("!!!!!!!!!!")
show_longest_word("Aaaaaaaaaaaaaaaaaaaaaaaaby żółwia sprzedam")
