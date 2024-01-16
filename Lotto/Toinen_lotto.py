
#POHJUSTUS
#YKSI TUNTIHARJOITUS
# Dictionary, jossa avaimena on vk nro 1-52 ja sisältönä arvottu
# (veikkauksen) lottorivi eli 7 luku väliltä 1-40. tuplia ei rivillä sallita
#
# generoidaan aluksi veikkauksen rivit ko viikoille
#
# pyydä käyttäjältä hänen rivinsä ( siis 7 numero väliltä 1-40)
#
# käy läpi veikkauksen rivit ja tulosta miten olisi lykästänyt antamallaan rivillä
# näytä siis viikottainen tulos

import random

rivitviikkoittain = dict()

for vk in range (1,53):
    vkrivi = set()
    while (len(vkrivi) < 7):
        nro = random.randint(1, 40)
        vkrivi.add(nro)
    rivitviikkoittain[vk] = vkrivi

omarivi = set()
while (len(omarivi) < 7):
    arvo = int(input("Anna rivisi numero (1-40): "))
    if arvo < 1 or arvo > 40:
        continue
    if arvo in omarivi:
        print("nro on jo rivillä!!")
    else:
        omarivi.add(arvo)

for viikkonro in rivitviikkoittain:
    print("viikko", viikkonro)
    osumat = omarivi.intersection(rivitviikkoittain[viikkonro])
    print("\tOsmuia oli ",len(osumat), " kpl")
    print("\tja ne olivat ", osumat)













