import random
#### 
#            A B C D E F G H I J
spelplan = [['0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0']]

## Listor
kolumner = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
rader = ["1","2","3","4","5","6","7","8","9","10"]
riktning = ["H", "V"]
tagnaRutor = []
tagnaRutorCPU = []
ordning = ["första", "andra", "tredje", "fjärde", "femte"]
skepp = [5,4,3,3,2]

## Skapa alla rutor
#def skapaRutor(listor):
rutor = []
for j in range(10):
    for i in range(10):
        rutor.append(kolumner[i]+rader[j])

listor = kolumner, rader, riktning, ordning, skepp, tagnaRutor, spelplan, rutor


## Skriv ut instruktioner
print("Spelplanen ser ut så här:\n     A    B    C    D    E    F    G    H    I    J")
j = 1
for i in spelplan:
    if j < 10:
        print(str(j)+" ",i)
    else:
        print(j,i)
    j+=1
    
print("""\nDu placerar dina skepp genom att skriva
placeringen du vill att det ska börja på, samt
om du vill ha det horisontellt eller vertikalt.
Skeppet "växer" åt höger vid horisontell placering
och nedåt vid vertikal placering.

Exempel: E4V placerar skeppet på kolumn E, och raderna 4-8.\n""")


def godkandPlacering(listor):
    rutor = []
    for j in range(10):
        for i in range(10):
            rutor.append(kolumner[i]+rader[j])
    counter = 0
    for i in range(5): # Kör slingan fem gånger för fem skepp
        kontroll = False
        while kontroll != True:
            placering = ""
            placering = input("Placera nu ut ditt " + ordning[i] + " skepp med längden " + str(skepp[i]) + ":\n").upper()
            ## Felkontroll
            while placering[:-1] not in rutor or placering[-1] not in riktning or len(placering)==0:
                while len(placering)==0:
                    placering = input("Du måste skriva någonting! Välj en ruta:\n").upper()
                if placering[:-1] in tagnaRutor:
                    placering = input("Du har redan använt den/de rutorna! Välj en annan:\n").upper()
                elif placering[-1] not in riktning:
                    placering = input("Du har angivit en felaktig riktning! Välj en annan:\n").upper()
                else:
                    placering = input("Du har angivit en felaktig ruta. Använd formatet A1H.\nFörsök igen: ").upper()
            kontroll = placeraSkepp(listor, placering, skepp[i], rutor)
        ritaSpelplan(listor, placering[-1], skepp[i], counter) # Rita ut spelplanen
        counter = len(tagnaRutor)
        print("Spelplanen ser nu ut så här:\n     A    B    C    D    E    F    G    H    I    J")
        j = 1
        for i in spelplan:
            if j < 10:
                print(str(j)+" ",i)
            else:
                print(j,i)
            j+=1


def placeraSkepp(listor, placering, langd, rutor):
    a = tagnaRutor.append
    r = rutor.remove
    if placering[-1] == "H":
        try:
            kolumner[kolumner.index(placering[0])+(langd-1)] # Räkna ut var skeppet slutar, ger fel om skepp är utanför kolumner
            k = kolumner.index(placering[0]) # Hämta vilken kolumn skeppet startar på
            for s in range(langd):
                try:
                    rutor.index(kolumner[k+s]+placering[1:-1]) # Se om skeppet kommer överlappa ett annat skepp
                except ValueError:
                    print("Skeppet går inte att placera där, du har redan ett skepp som täcker en eller flera av rutorna.\nFörsök igen!\n")
                    return False
                    break
            for j in range(langd):
                a(str(kolumner[k+j]+placering[1:-1])) # Lägg till nästa ruta i tagnaRutor
                r(str(kolumner[k+j]+placering[1:-1])) # Ta bort använda rutor från rutor
            return True
        except IndexError:
            print("Skeppet kan inte sträcka sig utanför spelplanen, försök igen!\n")
            return False
    if placering[-1] == "V":
        try:
            rader[rader.index(placering[1:-1])+(langd-1)] # Räkna ut var skeppet slutar, ger fel om skepp är utanför rader
            k = rader.index(placering[1:-1]) # Hämta vilken rad skeppet startar på
            for s in range(langd):
                try:
                    rutor.index(placering[0]+rader[k+s]) # Se om skeppet kommer överlappa ett annat skepp
                except ValueError:
                    print("Skeppet går inte att placera där, du har redan ett skepp som täcker en eller flera av rutorna\nFörsök igen!\n")
                    return False
                    break
            for j in range(langd):
                a(str(placering[0]+rader[k+j])) # Lägg till nästa ruta i tagnaRutor
                r(str(placering[0]+rader[k+j])) # Ta bort använda rutor från rutor
            return True
        except IndexError:
            print("Skeppet kan inte sträcka sig utanför spelplanen, försök igen!\n")
            return False

