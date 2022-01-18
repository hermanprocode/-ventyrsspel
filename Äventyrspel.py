import random as rand
from traps import *
from items import *
from enemies import *

# Den här funktionen visar sitt inventory och låter en använda sina items


def showInv(hp, strength, max_hp, inventory):
    svar = 10
    sure = "placeholder"
    while svar > len(inventory) or svar < 1:
        for i, item in enumerate(inventory):
            print(f"[{i+1}] {item.name}")
        try:
            svar = int(input(
                "Vilket föremål vill du använda? Välj genom föremålets position 1,2,3.... "))
        except:
            print("\nOgiltigt svar, svaret måste vara ett heltal")
            continue
        if svar <= len(inventory) and len(inventory) >= 1 and svar >= 1:
            print(
                f"\n{inventory[svar-1].name}\n{inventory[svar-1].rarity}\n{inventory[svar-1].description}")
            while sure != "ja" and sure != "nej":
                try:
                    sure = input(
                        f"Är du säker att du vill använda {inventory[svar-1].name} [ja], [nej] -> ")
                except:
                    print("Ogiltigt svar, svara med ja eller nej")
                    continue
                if sure.upper() != "JA" and sure != "NEJ":
                    print("Ogiltigt svar, svara med ja eller nej")
            if sure.upper() == "JA":
                if inventory[svar-1].rand_lower == None:
                    hp = hp + inventory[svar-1].hp_bonus
                    strength = strength + inventory[svar-1].strength_bonus
                    print(
                        f"Din strength ökade med {inventory[svar-1].strength_bonus} och ditt hp med {inventory[svar-1].hp_bonus}")
                else:
                    slumptal = rand.randint(
                        inventory[svar-1].rand_lower, inventory[svar-1].rand_upper)
                    hp = hp + slumptal
                    strength = strength + inventory[svar-1].strength_bonus
                    if slumptal >= 0:
                        print(
                            f"\nDin strength ökade med {inventory[svar-1].strength_bonus} och ditt hp med {slumptal}")
                    else:
                        print(
                            f"\nDin strength ökade med {inventory[svar-1].strength_bonus} men ditt hp gick ned med {slumptal}")
                if hp >= max_hp:
                    print("Du nådde max hp, levla upp för att öka max hp")
                    hp = max_hp
                inventory.remove(inventory[svar-1])
                return hp, strength
            else:
                print("Stänger inventory")
                return hp, strength
        else:
            print(f"\nHittade inte ett item vid position {svar}")

# Den här funktionen kontrollerar dörrarna och bestämmer vad som ska vara bakom varje dörr


def checkDoor(svar, list):
    if list[svar-1] < 2:
        return "item"
    elif list[svar-1] > 1 and list[svar-1] < 5:
        return "enemy"
    elif list[svar-1] > 4:
        return "trap"


