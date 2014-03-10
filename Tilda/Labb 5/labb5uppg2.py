from hashtest import *

def search(hash_table):
    """ Sökfunktionen. Returnerar vikten på atomen, eller om atomen inte finns
    så skrivs det ut. Inparameter är hash_tableen. """
    s = input("Atombeteckning: ")
    try:
        return(hash_table.get(s.capitalize()).weight)
    except KeyError:
        return("Okänd atom. Försök igen.")

def main():
    """ Huvudfunktionen. Skapar hash_tableen och testar att allt är korrekt.
    Startar även search-funktionen där man söker efter atom. """
    atomlista = skapaAtomlista()
    hash_table = lagraHashtabell(atomlista)
    allaAtomerFinns(hash_table, atomlista)    
    knasAtomFinnsInte(hash_table)
    while True:
        print(search(hash_table))

main()
