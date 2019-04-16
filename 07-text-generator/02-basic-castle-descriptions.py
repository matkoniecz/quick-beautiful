import random

def main():
    construction_adjectives = ["sławny", "wspaniały", "sławny", "zarośnięty", "zniszczony", "drogi", "wapienny"]
    construction_type = ["zamek", "fort", "gród"]
    leader_name = ["Eufemia", "Jadwiga", "Marianna", "Kunegunda",
    "Piotr", "Bolesław", "Kazimierz", "Arnulf"]

    selected_adjective = random.choice(construction_adjectives)
    selected_type = random.choice(construction_type)
    selected_leader = random.choice(leader_name)
    construction_year = str(random.randint(1, 1800))

    print("Ten", selected_adjective, selected_type, "został zbudowany w roku", construction_year+".")
    print("Rządził(a) wtedy", selected_leader+".")

main()
