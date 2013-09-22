def raknaOrd(text):
    global allaOrd
    allaOrd = []
    for line in text:
        words = line.split()
        for i in range(len(words)):
            allaOrd.append(words[i])
    return allaOrd

def main():
    inläsning = False
    while inläsning != True:
        try:
            filNamn = input("Ange filnamnet på den text du vill läsa in: ")
            text = open(filNamn, 'r')
            inläsning = True
        except FileNotFoundError:
            print("Filen du angav finns inte. Försök igen!")
        except IOError:
            print("Filen gick inte att läsa in. Försök igen!")
    print("Orden som lästes in var:\n\n", raknaOrd(text), "\n\nOch det var", len(allaOrd), "ord.")

main()
