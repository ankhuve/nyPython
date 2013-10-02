class ListMaker:
    def __init__(self, word, count):
        self.objekt = []
        self.word = word
        self.count = count

    def create_object(self, word, count):
        self.objekt.append(self.word)
        self.objekt.append(self.count)
        return self.objekt

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
    print(d)
    return d

##def listMaker(d):
##    li = []
##    for word in d:
##        li.append(word)
##        li.append(d[word])
##    print(li)
##    return li
##
##def printWords(li):
##    for i in range(0,len(li),2):
##        print("Ordet", li[i], "fanns", li[i+1], "gånger i texten.")

def main():
    allWords = readFile()
    d = counter(allWords)
    for i in d:
        ord = i
        rakn = d[i]
        x = ListMaker(ord, rakn)
        lista = x.create_object(ord, rakn)
    
    
    #li = listMaker(counter(allaOrden))
    #printWords(li)

main()
