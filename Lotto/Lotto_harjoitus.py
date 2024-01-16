

import random

lkm = 0
#LUODAA OIKEA RIVI SATUNNAISISTA NUMEROISTA
oikearivi = set()
while True:
    luku = random.randint(1,40)
    oikearivi.add(luku)
    if (len(oikearivi) == 7):
        break

print("Tämän kerran oikearivi:\n ", oikearivi)

jarjestetty_rivi = list(oikearivi)
jarjestetty_rivi.sort()

print(" ",jarjestetty_rivi)

nrorivi = random.sample(range(1,41),7)

osumat = set(oikearivi).intersection(nrorivi)
if len(osumat) != 0:
    print(" ", osumat)
else:
    print(" ")


#
# kerrat = 0
# while True:
#     nrorivi = random.sample(range(1,41),7)
#     nrorivi.sort()
#     print(" ",nrorivi)
#     kerrat += 1
#
#     osumat = set(oikearivi).intersection(nrorivi)
#     if len(osumat) != 0:
#         print(" ", osumat)
#     else:
#         print(" ")
#
#     if (len(osumat) == 7):
#         print("7 oikein tuli: ", kerrat, " yrityksellä")
#         break

