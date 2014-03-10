from molgrafik import Molgrafik, Ruta
from hashtest import *

def search(hash_table, atomlista):
    """ Sökfunktionen. Returnerar vikten på atomen, eller om atomen inte finns
    så skrivs det ut. Inparameter är hash_tableen. """
    s = input("Atombeteckning: ")
    try:
        return Ruta(Atom(s.capitalize(), hash_table.get(s.capitalize()).weight))
    except KeyError:
        print("Okänd atom. Försök igen.")
        return None

def main():
    """ Huvudfunktionen. Skapar hash_tableen och testar att allt är korrekt.
    Startar även search-funktionen där man söker efter atom. Visar en ruta med
    atomen och atom"""
    atomlista = skapaAtomlista()
    hash_table = lagraHashtabell(atomlista)
    allaAtomerFinns(hash_table, atomlista)    
    knasAtomFinnsInte(hash_table)
    mg = Molgrafik()
    while True:
        r = search(hash_table, atomlista)
        if r:
            mg.show(r)
            mg.root = None   

main()
