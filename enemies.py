class Enemy:
    def __init__(self, name, strength, min_lvl, max_lvl):
        self.name = name
        self.strength = strength
        self.min_lvl = min_lvl
        self.max_lvl = max_lvl

zombie = Enemy("Zombie", 2, 1, 1)
lost_soul = Enemy("Lost soul", 2, 1, 1)
sandworm = Enemy("Sandworm", 2, 1, 1)
mike_wazowski = Enemy("Mike Wazowski", 3, 1, 1)
wolf_spider = Enemy("Wolf spider", 3, 1, 2)
mega_knight = Enemy("Mega knight", 4, 1, 2)
troll = Enemy("Troll", 4, 1, 2)
werewolf = Enemy("Werewolf", 4, 2, 5)
vampire = Enemy("Vampire", 5, 2, 5)
the_devil = Enemy("The devil", 6, 3, 5)
emerald_dragon = Enemy("Emerald dragon", 8, 3, 5)
final_boss = Enemy("Typhon", 12, 4, 100)