# Den här funktionen slumpar fram ett item från en random rarity. Den kollar också om ditt inventory är fullt och om det är fallet frågar den om du vill byta ut itemet mot ett annat i ditt inventory
def chooseAndAddItem(slumptal, upper_limit, lower_limit, rarity_upper_limit, rarity_lower_limit, inventory):
    svar = ""
    all_items = [mjolk, appelskrutt, agg, brod, kottbullar, vattenflaska, taco_buffe,
                 skolmat, vodka, kraftor, fugu, oboy, svart_vattenmelon, wagyu_beef]
    if slumptal <= upper_limit and slumptal > lower_limit:
        slumptal = rand.randint(rarity_lower_limit, rarity_upper_limit)
        print(
            f"\n{all_items[slumptal].rarity}\nDu hittade {all_items[slumptal].name}")
        if len(inventory) < 5:
            print(f"{all_items[slumptal].name} lades till i ditt inventory")
            inventory.append(all_items[slumptal])
        else:
            while svar.upper() != "JA" and svar.upper() != "NEJ":
                try:
                    svar = input(
                        f"\nDitt inventory är fullt\nVill du byta ut {all_items[slumptal].name} mot ett annat item i ditt inventory [ja] eller [nej] -> ")
                except:
                    print("Ogiltigt svar, svara med ja eller nej")
                    continue
                if svar.upper() != "JA" and svar.upper() != "NEJ":
                    print("Ogiltigt svar, svara med ja eller nej")
            if svar.upper() == "JA":
                svar = 10
                while svar > len(inventory) or svar < 1:
                    for x, i in enumerate(inventory):
                        print(f"[{x+1}] {i.name}")
                    try:
                        svar = int(input(
                            "Vilket föremål vill du byta ut? Välj genom föremålets position 1,2,3... -> "))
                    except:
                        print("\nOgiltigt svar, svaret måste vara ett heltal")
                        continue
                    if svar <= len(inventory) and svar >= 1:
                        print(
                            f"Du kastade iväg {inventory[svar-1].name} och bytte ut det mot {all_items[slumptal].name}")
                        inventory.pop(svar-1)
                        inventory.append(all_items[slumptal])
                    else:
                        print(f"\nHittade inte ett item vid position {svar}")


