import random

cardfaces=[]
trap=["naval mine","smokescreen","sabotage"]
perk=["flak armor","far sight","aluminium hull"]
offense=["FMJ upgrade","Rifling","Advanced Rifling","EMP upgrade"]
defensive=["Reinforced hull","Sonar"]
help=["Backup","Extra fuel","Extra fuel 2","Rally","Adrinaline Rush",]
special=["Repair","Hack intel","Jack sparrow"]
deck=[]
for i in range(4):
    cardfaces.append(help[i]+" (help card)")

for h in range(4):
    cardfaces.append(offense[h]+" (offense card)")

for q in range(2):
    cardfaces.append(defensive[q]+" (defensive card)")

for a in range(3):
    cardfaces.append(special[a]+" (special card)")

for j in range(3):
    cardfaces.append(perk[j]+ " (Special perk card)")

for k in range(3):
    if trap=="naval mine":
        cardfaces.append(trap[k]+" offensive trap card")
    elif trap=="smokescreen" or "sabotage":
        cardfaces.append(trap[k]+" (Defensive trap card)")
    else:
        cardfaces.append(trap[k]+" (trap card)")



#print(cardfaces)


for l in range(19):
    card =(cardfaces[l])
    deck.append(card)


random.shuffle(deck)

for m in range(19):
    print(deck[m])
