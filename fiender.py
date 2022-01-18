class Fiende:
    def __init__(self, namn, styrka, min_lvl, max_lvl):
        self.namn = namn
        self.styrka = styrka
        self.min_lvl = min_lvl
        self.max_lvl = max_lvl

zombie = Fiende("Zombie", 2, 1, 1)
lost_soul = Fiende("Lost soul", 2, 1, 1)
sandworm = Fiende("Sandworm", 2, 1, 1)
mike_wazowski = Fiende("Mike Wazowski", 3, 1, 1)
wolf_spider = Fiende("Wolf spider", 3, 1, 2)
mega_knight = Fiende("Mega knight", 4, 1, 2)
troll = Fiende("Troll", 4, 1, 2)
werewolf = Fiende("Werewolf", 4, 2, 5)
vampire = Fiende("Vampire", 5, 2, 5)
the_devil = Fiende("The devil", 6, 3, 5)
emerald_dragon = Fiende("Emerald dragon", 8, 3, 5)
final_boss = Fiende("Typhon", 12, 4, 100)
