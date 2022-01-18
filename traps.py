class Traps:
    def __init__(self, description, val, end1, end2, end3, end4, solution, hp_loss):
        self.description = description
        self.val = val
        self.hp_loss = hp_loss
        self.end1 = end1
        self.end2 = end2
        self.end3 = end3
        self.end4 = end4
        self.solution = solution

hjulfallan = Traps("Du kliver in i ett rum fyllt med tunnor längs väggarna, plötsligt ser du ett hjul komma mot dig samtidigt som du hör en stål dörr stängas bakom dig",
                   "lägg dig ner [1], hoppa???? [2], banka på stålldörren [3], skrik:HJÄÄLP [4]", "Du la dig ner och somnade, hjulet krossade dig i din sömn", "Du hoppade så högt du kunde och lyckades precis komma över hjulet", "Du banka o banka o banka, inget hände, hjulet kom ikapp...", "Du skrek allt vad du hade, men inget svar....", "WCWW", 2)
ju_storre_de_ar = Traps("Du kliver in genom dörren till en naturlig grotta med en massa klippor. Medans du söker igenom grottan börjar marken skaka och ett stenras blokerar ingången. Turligt nog stog du inte under stenarna. Det forsar in vatten in i grottan snabbt börjar fyllas upp, du har ett rep.",
                        "klättra upp för väggen [4], håll andan [2], kasta repet [3], drick upp allt vatten [1]", "Stenen var hal men du lyckades ta greppet och klättrade undan", "Du hade för små lungor, du drunknade", "Repet fäste sig i en sten i taket, stenen föll ned med repet och landa på din skalle", "Du blev vattenförgiftad och förlorade förmågan att simma, du drunknade", "CWWW", 3)
fortnite_spike_trap = Traps("Du kommer fram till ett rum som lyses upp, du tittar framför dig och ser en forre spike trap på taket framför dig, dörren stängs bakom dig...", "Försök att krypa längs med marken för att undvika fällan [1], bygg ett forre tak på fällan [2], aktivera fällan och försök att springa förbi medan den resettar [3], ta sönder fällan med en fortnite legendary scar [4]",
                            "Du lade dig ner på marken och började krypa, men forre fällan aktiverades och du blev träffad", "Du byggde ett forre tak ovanpå fällan, fällans rörelsedetektorer såg inte dig och du kom förbi", "du kastade en sten under fällan och den aktiverades, sedan sprang du förbi utan att bli träffad men du såg dig inte för och halkade", "Du tog sönder fällan med en legendary scar", "WCWC", 2)
clashroyale_trap = Traps(
    "Du förs in i ett litet rum med ett bord i mitten av rummet, på bordet ligger det en telefon med en clash royale match som startar...", "Använd Theos deck [1], Försök att lämna matchen [2], Använd ditt egna deck [3], Spela inte matchen [4]", "Du använde Theos deck och satte ut prince level 14 som lätt vann, sedan öppnades en hemlig dörr och du gick vidare", "Du klickar på hemknappen för att försöka gå ur spelet, men när du trycker på knappen så får du en stöt av telefonen", "Du använde ditt egna deck och förlorade stort, du tänker att du skulle valt Theos deck och sedan börjar telefon brinna", "Du rör inte telefonen och låter matchen spelas ut av sig själv, du hör ett ljud och ser sedan hur golvet försvinner under dig", "CWWW", 1)
snurrande_klingan = Traps("Det enda som syns är stenväggar, du fortsätter framåt ontanande när du hör ett klick.", "Fortsätt som vanligt [1], Lägg dig ner på marken [2], Hoppa uppåt [3], Sätt dig ner och spela patiens [4]", "En snurrande klinga flyger upp från marken och strimlar din vad",
                          "En snurrande klinga flyger upp från marken och sätter sig i din rygg", "En snurrande klinga flyger upp från marken och kapar dina fötter, du ligger skrikande på marken och förblöder", "En snurrande klinga flyger upp från marken 2 millimeter från ditt huvud och på något sätt klarar du dig oskadd", "WWWC",
                          1)
forsta_steget_fallan = Traps("Rummet lyser upp blått när du öppnar dörrarna du märker snabbt att väggarna är gjorda ut av en sällsynt bergart vid namn Larimar.", "Slå sönder väggarna för att få med dig lite av den dyra stenen [1], Använd detta tillfälle för att vila [2], Gå runt i rummet för att hitta perfekta ljuset för en selfie [3], Undersök väggarna efter fällor eller lönndörr [4]", "Medans du är upptagen med att slå sönder väggarna trampar du på en tryckplatta som får en träplatta att glida undan och en rad sylvassa knivblad svänger upp och skär sönder din ena vad och häl",
                             "När du lägger dig ner stöter du till en tryckplatta men ingenting verkar hända på ett tag, du väljer att fortsätta vila i ett tag till", "Medans du letar efter ett ljus från gud då det är det enda som skulle kunna rädda den bilden, trampar du på en tryckplatta som får en träplatta att glida undan och en rad sylvassa knivblad flyger upp och skär sönder din ena vad och häl", "Nu vet du i alla fall att det fanns varken fälla eller lönndörr i väggarna, men däremot finns det i golvet och du råkar trampar du på en tryckplatta som får en träplatta att glida undan och en rad sylvassa knivblad flyger upp och skär sönder din ena vad och häl", "WCWW", 2)
