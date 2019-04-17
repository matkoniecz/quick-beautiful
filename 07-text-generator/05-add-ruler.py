import random

def is_feminine_word(word):
    return word[-1] == "a"

def select_variant(control_word, word_with_variants):
    if is_feminine_word(control_word):
        return word_with_variants["feminine"]
    else:
        return word_with_variants["masculine"]

def construction_adjectives():
    return [
        # store variants for grammatical genders
        {"feminine": "sławna", "masculine": "sławny"},
        {"feminine": "wspaniała", "masculine": "wspaniały"},
        {"feminine": "piękna", "masculine": "piękny"},
        {"feminine": "zarośnięta", "masculine": "zarośnięty"},
        {"feminine": "zniszczona", "masculine": "zniszczony"},
        {"feminine": "droga", "masculine": "drogi"},
        {"feminine": "wapienna", "masculine": "wapienny"},
    ]

def construction_types():
    return ["zamek", "fort", "gród", "forteca", "strażnica"]

def leader_names():
    return ["Eufemia", "Jadwiga", "Marianna", "Kunegunda",
    "Piotr", "Bolesław", "Kazimierz", "Arnulf"]

def main():
    selected_type = random.choice(construction_types())
    selected_adjective = random.choice(construction_adjectives())
    selected_adjective = select_variant(selected_type, selected_adjective)
    selected_leader = random.choice(leader_names())
    construction_year = str(random.randint(1, 1800))

    ruling = select_variant(selected_leader, {"feminine": "Rządziła", "masculine": "Rządził"})
    pointer = select_variant(selected_type, {"feminine": "ta", "masculine": "ten"})
    change = select_variant(selected_type, {"feminine": "została", "masculine": "został"})
    construction = select_variant(selected_type, {"feminine": "zbudowana", "masculine": "zbudowany"})
    print(pointer.capitalize(), selected_adjective, selected_type, change, construction, "w roku", construction_year+".")
    print(ruling, "wtedy", selected_leader+".")
    
main()
 
