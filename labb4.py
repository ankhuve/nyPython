def raknaOrd():
    allaOrd = []
    enskildaOrd = []
    inläsning = False
    while inläsning != True:
        try:
            filNamn = input("Ange filnamnet på den text du vill läsa in: ")
            text = open(filNamn, 'r')
            for line in text:
                allaOrd += line.split()
            for i in allaOrd:
                allaOrd[allaOrd.index(i)] = allaOrd[allaOrd.index(i)].lower()
                if i.lower() not in enskildaOrd:
                    enskildaOrd.append(i.lower())
            inläsning = True
        except FileNotFoundError:
            print("Filen du angav finns inte. Försök igen!")
        except IOError:
            print("Filen gick inte att läsa in. Försök igen!")
    print("Orden som lästes in var:\n\n", allaOrd, "\n")
    for i in enskildaOrd:
        print("Antal förekomster av ordet '" + str(i).lower() + "':", allaOrd.count(i))
raknaOrd()
