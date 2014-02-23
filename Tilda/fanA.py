from bintreeFile import *
from listQfile import *

class ParentNode:
    """ Klass för nod som har info om förälder. """
    def __init__(self, word, parent = None):
        """Konstruktor. Sätter attributen till värden. Inparameter är ordet och ev förälder. """
        self.word = word
        self.parent = parent

def main():
    """ Huvudprogrammet, innehåller meny och kallar på funktioner för de olika valen. """
    swe = treeFromFileStuff("word3.txt") # Skapar svenskträdet
    c = 0 # Kontrollvariabel
    print("Välkommen till labb 4!\nLängsta kortaste vägen yo.\n")
    while c != 1:
        end = input("Slutord: ")
        if swe.exists(end):
            solutions = []
            l = open("word3.txt", "r", encoding = "utf-8")
            for word in l:
                used = Bintree() # Skapar träd för använda ord
                q = ListQ() # Skapar en kö
                used.put(word)
                q.put(ParentNode(word))
                found = False # Variabel för att kontrollera om ordet har hittats
                while not q.isEmpty():
                    if found == False:
                        k = q.get() # Hämta ord
                        j, found = search(swe, used, q, end, k)
                    else:
                        q.hand = [] # Nollställ kön för att bryta loopen
                if q.isEmpty() and found == False:
                    pass
                else:
                    steps = printChain(j)
                    if solutions == []:
                        solutions = [[word.strip()], steps]
                    else:
                        if steps >= solutions[1]:
                            if steps == solutions[1]:
                                solutions[0].append(word.strip())
                            else:
                                solutions[0] = [word.strip()]
                            solutions[1] = steps
                            print("Ord med längst lösning:",solutions[0]," : "+(str(solutions[1])))
            c = 1 # Kontrollvariabeln sätts till ett för att avsluta
        else:
            print("Slutordet var inte ett giltigt ord. Försök igen.")

def search(swe, old, q, end, node):
    """ Kontrollerar om ordet är hittat, om inte så kontrolleras om ordet är korrekt eller använt.
    Inparametrar är svenskträdet, gamlaträdet, kön, generationen barn och slutordet.
    Returnerar noden om det är detsamma som sista ordet, None om annars. Returnerar även True om hittat, False annars."""
    children = makeChildren(node)
    for j in children:
        i = j.word
        if i == end:
            return (j, True)
        elif swe.exists(i) and not old.exists(i):
            old.put(i)
            q.put(j)
        elif swe.exists(i) and old.exists(i):
            pass
    return (None, False)

def printChain(j):
    """Skapar kedjan, returnerar hur många steg det var.
    Inparametrar är slutnoden. """
    li = []
    makeChain(j, li)
    count = 0
    for i in li[:-1]:
        count += 1
    return count

def makeChain(j, li):
    """ Lägger till orden i en lista och kallar på sig själv om det finns en förälder.
    Inparameter är slutnoden och listan. """
    li.append(j.word)
    if j.parent:
        makeChain(j.parent, li)

def makeChildren(node):
    """Skapar nya ord för noden som är inparameter. returnerar sedan en lista med de nya noderna."""
    ALPH = "abcdefghijklmnopqrstuvwxyzåäö"
    children = []
    word = node.word
    for i in range(len(word)):
        for k in ALPH:
            if i == 0:
                new_word = k+word[1:]
            elif i == 1:
                new_word = word[0]+k+word[-1]
            else:
                new_word = word[:2]+k
            children.append(ParentNode(new_word, node))
    return children

def treeFromFileStuff(filename):
    """ Skapar ett träd och utför olika saker beroende på inparametern p. Inparameter är filnamnet på
    textfilen samt eventuell parameter för olika kommandon. Returnerar det nya trädet eller trädet samt lista
    med de inlästa orden. """
    tree = Bintree()
    with open(filename, "r", encoding = "utf-8") as file:
        for l in file:
            word = l.strip()                # Ett trebokstavsord per rad
            tree.put(word)             # in i sökträdet
    print("\n")
    return tree

main()