dubbeldorrens_dom = Traps("Du rycker i dörren men den är låst.", "Sparka ner dörren [1], Slå in dörren [2], Head bumpa dörren [3], Tackla dörren med axeln [4]", "Det är en kostig design på dörren och du flyger igenom men ditt andra ben fanns inte mer",
                          "Du försöker att slå in dörren men den vill inte öppnas, tillslut tittar du närmare vid handtaget och ser att det står \"PULL NOT PUSH\", du drar i dörrhandtaget och dörren öppnas. ", "Osäker på vad du tänkte när du valde detta alternativ men som du antagligen kan gissa så finns du inge mer", "Du borde fundera över att byta karriär till amerikansk spelare, för du är inge vidare som äventyrare", "WCWW", 1)
dodskikaren = Traps("Du öppnar den breda dörren och kliver in ett iskallt rum med glas splitter utspritt över hela golvet och den okända lukten slår emot dig som en vägg, men när du kliver in en liten bit till i rummet märker du något intressant i mitten av rummet. Det är en kikare", "Kolla genom kikaren [1], Inspektera kikaren för fällor [2], Slå sönder kikaren [3], Kolla igenom rummet [4]", "När du kollar genom kikaren märker du att det är någonting på väggen och när du vrider på kikaren för att få bättre skärpa, skjuts en kniv ut in i ditt öga",
                    "Du inspekterar kikaren och hittar ett flertal hemliga dödsfällor i kikaren. Du är glad att du var varsam och hittar tillslut en hemlig utväg ur rummet", "Kylan hade försvagat stålet och den var oväntat otålig och när du slog med all din kraft ramlade du framåt och landade på marken och förblödde", "När du kollar igenom rummet märker du något intressant, det är något ingraverat i väggen men det är för smått för att se med blåtta ögat. Då kommer du på kikaren, du hämtar den och när du kollar i den ser du att det är en karta när plötsligt det skjuts ut en kniv från inuti kikaren som träffar dig i ögat", "WCWW", 1)
gubben_i_ladan = Traps("Du öppnar dörren till ett rum så ljust att du tror att du kommer bränna bort dina ögon. När dina ögon äntligen har vant sig ser du gubben i lådan mitt i rummet.", "Veva fram gubben i lådan [1], Öppna luckan och dra ut gubben i lådan [2], Inspektera lådan [3], Sätt dig och vänta [4]", "När gubben i lådan äntligen hoppar fram så är det inte gubben i lådan utan en metall handske som flygger upp i ditt ansikte",
                       "Du bryter upp lådan och till din överaskning så är det faktiskt gubben i lådan, och när du sliter upp den går det BOOM", "Du förberder dig för det värsta medans du kontrollerar lådan. När du är klar har till din förvåning ingenting hänt och du släpper ner guarden. Plötslig hoppar gubben i lådan fram och du svimmar, men du klarar dig oskadd.", "Du sitter i ensamheten i flera timmar när plötsligt hoppar gubben i lådan fram och ger dig en hjärtattack", "WWCW", 1)
satans_bage = Traps("Väggar som avger något som skulle kunna förklaras som svart lysande är gjorde av obsidian vilket är rätt passande eftersom Satans båge är nu framför dig. Legenden säger att den som kan spänna bågen ska få en önskan uppfylld av djävulen själv.", "Försöker spänna bågen [1], Kontrollera bågen för att se varför den är så svår att spänna [2], Ställ dig på bågen och dra i linan [3], Ställ dig på linan och ta bågen på axlarna och sträck på benen (squat) [4]", "När du spänner bågen skär linan som verkar ha ett litet diamant lager som skär av dina fingrar",
                    "När du kontrollerar bågen märker du att den är gjord av kolstål och därmed omöjligt att böja. Du ger upp och konstigt nog kommer inte Jävulen och dödar dig", "När du spänner bågen skär linan som verkar ha ett litet diamant lager som skär av dina fingrar, vilket var rätt åt dig för att ha försökt att fuska", "Så den negativa saken är att när du trycker uppåt skär den diamant täkta linan av dinna hälar inklusive dinna skinkor, det positiva är att du är redo för julen", "WCWW", 2)
bowling = Traps("En möjligthet för en livstid har uppenbarat sig. Det är en bowlingbana framför dig om du får ner alla kägglor på två kast får du 5 liv (om din max-hp tillåter) och 3 strenght.", "Kasta bowlingklotet på vänster sida av banan [1], Kasta bowlingklotet på höger av banan [2], Kasta bowlingklotet i mitten av banan [3], Gör en Kobe [4]", "Du kastar ner bowlingklotet i rännan, nu är det bara att hoppas på en strike. När su ska kasta igen sätter du inn fingrarna i hål med förgiftade spikar och din hand fräts bort",
                "Så nära! Du kastade för hårt och kägglorna längst ut på båda sidor står fortfarande kvar. När du ska kasta ditt andra kast har bowlingklotet nu förgiftade spikar i hålen och när du stoppar ner handen och kastar blir du förlamad och klotet flyger upp i luften och träffar dig på foten som krossas", "Ett pinsamt kasst som på något sätt endast får ner kägglan längst fram. Klotet du får tillbaka har nu förgiftade spikar i hålen och när du stoppar ner handen ramlar alla dina kroppsdelar (som inte riktigt sitter på kroppen som bland annat tår och fingrar) av", "Pågrund av klotets tyngd åkte den rakt igenom golvet när den landa och ingenting hände", "WWWC", 1)
