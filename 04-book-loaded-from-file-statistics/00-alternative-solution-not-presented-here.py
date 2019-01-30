# alternative solution with regexp
# solution presented here is alternative and avoids topic of regexp
# and reminds about for loop syntax
import re

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

print(re.split(r'\W+', text))
