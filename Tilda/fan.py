from bintreeFile import *
from linkedQfile import *
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
                    while not q.isEmpty():
                        way_found = False
                        k = q.get()
                        children = makeChildren(k.value.word)
                        for i in children:
                            if swe.exists(i) and not gamla.exists(i):
                                gamla.put(i)
                                q.put(Node(ParentNode(i, k.value)))
                            elif i == end:
                                way_found = True
                            else:
                                pass
                            if way_found == True:
                                chain = [k.value.word]
                                c = 0
                                while c != 1:
                                    if isinstance(k, Node):
                                        chain.append(k.value.parent.word)
                                        k = k.value.parent
                                    elif isinstance(k, ParentNode):
                                        chain.append(k.word)
                                        k = k.parent
                                    else:
                                        c = 1
                                print("Vägen hittades!")
                                print(chain)
                                break
                        
                    c_1 = 1
                    c_2 = 1
                else:
                    print("Slutordet var inte ett giltigt ord. Försök igen.")
        else:
            print("Startordet var inte ett giltigt ord. Försök igen.")

class ParentNode:
    def __init__(self, word, parent = None):
        self.word = word
        self.parent = parent

def makeChildren(word):
    ALF = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'å', 'ä', 'ö']
    children = []
    for i in range(3):
        for k in ALF:
            if i == 0:
                new_word = k+word[1:]
            elif i == 1:
                new_word = word[0]+k+word[-1]
            else:
                new_word = word[:2]+k
            children.append(new_word)
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
