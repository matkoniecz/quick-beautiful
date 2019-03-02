text = "Ala ma żółtego kota."
for char in ['.', ',', '!', '(', ')', ':', ';', '?', '{', '}', '[', ']']:
    text = text.replace(char, "")
print(text.split())
