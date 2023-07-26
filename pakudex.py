from pakuri import Pakuri


class Pakudex:
    # default construction that prepares a new Pakudex object
    def __init__(self):
        self.pakudex_list = []

    # returns a list of names of the species of the critters as ordered in the Pakudex
    # if there are no species added yet, return None
    def get_species_list(self):
        if len(self.pakudex_list) == 0:
            return None
        else:
            species_list = []
            for item in self.pakudex_list:
                species_list.append(item.get_species())
            return species_list

    # returns an int list containing the level, CP, and HP of species
    # if species not in Pakudex, return None
    def get_stats(self, species: str):
        if self.pakudex_list is None:
            return None
        else:
            stats_list = []
            for item in self.pakudex_list:
                if item.get_species() == species:
                    stats_list.append(item.level)
                    stats_list.append(item.cp)
                    stats_list.append(item.hp)
                    return stats_list
                else:
                    return None

    # sorts Pakuri objects in this Pakudex according to Python standard lexicographical ordering of species name
    def sort_pakuri(self):
        self.pakudex_list.sort(key=lambda x: x.get_species())

    # adds species to the Pakudex: if successful, return True, and False otherwise
    def add_pakuri(self, species: str, level: int):
        # temp value to check for duplicates
        x = True
        if self.pakudex_list is not None:
            for index, item in enumerate(self.pakudex_list):
                if item.get_species() == species:
                    x = False
                    return x
        # if no duplicate, then add Pakuri
        if x is True:
            self.pakudex_list.append(Pakuri(species, level))
            for index, item in enumerate(self.pakudex_list):
                if index == (len(self.pakudex_list) - 1) and item.get_species() == species:
                    return True

    # removes a species from the pakudex: if successful, return True, and False otherwise
    def remove_pakuri(self, species: str):
        for index, item in enumerate(self.pakudex_list):
            if item.get_species() == species:
                self.pakudex_list.pop(index)

        for index, item in enumerate(self.pakudex_list):
            if item.get_species() == species:
                return False
            elif index == (len(self.pakudex_list) - 1) and item.get_species() != species:
                return True

    # attempts to evolve species within the Pakudex: should double level and increment attack by 1
    # if successful, return True, and False otherwise
    def evolve_species(self, species: str):
        if self.pakudex_list is None:
            return False
        else:
            for index, item in enumerate(self.pakudex_list):
                if item.get_species() == species:
                    level1 = item.level
                    level2 = level1 * 2
                    item.level = level2
                    attack1 = item.get_attack()
                    item.set_attack(attack1 + 1)
                    return True
                else:
                    return False


# prints user menu
def menu():
    # print()
    print('Pakudex Main Menu')
    print('-----------------')
    print('''1. List Pakuri
2. Show Pakuri
3. Add Pakuri
4. Remove Pakuri
5. Evolve Pakuri
6. Sort Pakuri
7. Exit''')
    print()

    # prompts user for input
    menu_choice = input('What would you like to do? ')

    # menu selection error check
    while not menu_choice.isdigit() or int(menu_choice) > 7 or int(menu_choice) < 1:
        print()
        print("Unrecognized menu selection!")
        print()
        print('Pakudex Main Menu')
        print('-----------------')
        print('''1. List Pakuri
2. Show Pakuri
3. Add Pakuri
4. Remove Pakuri
5. Evolve Pakuri
6. Sort Pakuri
7. Exit''')
        print()
        menu_choice = input('What would you like to do? ')

    return int(menu_choice)


def main():
    print("Welcome to Pakudex: Tracker Extraordinaire!")
    print()
    menu_choice = menu()
    pakudex = Pakudex()
    while 0 < menu_choice < 8:
        match menu_choice:
            # should number and list the critters in Pakudex in the order contained (or sorted)
            case 1:
                species_list = pakudex.get_species_list()
                # when no Pakuri have been added
                if species_list is None:
                    print()
                    print('No Pakuri currently in the Pakudex!')
                    print()
                else:
                    print()
                    print('Pakuri in Pakudex:')

                    for index, item in enumerate(species_list):
                        index2 = index + 1
                        print(index2, end='')
                        print(".", item)
                    print()

                menu_choice = menu()

            # prompts user for a species and collect species information to display
            case 2:
                print()
                name = input("Enter the name of the species to display: ")

                stats_list = pakudex.get_stats(name)
                # when no such Pakuri in pakudex
                if stats_list is None:
                    print("Error: No such Pakuri!")
                    print()
                else:
                    print()
                    print("Species:", name)
                    print("Level:", stats_list[0])
                    print("CP:", stats_list[1])
                    print("HP:", stats_list[2])
                    print()

                menu_choice = menu()

            # adding Pakuri: prompt displays to read in the species name and level (if not a duplicate)
            case 3:
                species_list = pakudex.get_species_list()
                print()
                name = input("Species: ")
                x = True
                # duplicate Pakuri
                if species_list is not None:
                    for item in species_list:
                        if item == name:
                            print("Error: Pakudex already contains this species!")
                            print()
                            x = False
                # if duplicate show menu again
                if x is False:
                    menu_choice = menu()
                # level input error check
                while x is True:
                    try:
                        level = int(input("Level: "))
                        assert (level >= 0)
                        break
                    except ValueError:
                        print('Invalid level!')
                    except:
                        print('Level cannot be negative.')

                if x is True:
                    pakuri = Pakuri(name, level)
                    pakudex.pakudex_list.append(pakuri)
                    print('Pakuri species', name, "(level", level, end='')
                    print(") added!")
                    print()
                    menu_choice = menu()

            # removing Pakuri: prompts for species name and removes it if found in Pakudex
            case 4:
                print()
                name = input("Enter the name of the Pakuri to remove: ")
                for index, item in enumerate(pakudex.get_species_list()):
                    if item == name:
                        in_list = True
                        break
                    else:
                        in_list = False
                if not in_list:
                    print("Error: No such Pakuri!")
                    print()
                elif pakudex.remove_pakuri(name):
                    print("Pakuri", name, "removed.")
                    print()
                menu_choice = menu()

            # evolving Pakuri: prompts for a species and evolves if it exists
            case 5:
                print()
                name = input("Enter the name of the species to evolve: ")
                if pakudex.evolve_species(name):
                    print(name, " has evolved!")
                    print()
                else:
                    print("Error: No such Pakuri!")
                    print()
                menu_choice = menu()

            # sorts Pakuri in Python standard lexicographical order
            case 6:
                if pakudex.pakudex_list is not None:
                    pakudex.sort_pakuri()
                    # does sort function crash when nothing in list?
                    print()
                    print("Pakuri have been sorted!")
                    print()
                menu_choice = menu()

            # exit case
            case 7:
                print()
                print('Thanks for using Pakudex! Bye!')
                break


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
