from molgrafik import Molgrafik, Ruta
from hashtest import *

def search(hashtabell, atomlista):
    s = input("Atombeteckning: ")
    try:
        return Ruta(Atom(s.capitalize(), hashtabell.get(s.capitalize()).weight))
    except KeyError:
        print("Okänd atom. Försök igen.")
        return None


atomlista = skapaAtomlista()
hashtabell = lagraHashtabell(atomlista)
allaAtomerFinns(hashtabell, atomlista)    
knasAtomFinnsInte(hashtabell)
mg = Molgrafik()
while True:
    r = search(hashtabell, atomlista)
    if r:
        mg.show(r)
        mg.root = None
        
