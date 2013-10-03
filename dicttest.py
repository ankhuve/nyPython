class ObjectMaker:
    def __init__(self, word, count):
        self.object = None
        self.word = word
        self.count = count

    def create_object(self, word, count):
        self.object = word, count
        return self.object

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
        x = ObjectMaker(word, count)
        lista.append(x.create_object(word, count))
    return lista

def sortList(lista):
    return sorted(lista, key=lambda x: x[1], reverse=True)

def printWords(li):
    for i in li:
        print("Ordet", i[0], "fanns", i[1], "gånger i texten.")
#################################################
def main():
    allWords = readFile()
    d = counter(allWords)
    sorted_list = sortList(listMaker(d))
    printWords(sorted_list)
#################################################
main()
