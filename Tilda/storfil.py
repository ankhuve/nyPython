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
            if song == "":
                song = "(None)"
            a = ""
            s = ""
            a = a.join(artist.split())
            s = s.join(song.split())
            songtable.append(a+" "+s)
    return songtable

def hitta(artist, hashtabell):
    start = time()
    print(hashtabell.get(artist))
    stop = time()
    tidhash = stop - start
    return tidhash

def makeHashtable(song_list):
    """Lagrar atomlistans element i en hashtabell"""
    print("\n-------------------------------------------------------")
    print(" * Lagrar listans atomer i hashtabell...")
    antalElement = len(song_list)
    hashtabell = Hashtabell(antalElement)
    s = time()
    for element in song_list:
        try:
            artist, song = element.split()
            entry = Atom(artist, song)
            hashtabell.put(artist, entry)
        except:
            print(element, "blev fel.")
    e = time()
    t = e - s
    print("Tabellen gjordes på", t, "sekunder.")
    return hashtabell

songtable = lasfil("unique_tracks.txt")
hashtabell = makeHashtable(songtable)
artist = "Elude"
tidhash = hitta(artist, hashtabell)
print(tidhash)
