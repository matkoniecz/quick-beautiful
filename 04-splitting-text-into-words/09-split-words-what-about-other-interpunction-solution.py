import string

text = "Ala ma żółtego kota."
for char in string.punctuation:
    text = text.replace(char, "")
print(text.split())
