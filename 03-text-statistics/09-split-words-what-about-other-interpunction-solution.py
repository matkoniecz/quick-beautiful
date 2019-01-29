import string

text = "Ala ma żółtego kota."
for char in string.punctuation:
    text = text.replace(char, "")
print(text.split())

# alternative solution with regexp
# above is better for newbies as it avoids topic of regexp
# and reminds about for loop syntax
import re
print(re.split('\W+', text))