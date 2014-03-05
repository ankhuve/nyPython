from molgrafik import Molgrafik, Ruta
from hashtest import *

def search(hashtabell, atomlista):
    s = input("Atombeteckning: ")
    name_list = []
    for element in atomlista:
        name, weight = element.split()
        name_list.append(name.lower())
    if s.lower() in name_list:
        return Ruta(Atom(s.capitalize(), hashtabell.get(s).weight))

    else:
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
        
