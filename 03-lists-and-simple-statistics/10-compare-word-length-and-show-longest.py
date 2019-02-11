words = [
    'Connecticut',
    'zażółć',
    'Rechtsschutzversicherungsgesellschaften',
    'Python',
    'Siebentausendzweihundertvierundfünfzig',
    'supercalifragilisticexpialidocious',
]

longest_word = words[0]
for word in words:
    if len(longest_word) < len(word):
        longest_word = word
print(longest_word)

# task: show shortest one?
# task: what would happen after removing len() function?