def ritaSpelplan(listor, riktn, langd, counter):
    for i in range(langd):
        k = tagnaRutor[counter]
        if riktn == "H":
            spelplan[rader.index(k[1:])][kolumner.index(k[0])+i] = "#" # Byt ut n0llan till '#'
        if riktn == "V":
            spelplan[rader.index(k[1:])+i][kolumner.index(k[0])] = "#" # Byt ut n0llan till '#'
    return spelplan, counter
        

def gissning(listor):
    skott = input("Vilken ruta vill du skjuta på?\n")
    if skott in TagnaRutorCPU:
        print("Träff! ")
        del TagnaRutorCPU[tagnaRutor.index(skott)]
        

def valCPU(listor):
    rutor = []
    for j in range(10):
        for i in range(10):
            rutor.append(kolumner[i]+rader[j])
    for i in skepp:
        kontroll = False
        while kontroll != True:
            randRikt = random.choice(riktning)
            placeringCPU = random.choice(rutor)
            kontroll = False
            while placeringCPU in tagnaRutorCPU:
                randRikt = random.choice(riktning)
                placeringCPU = random.choice(rutor) 
            placeringCPU += randRikt
            kontroll = placeraSkeppCPU(listor, placeringCPU, i)
    print(tagnaRutorCPU)
            

def placeraSkeppCPU(listor, placeringCPU, i):
    add = tagnaRutorCPU.append
    rem = rutor.remove
    if placeringCPU[-1] == "H":
        try:
            kolumner[kolumner.index(placeringCPU[0])+(i-1)] # Räkna ut var skeppet slutar, ger fel om skepp är utanför kolumner
            k = kolumner.index(placeringCPU[0]) # Hämta vilken kolumn skeppet startar på
            for s in range(i):
                try:
                    rutor.index(kolumner[k+s]+placeringCPU[1:-1]) # Se om skeppet kommer överlappa ett annat skepp
                except ValueError:
                    return False
                    break
            for j in range(i):
                add(str(kolumner[k+j]+placeringCPU[1:-1])) # Lägg till nästa ruta i tagnaRutor
                rem(str(kolumner[k+j]+placeringCPU[1:-1])) # Ta bort använda rutor från rutor
            return True
        except IndexError:
            return False
    if placeringCPU[-1] == "V":
        try:
            rader[rader.index(placeringCPU[1:-1])+(i-1)] # Räkna ut var skeppet slutar, ger fel om skepp är utanför rader
            k = rader.index(placeringCPU[1:-1]) # Hämta vilken rad skeppet startar på
            for s in range(i):
                try:
                    rutor.index(placeringCPU[0]+rader[k+s]) # Se om skeppet kommer överlappa ett annat skepp
                except ValueError:
                    return False
                    break
            for j in range(i):
                add(str(placeringCPU[0]+rader[k+j])) # Lägg till nästa ruta i tagnaRutor
                rem(str(placeringCPU[0]+rader[k+j])) # Ta bort använda rutor från rutor
            return True
        except IndexError:
            return False

def main():
    valCPU(listor)
    godkandPlacering(listor)

main()
