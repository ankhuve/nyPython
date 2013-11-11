import random
color = ["H", "S", "K", "R"]
nr = ['A','2','3','4','5','6','7','8','9','T','J','D','K']
deck = []
for i in nr:
    for n in color:
        deck.append(n+i)

spelplan=[]
for i in range(13):
    kol = [deck.pop(deck.index(random.choice(deck)))]
    spelplan.append(kol)

print(spelplan)
