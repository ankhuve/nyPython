from bintreeFile import *
from linkedQfile import *
import sys

class ParentNode:
    def __init__(self, word, parent = None):
        self.word = word
        self.parent = parent

def main():
    """ Huvudprogrammet, innehåller meny och kallar på funktioner för de olika valen. """
    swe = treeFromFileStuff("word3.txt") # Skapar svenskträdet om det inte finns
    gamla = Bintree()
    q = LinkedQ()
    c_1 = 0 # Kontrollvariabel
    print("Välkommen till labb 4!\n")
    while c_1 != 1:
        start = input("Startord: ")
        if swe.exists(start):
            c_2 = 0 # Kontrollvariabel
            while c_2 != 1:
                end = input("Slutord: ")
                if swe.exists(end):
                    gamla.put(start)
                    q.put(Node(ParentNode(start)))
                    found = False
                    while not q.isEmpty():
                        if found == False:
                            k = q.get()
                            children = makeChildren(k)
                            j, found = checkThings(swe, gamla, q, children, end)
##                            for j in children:
##                                i = j.value.word
##                                if swe.exists(i) and not gamla.exists(i):
##                                    gamla.put(i)
##                                    q.put(j)
##                                elif i == end:
##                                    found = True
##                                    break
                        else:
                            print("Det finns en väg till", end)
                            q.first = None
                            q.last = None
                    writeChain(j, start)
                    c_1 = 1
                    c_2 = 1
                else:
                    print("Slutordet var inte ett giltigt ord. Försök igen.")
        else:
            print("Startordet var inte ett giltigt ord. Försök igen.")

def checkThings(swe, old, q, children, end):
    for j in children:
        i = j.value.word
        if swe.exists(i) and not old.exists(i):
            old.put(i)
            q.put(j)
        elif i == end:
            return (j, True)
    return (None, False)


def writeChain(j, start):
    while j.value.parent != None:
        print(j.value.word)
        writeChain(j.value.parent, start)
    if j.value.word == start:
        print(j.value.word)
        sys.exit()

def makeChildren(node):
    ALPH = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'å', 'ä', 'ö']
    children = []
    word = node.value.word
    for i in range(len(word)):
        for k in ALPH:
            if i == 0:
                new_word = k+word[1:]
            elif i == 1:
                new_word = word[0]+k+word[-1]
            else:
                new_word = word[:2]+k
            children.append(Node(ParentNode(new_word, node)))
    return children
                


def treeFromFileStuff(filename, p=0):
    """ Skapar ett träd och utför olika saker beroende på inparametern p. Inparameter är filnamnet på
    textfilen samt eventuell parameter för olika kommandon. Returnerar det nya trädet eller trädet samt lista
    med de inlästa orden. """
    tree = Bintree()
    if p==2:
        li = [] # Lista för de inlästa orden.
    with open(filename, "r", encoding = "utf-8") as file:
        for l in file:
            word = l.strip()                # Ett trebokstavsord per rad
            if tree.exists(word) and p==1:
                print(word, end = " ")
            elif isinstance(p, Bintree):
                words = l.split() # Delar upp orden på den inlästa raden.
                for i in words:
                    if tree.exists(i):
                        pass
                    else:
                        tree.put(i)             # in i sökträdet
                        if p.exists(i):
                            print(i, end=" ") # Printar ordet om det finns i båda träden.
            else:
                tree.put(word)             # in i sökträdet
                if p==2:
                    li.append(word)
    print("\n")
    if p==2:
        return tree, li
    else:
        return tree

main()
