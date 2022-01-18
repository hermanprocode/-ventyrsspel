import random as rand
from fällor import *
from föremål import *
from fiender import *

# Den här funktionen visar sitt förråd och låter en använda sina föremål


def visa_förråd(hp, styrka, max_hp, förråd):
    svar = 10
    säker = "placeholder"
    while svar > len(förråd) or svar < 1:
        for i, föremål in enumerate(förråd):
            print(f"[{i+1}] {föremål.namn}")
        try:
            svar = int(input(
                "Vilket föremål vill du använda? Välj genom föremålets position 1,2,3.... "))
        except:
            print("\nOgiltigt svar, svaret måste vara ett heltal")
            continue
        if svar <= len(förråd) and len(förråd) >= 1 and svar >= 1:
            print(
                f"\n{förråd[svar-1].namn}\n{förråd[svar-1].sällsynthet}\n{förråd[svar-1].beskrivning}")
            while säker != "ja" and säker != "nej":
                try:
                    säker = input(
                        f"Är du säker att du vill använda {förråd[svar-1].namn} [ja], [nej] -> ")
                except:
                    print("Ogiltigt svar, svara med ja eller nej")
                    continue
                if säker.upper() != "JA" and säker != "NEJ":
                    print("Ogiltigt svar, svara med ja eller nej")
            if säker.upper() == "JA":
                if förråd[svar-1].slump_lägre == None:
                    hp = hp + förråd[svar-1].hp_bonus
                    styrka = styrka + förråd[svar-1].styrka_bonus
                    print(
                        f"Din styrka ökade med {förråd[svar-1].styrka_bonus} och ditt hp med {förråd[svar-1].hp_bonus}")
                else:
                    slumptal = rand.randint(
                        förråd[svar-1].slump_lägre, förråd[svar-1].slump_högre)
                    hp = hp + slumptal
                    styrka = styrka + förråd[svar-1].styrka_bonus
                    if slumptal >= 0:
                        print(
                            f"\nDin styrka ökade med {förråd[svar-1].styrka_bonus} och ditt hp med {slumptal}")
                    else:
                        print(
                            f"\nDin styrka ökade med {förråd[svar-1].styrka_bonus} men ditt hp gick ned med {slumptal}")
                if hp >= max_hp:
                    print("Du nådde max hp, levla upp för att öka max hp")
                    hp = max_hp
                förråd.remove(förråd[svar-1])
                return hp, styrka
            else:
                print("Stänger förråd")
                return hp, styrka
        else:
            print(f"\nHittade inte ett föremål vid position {svar}")

# Den här funktionen kontrollerar dörrarna och bestämmer vad som ska vara bakom varje dörr


def kolla_dörr(svar, list):
    if list[svar-1] < 2:
        return "föremål"
    elif list[svar-1] > 1 and list[svar-1] < 5:
        return "fiende"
    elif list[svar-1] > 4:
        return "trap"


# Den här funktionen slumpar fram ett föremål från en random sällsynthet. Den kollar också om ditt förråd är fullt och om det är fallet frågar den om du vill byta ut föremålet mot ett annat i ditt förråd
def välj_och_lägg_till_föremål(slumptal, övre_gräns, lägre_gräns, sällsynthet_övre_gräns, sällsynthet_lägre_gräns, förråd):
    svar = ""
    alla_föremål = [mjölk, äppelskrutt, ägg, bröd, köttbullar, vattenflaska, taco_buffe,
                    skolmat, vodka, kräftor, fugu, oboy, svart_vattenmelon, wagyu_beef]
    if slumptal <= övre_gräns and slumptal > lägre_gräns:
        slumptal = rand.randint(sällsynthet_lägre_gräns,
                                sällsynthet_övre_gräns)
        print(
            f"\n{alla_föremål[slumptal].sällsynthet}\nDu hittade {alla_föremål[slumptal].namn}")
        if len(förråd) < 5:
            print(f"{alla_föremål[slumptal].namn} lades till i ditt förråd")
            förråd.append(alla_föremål[slumptal])
        else:
            while svar.upper() != "JA" and svar.upper() != "NEJ":
                try:
                    svar = input(
                        f"\nDitt förråd är fullt\nVill du byta ut {alla_föremål[slumptal].namn} mot ett annat föremål i ditt förråd [ja] eller [nej] -> ")
                except:
                    print("Ogiltigt svar, svara med ja eller nej")
                    continue
                if svar.upper() != "JA" and svar.upper() != "NEJ":
                    print("Ogiltigt svar, svara med ja eller nej")
            if svar.upper() == "JA":
                svar = 10
                while svar > len(förråd) or svar < 1:
                    for x, i in enumerate(förråd):
                        print(f"[{x+1}] {i.namn}")
                    try:
                        svar = int(input(
                            "Vilket föremål vill du byta ut? Välj genom föremålets position 1,2,3... -> "))
                    except:
                        print("\nOgiltigt svar, svaret måste vara ett heltal")
                        continue
                    if svar <= len(förråd) and svar >= 1:
                        print(
                            f"Du kastade iväg {förråd[svar-1].namn} och bytte ut det mot {alla_föremål[slumptal].namn}")
                        förråd.pop(svar-1)
                        förråd.append(alla_föremål[slumptal])
                    else:
                        print(
                            f"\nHittade inte ett föremål vid position {svar}")


