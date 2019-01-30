text = "Ala ma żółtego kota"

print("words:")
for word in text.split():
    print(word)
print()

# make short step for array explanation/reminder

print("words and their lengths:")
for word in text.split():
    print(word, len(word))
print()

print("words and the first letter")
for word in text.split():
    print(word, word[0])
print()

print("words and the second letter")
for word in text.split():
    print(word, word[1])
print()

print("words and the last letter")
for word in text.split():
    print(word, word[-1])
print()
