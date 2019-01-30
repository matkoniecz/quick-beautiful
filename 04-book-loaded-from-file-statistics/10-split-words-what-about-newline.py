import string

# note multiline string definition
text = """Ojcze nasz, któryś jest w niebie
święć się imię Twoje;
przyjdź królestwo Twoje;
bądź wola Twoja jako w niebie tak i na ziemi;
chleba naszego powszedniego daj nam dzisiaj;
i odpuść nam nasze winy,
jako i my odpuszczamy naszym winowajcom;
i nie wódź nas na pokuszenie;
ale nas zbaw od złego.

Amen."""

print("works, nice:")
for char in string.punctuation:
    text = text.replace(char, " ")
print(text.split())