def öppna_dörr(hp, styrka, förråd, lvl, max_hp, vinst):
    dörrar = []
    svar = "placeholder"
    for i in range(3):
        dörrar.append(rand.randint(1, 5))
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
        bakom_dörr = kolla_dörr(svar, dörrar)
    elif svar == 2:
        bakom_dörr = kolla_dörr(svar, dörrar)
    elif svar == 3:
        bakom_dörr = kolla_dörr(svar, dörrar)
    svar = ""
    if bakom_dörr == "föremål":
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
            välj_och_lägg_till_föremål(slumptal, 60, 0, 5, 0, förråd)
            välj_och_lägg_till_föremål(slumptal, 90, 60, 10, 6, förråd)
            välj_och_lägg_till_föremål(slumptal, 100, 90, 13, 11, förråd)
        elif svar.upper() == "NEJ":
            print("Du lämmnade kistan oöppnad")
    elif bakom_dörr == "trap":
        fällorna = [hjulfällan, ju_större_de_är,
                    fortnite_spik_fälla, clashroyale_fälla, snurrande_klingan, första_steget_fällan, dubbeldörrens_dom, dödskikaren, gubben_i_lådan, satans_båge, bowling, bomerang_kniv_domedagshandsken, gammal_mantel, hoppa_hage, dammsugar_fällan]
        slumptal = rand.randint(0, (len(fällorna)-1))
        print(f"\n{fällorna[slumptal].beskrivning}")
        svar = ""
        while svar != 1 and svar != 2 and svar != 3 and svar != 4:
            try:
                svar = int(
                    input(f"\nVad gör du? {fällorna[slumptal].val} -> "))
            except:
                print("Ogiltigt svar, svara med [1], [2], [3] eller [4]")
                continue
            if svar != 1 and svar != 2 and svar != 3 and svar != 4:
                print("Ogiltigt svar, svara med [1], [2], [3] eller [4]")
        if svar == 1:
            print(f"\n{fällorna[slumptal].slut1}")
        elif svar == 2:
            print(f"\n{fällorna[slumptal].slut2}")
        elif svar == 3:
            print(f"\n{fällorna[slumptal].slut3}")
        elif svar == 4:
            print(f"\n{fällorna[slumptal].slut4}")
        if fällorna[slumptal].lösning[svar-1] == "W":
            hp = hp - fällorna[slumptal].hp_förlust
            print(f"Du förlorade {fällorna[slumptal].hp_förlust} hp")
    elif bakom_dörr == "fiende":
        giltiga_fiender = []
        fiender = [zombie, lost_soul, sandworm, mike_wazowski, wolf_spider,
                   mega_knight, troll, werewolf, vampire, the_devil, emerald_dragon, final_boss]
        for i in fiender:
            if lvl <= i.max_lvl and lvl >= i.min_lvl:
                giltiga_fiender.append(i)
        slumptal = rand.randint(0, (len(giltiga_fiender)-1))
        while svar.upper() != "JA" and svar.upper() != "NEJ":
            try:
                svar = input(
                    f"Du stötte på {giltiga_fiender[slumptal].namn}, vill du slåss? [ja] eller [nej] -> ")
            except:
                print("Ogiltigt svar, svara med ja eller nej")
                continue
            if svar.upper() != "JA" and svar.upper() != "NEJ":
                print("Ogiltigt svar, svara med ja eller nej")
        if svar.upper() == "JA":
            if styrka > giltiga_fiender[slumptal].styrka:
                if giltiga_fiender[slumptal].namn == "Typhon":
                    print("\nModiga kämpe du räddade denna alternativa värld och kommer gå genom historierna som en legend. Vi längtar till nästa gång vi möts")
                    vinst = True
                else:
                    print(
                        f"\nDu vann och levlade upp till {lvl+1}! Ditt max hp ökade till {max_hp + 1}, ditt hp gick upp med 1.")
                    lvl += 1
                    max_hp += 1
                    hp += 1
            elif styrka < giltiga_fiender[slumptal].styrka:
                print("\nDu förlorade, du tog 1 skada!")
                hp -= 1
            elif styrka == giltiga_fiender[slumptal].styrka:
                print(
                    "\nDet blev lika, ni skakade hand och called it a day")
        elif svar.upper() == "NEJ":
            spring = rand.randint(0, 10)
            if spring <= 3:
                print(
                    f"Du lyckades springa iväg från faran eftersom Ians fortnite dans skrämde livet ur {giltiga_fiender[slumptal].namn} som kommer vara ärrad för livet")
            else:
                print(
                    f"Du sprang för ditt liv men blev distraherad av Rubens fortnite dans och {giltiga_fiender[slumptal].namn} lyckades komma i kapp och du förlorade 1 hp")
                hp -= 1
    return hp, lvl, max_hp, vinst

# Huvudprogrammet som definerar några variablar och kallar på olika funktioner


def main():
    vinst = False
    hp = 5
    max_hp = 5
    styrka = 3
    lvl = 1
    förråd = []
    while hp > 0 and vinst == False:
        try:
            svar = input(
                "\nVad vill du göra, visa stats [s], visa förråd [i], välja dörr [d], avsluta programmet [quit] -> ")
        except:
            print("Ogiltigt svar, svara med [s], [i] eller [d]")
        if svar.upper() == "S":
            print(f"Du har {hp} hp, {styrka} styrka och är level {lvl}")
        elif svar.upper() == "I":
            if len(förråd) > 0:
                hp, styrka = visa_förråd(hp, styrka, max_hp, förråd)
            else:
                print("Ditt förråd är tomt")
        elif svar.upper() == "D":
            hp, lvl, max_hp, vinst = öppna_dörr(
                hp, styrka, förråd, lvl, max_hp, vinst)
        elif svar.upper() == "QUIT":
            hp = 0
        else:
            print("Ogiltigt svar, svara med [s], [i] eller [d]")
    if hp == 0:
        print("GAME OVER")


main()
