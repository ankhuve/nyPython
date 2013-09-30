
def readFile():
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
    return text
            
def splitText(text):
    li = []
    for line in text:
        li += line.split()
    for i in li:
        li[li.index(i)] = li[li.index(i)].lower()
    print("\nOrden som lästes in från texten var:\n", li, "\n")
    return li

def wordCounter(text):
    d = {}
    allaOrden = splitText(text)
    for word in allaOrden:
        if word in d.keys():
            d[word] += 1
        else:
            d[word] = 1
    return d

def main():
    text = readFile()
    d = wordCounter(text)
    for word in d:
        print("Ordet", word, "fanns",  d[word], "gånger i texten.")

main()
