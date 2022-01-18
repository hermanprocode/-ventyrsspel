class Item:
    def __init__(self, name, description, rarity, strength_bonus, hp_bonus, rand_lower, rand_upper):
        self.name = name
        self.strength_bonus = strength_bonus
        self.hp_bonus = hp_bonus
        self.description = description
        self.rarity = rarity
        self.rand_lower = rand_lower
        self.rand_upper = rand_upper

mjolk = Item(
    "Mjölk", "Ger dig 1 hp, det finns myter om att detta är tjurens prostatavätska", "Common", 0, 1, None, None)
appelskrutt = Item("Äppelskrutt", "ger ingen näring",
                   "Common", 0, 0, None, None)
brod = Item(
    "Bröd", "Ger dig 1 hp, vanlig mat som har ätits i tusentals år", "Common", 0, 1, None, None)
vattenflaska = Item(
    "Vattenflaska", "Ger dig mellan 1 och 2 hp, alla behöver vatten", "Common", 0, 0, 1, 2)
agg = Item(
    "Ägg", "Ger dig -1 hp men +1 strength, innehåller mycket protein", "Common", 1, -1, None, None)
kottbullar = Item(
    "Köttbullar", "En klassisk svensk rätt, barnen och ungdomar älskar köttbullar", "Common", 1, 0, None, None)
skolmat = Item("Skolmat", "Ger dig 4 hp men -1 strength",
               "Rare", -1, 4, None, None)
fugu = Item(
    "Fugu", "Ger dig mellan -3 och 3 hp, en mycket känd maträtt i Japan som lika väl kunde döda dig som det skulle kunna vara en maträtt för gudarna", "Rare", 1, 0, -3, 3)
taco_buffe = Item(
    "Taco Buffé", "Ger dig 1 strength. En rätt som kommer hålla dig mätt resten av dagen", "Rare", 1, 0, None, None)
kraftor = Item("Kräftor", "Ger dig 2 hp och 1 strength, brukar ätas i Augusti då det är kräftskiva",
               "Rare", 1, 2, None, None)
vodka = Item("Vodka", "Drick om du vågar, kan ge sidoeffekter",
             "Rare", 2, 0, -1, 0)
oboy = Item("Oboy", "Ger dig 4 hp och 1 strength, Blev populärt på 80-talet, Benes favorit",
            "Legendary", 1, 4, None, None)
svart_vattenmelon = Item(
    "Svart vattenmelon", "Såldes för 12 000 $ och är en av de dyraste råvarorna som finns i världen, definitivt en råvara värdig en kung. Ger dig 2 hp och 2 strength", "Legendary", 2, 2, None, None)
wagyu_beef = Item("Wagyu beef", "När vi tänker på en dyr köttbit tänker vi alla på oxfilé, men denna luxurösa köttbit är tillräckligt dyr för att mata en liten by i afrika under 1 år. Ger dig 3 strength", "Legendary", 3, 0, None, None)
