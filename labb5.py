class ObjectMaker:
    def __init__(self, word, count):
        self.object = None
        self.word = word
        self.count = count

def readFile():
    read = False
    while read != True:
            try:
                filNamn = input("Ange filnamnet på den text du vill läsa in: ")
                allWords = open(filNamn, 'r')
                read = True
            except FileNotFoundError:
                print("Filen du angav finns inte. Försök igen!")
            except IOError:
                print("Filen gick inte att läsa in. Försök igen!")
    return allWords

def counter(allWords):
    d = {}
    for line in allWords:
        words = line.split()
        for word in words:
            word = word.lower()
            if word in d.keys():
                d[word] += 1
            else:
                d[word] = 1
    return d

def listMaker(d):
    lista = []
    for i in d:
        word = i
        count = d[i]
        x = ObjectMaker(word, count)    # Skapa ett objekt med ordet och antalet gånger det förekommer i texten
        lista.append(x)
    return lista

def sortList(lista):
    return sorted(lista, key=lambda x: x.count, reverse=True)

def printWordCount(li):
    for i in li:
        print("Ordet", i.word, "fanns", i.count, "gånger i texten.")

def printAllWords(allWords):
    print("\nOrden som lästes in var:")
    words = ""
    for word in allWords:
        words += word+", "
    print(words, "\n")
#################################################
def main():
    allWords = readFile() # Läser in textfilen som returneras till allWords
    d = counter(allWords) # Skapar en dictionary med orden och antal gånger de förekommer
    printAllWords(d)      # Skriv ut varje ord i texten en gång
    sorted_list = sortList(listMaker(d))    # Sortera listan med avseende på det andra värdet (siffran) och lägg in i en ny lista
    printWordCount(sorted_list) # Skriv ut den sorterade listan
#################################################
main()
