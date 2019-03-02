def text_into_word_array(text):
    for char in ['.', ',', '!', '(', ')', ':', ';', '?', '{', '}', '[', ']']:
        text = text.replace(char, " ")
    return text.split()


# note splits without introducing newlines
text = "KARTOFLE Z PIECA. Kartofle surowe, obrane z łupinek, pokrajać w \
cieniuchne płatki. Na kilo takich kartofli (już obranych) wziąć pięć deka \
szmalcu i pięć deka masła. Dwadzieścia deka cebuli pokrajać w paski, \
przesmażyć ze szmalcem i masłem, włożyć kartofle, smażyć dalej na wolnym \
ogniu, potrząsając patelnią i mięszając. Po dziesięciu minutach osolić, \
popieprzyć, przełożyć do ogniotrwałej foremki lub nelsonki, wstawić w miernie \
gorący piec na pół godziny lub nieco więcej. Podawać w tem samem naczyniu, \
posypane zielonym koperkiem lub pietruszeczką.."

print(text_into_word_array(text))
