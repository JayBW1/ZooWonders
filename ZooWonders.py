class animal():
    species = ""
    age = 0
    name = ""
    habits = ""
    habitat = ""
    diet = ""

    def __init__(self, species, age, name, habits, habitat, diet):
        self.species = species
        self.age = age
        self.name = name
        self.habits = habits
        self.habitat = habitat
        self.diet = diet

    def animal_get(file, species: str, group: list):
        with open(file, "r") as f:
            f.seek(0, 0)
            f_read = f.read()
            f_readlines = f_read.split("\n")
            for line in f_readlines:
                if species in line:
                    group.append(line)

animal_list = ["lion", "zebra"]
while True:
    group_list = []
    animal_select = input("Enter Animal Name: ").lower()
    if animal_select in animal_list:
        animal.animal_get("ZooWonders.txt", animal_select, group_list)
        print(group_list)
    