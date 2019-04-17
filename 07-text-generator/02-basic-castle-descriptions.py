import random

def main():
    selected_adjective = random.choice(construction_adjectives())
    selected_type = random.choice(construction_types())
    construction_year = str(random.randint(1, 1800))
    print("Ten", selected_adjective, selected_type, "został zbudowany w roku", construction_year+".")

def construction_adjectives():
    return ["sławny", "wspaniały", "sławny", "zarośnięty", "zniszczony", "drogi", "wapienny"]

def construction_types():
    return ["zamek", "fort", "gród"]

main()
