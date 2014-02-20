from bintreeFile import *
from listQfile import *
import sys

class ParentNode:
    def __init__(self, word, parent = None):
        self.word = word
        self.parent = parent

def main():
    """ Huvudprogrammet, innehåller meny och kallar på funktioner för de olika valen. """
    swe = treeFromFileStuff("word3.txt") # Skapar svenskträdet om det inte finns
    used = Bintree()
    q = ListQ()
    c_1 = 0 # Kontrollvariabel
    print("Välkommen till labb 4!\n")
    while c_1 != 1:
        start = input("Startord: ")
        if swe.exists(start):
            c_2 = 0 # Kontrollvariabel
            while c_2 != 1:
                end = input("Slutord: ")
                if swe.exists(end):
                    used.put(start)
                    q.put(ParentNode(start))
                    found = False
                    if q.isEmpty() and found == False:
                        print("Det fanns ingen lösning, det är ju omöjligt!!!!!1")
                    else:
                        while not q.isEmpty():
                            if found == False:
                                k = q.get()
                                children = makeChildren(k)
                                j, found = checkThings(swe, used, q, children, end)
                            else:
                                print("Det finns en väg till", end)
                                q.hand = []
                        li = []
                        writeChain(j, li)
                        li.reverse()
                        s = ""
                        count = 0
                        for i in li[:-1]:
                            count += 1
                            s += i+" -> "
                        s += end
                        print(s)
                        print("Det var", count, "steg.")
                        c_1 = 1
                        c_2 = 1
                else:
                    print("Slutordet var inte ett giltigt ord. Försök igen.")
        else:
            print("Startordet var inte ett giltigt ord. Försök igen.")

def checkThings(swe, old, q, children, end):
    for j in children:
        i = j.word
        if i == end:
            return (j, True)
        elif swe.exists(i) and not old.exists(i):
            old.put(i)
            q.put(j)
    return (None, False)


def writeChain(j, li):
    li.append(j.word)
    if j.parent:
        writeChain(j.parent, li)

def makeChildren(node):
    ALPH = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'å', 'ä', 'ö']
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
