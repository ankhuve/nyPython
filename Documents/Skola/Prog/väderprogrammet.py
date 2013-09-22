# väderprogrammet

nederbord=[]

def inmatning(nederbord):
    for i in range(12):
        siffra = input("ange för mån " + str(i+1) + " nederbörden:")
        nederbord.append(siffra)

def statistik(nederbord):
    for i in (nederbord):
        totalnederbord = 0
        totalnederbord += int(i)
    medelvärde = totalnederbord/12
    print("medelvärde under året: ", medelvärde)
    print("minimala nederbörden under en månad är:", min(nederbord))
    print("minimala nederbörden under en månad är:", max(nederbord))


val = None
while val != "3":
    print("Hej och välkommen till väderprogrammet")
    val = input("Ditt val:" )
    if val == "1":
        inmatning(nederbord)

    elif val == "2":
        if nederbord == []:
            print ("du har ej fyllt i nummer 1")
        else:
            statistik(nederbord)
        break
