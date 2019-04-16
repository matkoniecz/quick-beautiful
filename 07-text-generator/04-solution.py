import random

def is_feminine_word(word):
    return word[-1] == "a"

def main():
    construction_adjectives = [
        # store variants for grammatical genders
        {"feminine": "sławna", "masculine": "sławny"},
        {"feminine": "wspaniała", "masculine": "wspaniały"},
        {"feminine": "piękna", "masculine": "piękny"},
        {"feminine": "zarośnięta", "masculine": "zarośnięty"},
        {"feminine": "zniszczona", "masculine": "zniszczony"},
        {"feminine": "droga", "masculine": "drogi"},
        {"feminine": "wapienna", "masculine": "wapienny"},
    ]
    construction_type = ["zamek", "fort", "gród", "forteca", "strażnica"]

    leader_name = ["Eufemia", "Jadwiga", "Marianna", "Kunegunda",
    "Piotr", "Bolesław", "Kazimierz", "Arnulf"]

    selected_adjective = random.choice(construction_adjectives)
    selected_type = random.choice(construction_type)
    if is_feminine_word(selected_type):
        selected_adjective = selected_adjective["feminine"]
    else:
        selected_adjective = selected_adjective["masculine"]
    selected_leader = random.choice(leader_name)
    construction_year = str(random.randint(1, 1800))

    ruling = {"feminine": "Rządziła", "masculine": "Rządził"}
    if is_feminine_word(selected_leader):
        ruling = ruling["feminine"]
    else:
        ruling = ruling["masculine"]

    pointer = {"feminine": "ta", "masculine": "ten"}
    if is_feminine_word(selected_type):
        pointer = pointer["feminine"]
    else:
        pointer = pointer["masculine"]

    change = {"feminine": "została", "masculine": "został"}
    if is_feminine_word(selected_type):
        change = change["feminine"]
    else:
        change = change["masculine"]
    construction = {"feminine": "zbudowana", "masculine": "zbudowany"}
    if is_feminine_word(selected_type):
        construction = construction["feminine"]
    else:
        construction = construction["masculine"]

    print(pointer.capitalize(), selected_adjective, selected_type, change, construction, "w roku", construction_year+".")
    print(ruling, "wtedy", selected_leader+".")
    
main()
