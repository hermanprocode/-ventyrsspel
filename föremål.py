class Föremål:
    def __init__(self, namn, beskrivning, sällsynthet, styrka_bonus, hp_bonus, slump_lägre, slump_högre):
        self.namn = namn
        self.styrka_bonus = styrka_bonus
        self.hp_bonus = hp_bonus
        self.beskrivning = beskrivning
        self.sällsynthet = sällsynthet
        self.slump_lägre = slump_lägre
        self.slump_högre = slump_högre


mjölk = Föremål(
    "Mjölk", "Ger dig 1 hp, det finns myter om att detta är tjurens prostatavätska", "Common", 0, 1, None, None)
äppelskrutt = Föremål("Äppelskrutt", "ger ingen näring",
                      "Common", 0, 0, None, None)
bröd = Föremål(
    "Bröd", "Ger dig 1 hp, vanlig mat som har ätits i tusentals år", "Common", 0, 1, None, None)
vattenflaska = Föremål(
    "Vattenflaska", "Ger dig mellan 1 och 2 hp, alla behöver vatten", "Common", 0, 0, 1, 2)
ägg = Föremål(
    "Ägg", "Ger dig -1 hp men +1 strength, innehåller mycket protein", "Common", 1, -1, None, None)
köttbullar = Föremål(
    "Köttbullar", "En klassisk svensk rätt, barnen och ungdomar älskar köttbullar", "Common", 1, 0, None, None)
skolmat = Föremål("Skolmat", "Ger dig 4 hp men -1 strength",
                  "Rare", -1, 4, None, None)
fugu = Föremål(
    "Fugu", "Ger dig mellan -3 och 3 hp, en mycket känd maträtt i Japan som lika väl kunde döda dig som det skulle kunna vara en maträtt för gudarna", "Rare", 1, 0, -3, 3)
taco_buffe = Föremål(
    "Taco Buffé", "Ger dig 1 strength. En rätt som kommer hålla dig mätt resten av dagen", "Rare", 1, 0, None, None)
kräftor = Föremål("Kräftor", "Ger dig 2 hp och 1 strength, brukar ätas i Augusti då det är kräftskiva",
                  "Rare", 1, 2, None, None)
vodka = Föremål("Vodka", "Drick om du vågar, kan ge sidoeffekter",
                "Rare", 2, 0, -1, 0)
oboy = Föremål("Oboy", "Ger dig 4 hp och 1 strength, Blev populärt på 80-talet, Benes favorit",
               "Legendary", 1, 4, None, None)
svart_vattenmelon = Föremål(
    "Svart vattenmelon", "Såldes för 12 000 $ och är en av de dyraste råvarorna som finns i världen, definitivt en råvara värdig en kung. Ger dig 2 hp och 2 strength", "Legendary", 2, 2, None, None)
wagyu_beef = Föremål("Wagyu beef", "När vi tänker på en dyr köttbit tänker vi alla på oxfilé, men denna luxurösa köttbit är tillräckligt dyr för att mata en liten by i afrika under 1 år. Ger dig 3 strength", "Legendary", 3, 0, None, None)
