##from molgrafik import Molgrafik, Ruta
from hashtest import *
from time import *

def lasfil(filnamn):
    songtable = []
    with open(filnamn,"r",encoding='utf-8') as fil:
        for rad in fil:
            data = rad.split("<SEP>")
            artist = data[2].strip()
            song = data[3].strip()
            a = ""
            s = ""
            a = a.join(artist.split())
            s = s.join(song.split())
            songtable.append(a+" "+s)
    return songtable

def hitta(artist, songtable):
    start = time()
    print(songtable[artist])
    stop = time()
    tidhash = stop - start
    return tidhash

songtable = lasfil("unique_tracks.txt")
##song_list = []
##for i in songtable:
##    a = ""
##    s = ""
##    a = a.join(artist.split())
##    s = s.join(songtable[artist].split())
####    print(a, s)
##    song_list.append(a+" "+s)

def makeHashtable(song_list):
    """Lagrar atomlistans element i en hashtabell"""
    print("\n-------------------------------------------------------")
    print(" * Lagrar listans atomer i hashtabell...")
    antalElement = len(song_list)
    hashtabell = Hashtabell(antalElement)
    for element in song_list:
        try:
            namn, vikt = element.split()
            nyAtom = Atom(namn, vikt)
            hashtabell.put(namn, nyAtom)
        except:
            print(element, "blev fel.")
    print(hashtabell)
    return hashtabell

hashtabell = makeHashtable(songtable)
artist = "Elude"
tidhash = hitta(artist, hashtabell)
print(tidhash)
