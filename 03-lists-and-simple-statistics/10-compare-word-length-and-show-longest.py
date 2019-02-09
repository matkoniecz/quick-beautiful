words = [
    'Connecticut',
    'zażółć',
    'Rechtsschutzversicherungsgesellschaften',
    'Python',
    'Siebentausendzweihundertvierundfünfzig',
    'supercalifragilisticexpialidocious',
]

longest_word = words[0]
length = len(words[0])
for word in words:
    if length < len(word):
        length = len(word)
        longest_word = word
print(longest_word)

# task: show shortest one?
# task: what would happen after removing len() function?
