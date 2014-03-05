from hashtest import *

def search(hashtabell, atomlista):
    s = input("Atombeteckning: ")
    try:
        print(hashtabell.get(s.capitalize()).weight)
    except KeyError:
        print("Okänd atom. Försök igen.")


atomlista = skapaAtomlista()
hashtabell = lagraHashtabell(atomlista)
allaAtomerFinns(hashtabell, atomlista)    
knasAtomFinnsInte(hashtabell)
while True:
    search(hashtabell, atomlista)
