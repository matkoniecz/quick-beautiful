text = "Ala ma niebieskiego kota!"
for char in ['.', '!']:
    text = text.replace(char, "")
print(text.split())

"""
note that it will work well in a typical English or Polish text
but nearly every language rule has some exceptions

 for example:
  - https://en.wikipedia.org/wiki/!Kung_languages (yes, ! is part of the word)
  - https://en.wikipedia.org/wiki/!!! (it is a band - and this Wikipedia
    article is just one possible text about them)
  - words in Juǀʼhoan language language may have exxclamation mark in the middle
    see http://www.sscnet.ucla.edu/history/ehret/Khoisan100word.pdf
    that has examples such as "n!om" meaning "to fly"

Any processing of text using simple replacements will have problems with such cases.
And even complex one will have trouble to distinguish exclamation mark used as
a puctuation in "Ha! Ha!" and use as a letter in "Saint-Louis-du-Ha! Ha!" town name

Yes, seriously - see https://en.wikipedia.org/wiki/Saint-Louis-du-Ha!_Ha!
"""
