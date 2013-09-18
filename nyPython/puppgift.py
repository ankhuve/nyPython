#### 
#       A B C D E F G H I J 
rad1 = [0,0,0,0,0,0,0,0,0,0]
rad2 = [0,0,0,0,0,0,0,0,0,0]
rad3 = [0,0,0,0,0,0,0,0,0,0]
rad4 = [0,0,0,0,0,0,0,0,0,0]
rad5 = [0,0,0,0,0,0,0,0,0,0]
rad6 = [0,0,0,0,0,0,0,0,0,0]
rad7 = [0,0,0,0,0,0,0,0,0,0]
rad8 = [0,0,0,0,0,0,0,0,0,0]
rad9 = [0,0,0,0,0,0,0,0,0,0]
rad10 = [0,0,0,0,0,0,0,0,0,0]

kolumner = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
rader = ["1","2","3","4","5","6","7","8","9","10"]
riktning = ["H", "V"]

## Skapa alla rutor
rutor = []
for j in range(10):
    for i in range(10):
        rutor.insert(i, kolumner[i]+rader[j])

## Skriv ut instruktioner
print("Spelplanen ser ut så här:\n\n    A  B  C  D  E  F  G  H  I  J\n1 ", rad1, "\n2 ", rad2, "\n3 ",
      rad3, "\n4 ", rad4, "\n5 ", rad5, "\n6 ", rad6, "\n7 ",
      rad7, "\n8 ", rad8, "\n9 ", rad9, "\n10", rad10, "\n")
print("""Du placerar dina skepp genom att skriva
placeringen du vill att det ska börja på, samt
om du vill ha det horisontellt eller vertikalt.
Skeppet "växer" åt höger vid horisontell placering
och nedåt vid vertikal placering.

Exempel: E4H placerar skeppet på kolumn E, och raderna 4-8.\n""")
tagnaRutor = []

def godkandPlacering(kolumner, rader, rutor, riktning, tagnaRutor):
    lista = ["första", "andra", "tredje", "fjärde", "femte"]
    skepp = ["1","2","3","4","5"]
    for i in range(5):
        placering = ""
        placering = input("Placera nu ut ditt " + lista[i] + " skepp med längden " + skepp[i] + ":\n").upper()
        while placering[:-1] not in rutor and placering[-1] not in riktning or len(placering)<3:
            #felKontroll(placering, kolumner, rader, riktning, tagnaRutor, rutor, position)
            #while placering not in rutor:
            if placering[:-1] in tagnaRutor:
                placering = input("Du har redan använt den/de rutorna! Välj en annan:\n").upper()
            elif placering[-1] not in riktning:
                placering = input("Du har angivit en felaktig riktning! Välj en annan:\n").upper()
            else:
                placering = input("Du har angivit en felaktig ruta. Använd formatet A1H.\nFörsök igen: ").upper()
        tagnaRutor.insert(i, placering)
        i += 1

##def felKontroll(placering, kolumner, rader, riktning, tagnaRutor, rutor, position):
##    placering = placering.upper()
##    while placering[:-1] not in rutor and placering[-1] not in riktning:
##        placering = input("Du har angivit en felaktig ruta, den kanske är upptagen eller så har du skrivit fel. Använd ex. A1H.\nFörsök igen: ")
##        placering = placering.upper()
##        #else:
##        #    placering = input("Du har angivit en felaktig ruta, den kanske är upptagen eller så har du skrivit fel. Använd ex. A1H.\nFörsök igen: ")
##    return placering
##        #if placering[-1] not in riktning:
##        #    placering = input("Du har angivit en felaktig riktning. \nFörsök igen: ")
##        #elif placering not in rutor:
##        #    placering = input("Du har angivit en felaktig ruta, den kanske är upptagen eller så har du skrivit fel. Använd ex. A1H.\nFörsök igen: ")
##        #else:
##        #    position = True

##def placeraSkepp(placering, kolumner, rader):
##    for i in placering:
##        1+1
    
godkandPlacering(kolumner, rader, rutor, riktning, tagnaRutor)



