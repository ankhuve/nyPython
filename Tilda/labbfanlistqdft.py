from bintreeFile import *
from listQfile import *
import sys

class ParentNode:
    """ Klass för nod som har info om förälder. """
    def __init__(self, word, parent = None):
        """Konstruktor. Sätter attributen till värden. Inparameter är ordet och ev förälder. """
        self.word = word
        self.parent = parent

def main():
    """ Huvudprogrammet, innehåller meny och kallar på funktioner för de olika valen. """
    swe = treeFromFileStuff("word3.txt") # Skapar svenskträdet
    used = Bintree() # Skapar träd för använda ord
    q = ListQ() # Skapar en kö
    c = 0 # Kontrollvariabel
    print("Välkommen till labb 4!\n")
    while c != 1:
        start = input("Startord: ")
        if swe.exists(start):
            c = 0 # Andra kontrollen
            while c != 1:
                end = input("Slutord: ")
                if end == start:
                    print("Det var samma ord som du ville börja med, försök igen.")
                elif swe.exists(end):
                    used.put(start)
                    q.put(ParentNode(start))
                    found = False # Variabel för att kontrollera om ordet har hittats
                    while not q.isEmpty():
                        if found == False:
                            k = q.get(-1) # Hämta ord
                            j, found = depth(swe, used, q, end, k)
                        else:
                            print("Det finns en väg till", end)
                            q.hand = [] # Nollställ kön för att bryta loopen
                    if q.isEmpty() and found == False:
                        print("Det fanns ingen lösning, det är ju omöjligt!!!!!1")
                    else:
                        printChain(j, end)
                    c = 1 # Kontrollvariabeln sätts till ett för att avsluta
                else:
                    print("Slutordet var inte ett giltigt ord. Försök igen.")
        else:
            print("Startordet var inte ett giltigt ord. Försök igen.")




def depth(swe, old, q, end, node):
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
            depth(swe, old, q, end, j)
        elif swe.exists(i) and old.exists(i):
            pass
        
    return (None, False)


def printChain(j, end):
    li = []
    makeChain(j, li)
    li.reverse()
    s = ""
    count = 0
    for i in li[:-1]:
        count += 1
        s += i+" -> "
    s += end
    print(s)
    print("Det var", count, "steg.")

def makeChain(j, li):
    li.append(j.word)
    if j.parent:
        makeChain(j.parent, li)

def makeChildren(node):
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

def treeFromFileStuff(filename, p=0):
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
