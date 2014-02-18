from bintreeFile import *
import time
def main():
    """ Huvudprogrammet, innehåller meny och kallar på funktioner för de olika valen. """
    tree = Bintree() # Träd för användarens värden
    v = 1 # Variabel för menyval
    print("Välkommen till labben för binära sökträd!\n")
    while v != "0":
        v = input("""Vad vill du göra?\n
    1 - Sätta in något i trädet
    2 - Skriva ut trädet
    3 - Läs in från fil och skriv ut dubbletter (Uppgift 2)
    4 - Jämför engelska och svenska ord (Uppgift 3)
    5 - Jämför tidsåtgång mellan trädsökning och listsökning.
    6 - Kolla ord baklänges (A-delen)
    
    0 - Avsluta\n
Ange ditt val: """)
        if v == "0":
            print("Hejdå!")
        elif v == "1":
            insertIntoTree(tree)
        elif v == "2":
            print("\nTrädet innehåller följande:")
            tree.write() # Skriver ut alla värden i trädet
        elif v == "3":
            print("\nMatchande ord:")
            swe = treeFromFileStuff("word3.txt", 1) # Skapar ett träd
        elif v == "4":
            try:
                if swe: # Kontroll för att se om trädet med svenska finns
                    pass
            except NameError:
                swe = treeFromFileStuff("word3.txt") # Skapar svenskträdet om det inte finns
            print("\nMatchande ord:")
            treeFromFileStuff("engelska.txt", swe) # Kallar på funktionen och skickar in svenskträdet.
        elif v == "5":
            timeComparison()
        elif v == "6":
            backwardsComparison()
        else:
            print("Felaktigt val, försök igen!\n")

def backwardsComparison():
    """ Jämför vilka ord som blir andra svenska ord baklänges och skriver ut dessa en gång. """
    print("\nOrd och orden baklänges:")
    li = [] # Lista som håller reda på vilka ord som redan testats
    swe = treeFromFileStuff("word3.txt")
    with open("word3.txt", "r", encoding = "utf-8") as file:
        for l in file:
            words = l.split()                # Ett trebokstavsord per rad
            for i in words:
                if swe.exists(i[::-1]) and swe.exists(i[::-1]).value != i:
                    if i[::-1] in li: # Om ordet baklänges redan är använt
                        pass
                    else:
                        print(i, i[::-1])
                        li.append(i)
    print("\n")

def insertIntoTree(tree):
    """ Funktion för insättning av värde. Inparameter är användarens träd. """
    c = 1 # Kontrollvariabel
    while c != "0":
        c = input("\nVilket värde vill du sätta in i trädet (0 för att gå tillbaka)? ")
        if c == "0":
            break
        if tree.exists(c):
            print("Det fanns redan i trädet.")
        else:
            tree.put(c)
            print(c, "sattes in i trädet.")
            
def timeComparison():
    """ Jämför tidsåtgång för sökning i träd och lista. """
    swe, li = treeFromFileStuff("word3.txt", 2) # Skapar svenskträdet och en lista med orden
    w = input("Vilket ord vill du söka efter? ")
    c = 0 # Kontrollvariabel
    while c != 1:
        try:
            n = int(input("Hur många sökningar vill du göra (rekommenderar minst 1000 för snabb dator)? "))
            c = 1 # För att bryta while-loopen
            s = time.time() # Starttid
            for i in range(n):
                if swe.exists(w):
                    pass
            e = time.time() # Sluttid
            print("\n"+str(n)+" sökningar i trädet tog", e-s, "sekunder.")
            s = time.time()
            for i in range(n):
                if w in li:
                    pass
            e = time.time()
            print(n, "sökningar i listan tog", e-s, "sekunder.\n")
        except:
            print("Det var inte en giltig siffra, försök igen!\n")

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
