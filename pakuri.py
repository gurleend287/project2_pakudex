import math


class Pakuri:
    # default constructor
    def __init__(self, species: str, level: int):
        self.__species = species
        self.__level = level
        self.__attack = (len(self.__species) * 7 + 11) % 16
        self.__defense = (len(self.__species) * 5 + 17) % 16
        self.__stamina = (len(self.__species) * 6 + 13) % 16

    # returns spcies of this critter
    def get_species(self):
        return self.__species

    # returns attack value for this critter
    def get_attack(self):
        return self.__attack

    # returns the defense value for this critter
    def get_defense(self):
        return self.__defense

    # returns speed of this critter
    def get_stamina(self):
        return self.__stamina

    # changes attack value for this critter to new_attack
    def set_attack(self, new_attack: int):
        self.__attack = new_attack

    # calculates and returns Pakuri object's combat power (CP)
    @property
    def cp(self):
        cp = math.floor(self.__attack * math.sqrt(self.__defense) * math.sqrt(self.__stamina) * self.__level * 0.08)
        return cp

    # calculates and returns Pakuri object's health points (HP)
    @property
    def hp(self):
        hp = math.floor(self.__stamina * self.__level / 6)
        return hp

    @property
    # level getter property
    def level(self):
        return self.__level

    # level setter property
    @level.setter
    def level(self, level: int):
        self.__level = level