bomerang_kniv_domedagshandsken = Traps("Du kliver in i ett rum med en stor skylt inuti. Välj en utav de två valen och klara utmaningen som den medför. Framför dig är en underligt formad kniv (med utmaningen att träffa mitt i prick på en måltavla), den andra saken är en medeltids stridshandske (med utmaningen att slå sönder en stenbumling).",
                                       "Välj kniven och kasta den mot måltavlan [1], Välj kniven och slå den mot måltavlan [2], Välj stridshandsken och sätt på dig den. Slå sedan mad all kraft du har mot stenblocket [3], Välj stridshandsken, men istället för att sätta på dig den prövar du att slå med dina bara nävar [4]", "Den ovanliga formen på kniven påminner om en bomerang och när du kastar den kommer den flygande tillbaka in i ditt ansikte", "Handtaget sitter löst och när du slår mot måltavlan som bara råkar vara gjord av sten lossnar knivbladet och flyger upp i ditt ansikte", "Handsken har ett extra lager mellan metallen som är fylld med syra och när du slår stenbumlingen går glaslagret sönder och dn hand fräts bort", "Du slår med sådan kraft att stenbumlingen krossas precis som din näve", "WWWW", 2)
gammal_mantel = Traps("Det enda synliga i rummet är ett förmultnat lik med en gyllene mantel.", "Söker igenom liket efter döds orsak [1], Sätt på dig manteln och se dess effekt [2], Sätt på dig manteln och gör en fortnite dans [3], Strunta i manteln och liket och gå tillbaka genom dörren du kom från [4]", "Medans du sökte igenom liket förlorade du energi och somnade, när du tillslut vaknade var du över 80 år",
                      "Manteln var en gammal artefakt som tog liv från den som bar den, du blev gammal innan du han ta av den", "Fortnite dansen gjorde så att du inte märkte att du blev äldre och du åldrades till en ålder som inte borde kunna nås av en människa", "Till din överraskning hände ingenting och du klarade dig undan från fällan", "WWWC", 2)
hoppa_hage = Traps("Du kommer in till ett hinder, framför dig är ett 4 meter långt och 3 meter djupt hål.", "Hoppa över hålet till andra sidan [1], Hoppa ner i hålet och klättra upp på andra sidan [2], Styla och gör en framåtvållt över hålet [3], Ta sats för att hoppa över hålet [4]", "Du hoppar över men när du ska landa på andra sidan slår du in i en osynlig vägg och du ramlar ner i hålet som har en botten gjord utav en bräcklig spegel som du flyger igenom och möts av en massa enorma spikar",
                   "När du hoppar ner i hålet går spegeln som hålets botten är gjord av och du ramlar ner i ett par enorma spikar", "Du kommer inte tillreckligt långt och slår i huvudet mot kanten", "du tar sats och hoppar med all din kraft över hålet. Du flyger framåt så snabbt att den magiska väggen på andra sidan inte påverkar dig", "WWWC", 3)
dammsugar_fallan = Traps("Det är det mest underligaste rum du någonsin har sett, golvet glimrande pågrund av alla skatter, åh andra sidan väggarna har en matt orange ton med ett klot som lyser upp rummet. Medans du badar i guldet som en kung stängs dörren tyst bakom dig omöjlig att hitta igen och taket som hade varit svårt att se pågrund av belysningen rör sig uppåt vilket medför att lufttrycket ändras och luften tunnas ut. Efter några minuter känner du dig svimfärdig.",
                         "Letar efter utgången [1], Struntar i det och avsluta ditt liv som en rik person [2], Slå på väggarna och be om hjälp [3], Be till gudarna om något att andas [4]", "Du letar och letar men utgången är som bortflugen och tiden flyger iväg precis som ditt sista andetag", "Precis innan du ska somna in för evigt märker du att guldet endast är choklad invirad i guldfärgat godispapper och du dör olycklig, ensam och såklart som fattig igen", "En barmhärtig själ tyckte synd om dig och öppnade dörren", "Någon kände sig snäll nog att uppfylla din sista önskning och fyllde rummet med kolmonoxid, som binder till de röda blodkropparna 250 gånger starkare än vad syre gör, vilket gör att blodkropparnas förmåga att transportera syre försämras kraftigt. Detta gör att en hög exponering snabbt kan leda till kvävning även om man andas in ren luft efteråt. Och bara för att strö salt på såret öppnas dörren medans du långsamt kvävs, trots syren som nu finns i rummet", "WWCW", 3)