def openDoor(hp, strength, inventory, lvl, max_hp, win):
    doors = []
    svar = "placeholder"
    for i in range(3):
        doors.append(rand.randint(1, 5))
    while svar != 1 and svar != 2 and svar != 3:
        try:
            svar = int(
                input("\nVilken dörr vill du öppna, [1], [2] eller [3] -> "))
        except:
            print("Ogiltigt svar, svara med [1], [2] eller [3]")
            continue
        if svar != 1 and svar != 2 and svar != 3:
            print("Ogiltigt svar, svara med [1], [2] eller [3]")
    if svar == 1:
        behind_door = checkDoor(svar, doors)
    elif svar == 2:
        behind_door = checkDoor(svar, doors)
    elif svar == 3:
        behind_door = checkDoor(svar, doors)
    svar = ""
    if behind_door == "item":
        print("\nDu hittade en kista")
        while svar.upper() != "JA" and svar.upper() != "NEJ":
            try:
                svar = input("Vad gör du? öppna kistan [ja] eller [nej] -> ")
            except:
                print("Ogiltigt svar, svara med ja eller nej")
                continue
            if svar.upper() != "JA" and svar.upper() != "NEJ":
                print("Ogiltigt svar, svara med ja eller nej")
        if svar.upper() == "JA":
            slumptal = rand.randint(0, 100)
            chooseAndAddItem(slumptal, 60, 0, 5, 0, inventory)
            chooseAndAddItem(slumptal, 90, 60, 10, 6, inventory)
            chooseAndAddItem(slumptal, 100, 90, 13, 11, inventory)
        elif svar.upper() == "NEJ":
            print("Du lämmnade kistan oöppnad")
    elif behind_door == "trap":
        trapsen = [hjulfallan, ju_storre_de_ar,
                   fortnite_spike_trap, clashroyale_trap, snurrande_klingan, forsta_steget_fallan, dubbeldorrens_dom, dodskikaren, gubben_i_ladan, satans_bage, bowling, bomerang_kniv_domedagshandsken, gammal_mantel, hoppa_hage, dammsugar_fallan]
        slumptal = rand.randint(0, (len(trapsen)-1))
        print(f"\n{trapsen[slumptal].description}")
        svar = ""
        while svar != 1 and svar != 2 and svar != 3 and svar != 4:
            try:
                svar = int(input(f"\nVad gör du? {trapsen[slumptal].val} -> "))
            except:
                print("Ogiltigt svar, svara med [1], [2], [3] eller [4]")
                continue
            if svar != 1 and svar != 2 and svar != 3 and svar != 4:
                print("Ogiltigt svar, svara med [1], [2], [3] eller [4]")
        if svar == 1:
            print(f"\n{trapsen[slumptal].end1}")
        elif svar == 2:
            print(f"\n{trapsen[slumptal].end2}")
        elif svar == 3:
            print(f"\n{trapsen[slumptal].end3}")
        elif svar == 4:
            print(f"\n{trapsen[slumptal].end4}")
        if trapsen[slumptal].solution[svar-1] == "W":
            hp = hp - trapsen[slumptal].hp_loss
            print(f"Du förlorade {trapsen[slumptal].hp_loss} hp")
    elif behind_door == "enemy":
        giltiga_enemys = []
        enemys = [zombie, lost_soul, sandworm, mike_wazowski, wolf_spider,
                  mega_knight, troll, werewolf, vampire, the_devil, emerald_dragon, final_boss]
        for i in enemys:
            if lvl <= i.max_lvl and lvl >= i.min_lvl:
                giltiga_enemys.append(i)
        slumptal = rand.randint(0, (len(giltiga_enemys)-1))
        while svar.upper() != "JA" and svar.upper() != "NEJ":
            try:
                svar = input(
                    f"Du stötte på {giltiga_enemys[slumptal].name}, vill du slåss? [ja] eller [nej] -> ")
            except:
                print("Ogiltigt svar, svara med ja eller nej")
                continue
            if svar.upper() != "JA" and svar.upper() != "NEJ":
                print("Ogiltigt svar, svara med ja eller nej")
        if svar.upper() == "JA":
            if strength > giltiga_enemys[slumptal].strength:
                if giltiga_enemys[slumptal].name == "Typhon":
                    print("\nModiga kämpe du räddade denna alternativa värld och kommer gå genom historierna som en legend. Vi längtar till nästa gång vi möts")
                    win = True
                else:
                    print(
                        f"\nDu vann och levlade upp till {lvl+1}! Ditt max hp ökade till {max_hp + 1}, ditt hp gick upp med 1.")
                    lvl += 1
                    max_hp += 1
                    hp += 1
            elif strength < giltiga_enemys[slumptal].strength:
                print("\nDu förlorade, du tog 1 skada!")
                hp -= 1
            elif strength == giltiga_enemys[slumptal].strength:
                print(
                    "\nDet blev lika, ni skakade hand och called it a day")
        elif svar.upper() == "NEJ":
            spring = rand.randint(0, 10)
            if spring <= 3:
                print(
                    f"Du lyckades springa iväg från faran eftersom Ians fortnite dans skrämde livet ur {giltiga_enemys[slumptal].name} som kommer vara ärrad för livet")
            else:
                print(
                    f"Du sprang för ditt liv men blev distraherad av Rubens fortnite dans och {giltiga_enemys[slumptal].name} lyckades komma i kapp och du förlorade 1 hp")
                hp -= 1
    return hp, lvl, max_hp, win

# Huvudprogrammet som definerar några variablar och kallar på olika funktioner


def main():
    win = False
    hp = 5
    max_hp = 5
    strength = 3
    lvl = 1
    inventory = []
    while hp > 0 and win == False:
        try:
            svar = input(
                "\nVad vill du göra, visa stats [s], visa inventory [i], välja dörr [d], avsluta programmet [quit] -> ")
        except:
            print("Ogiltigt svar, svara med [s], [i] eller [d]")
        if svar.upper() == "S":
            print(f"Du har {hp} hp, {strength} styrka och är level {lvl}")
        elif svar.upper() == "I":
            if len(inventory) > 0:
                hp, strength = showInv(hp, strength, max_hp, inventory)
            else:
                print("Ditt inventory är tomt")
        elif svar.upper() == "D":
            hp, lvl, max_hp, win = openDoor(
                hp, strength, inventory, lvl, max_hp, win)
        elif svar.upper() == "QUIT":
            hp = 0
        else:
            print("Ogiltigt svar, svara med [s], [i] eller [d]")
    if hp == 0:
        print("GAME OVER")


main()
