##from molgrafik import Molgrafik, Ruta
from hashtest import *
from time import *

def readFile(file_name):
    """Läser in filen och skapar en lista med alla artister och sånger.
    Inparameter är filnamnet. Returnerar listan."""
    songtable = []
    with open(file_name,"r",encoding='utf-8') as text_file:
        for line in text_file:
            data = line.split("<SEP>")
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

def find(artist, hashtable):
    """Funktion för att söka efter en artist. Inparameter är hashtabellen.
    Returnerar tiden det tog för sökningen."""
    start = time()
    print(hashtable.get(artist))
    stop = time()
    time_hash = stop - start
    return time_hash

def makeHashtable(song_list):
    """Lagrar atomlistans element i en hashtabell. Inparameter är listan med låtarna. Returnerar hashtabellen."""
    print("\n-------------------------------------------------------")
    print(" * Lagrar listans atomer i hashtabell...")
    number_of_elements = len(song_list)
    hashtable = Hashtable(number_of_elements)
    s = time()
    for element in song_list:
        try:
            artist, song = element.split()
            entry = Atom(artist, song)
            hashtable.put(artist, entry)
        except:
            print(element, "blev fel.")
    e = time()
    t = e - s
    print("Tabellen gjordes på", t, "sekunder.")
    return hashtable

def main():
    """ Huvudfunktionen. Skapar hashtabellen och testar att allt är korrekt.
    Startar även search-funktionen som letar upp artisten och visar hur lång tid det tog. """
    songtable = readFile("unique_tracks.txt")
    hashtable = makeHashtable(songtable)
    artist = "Elude"
    time_hash = find(artist, hashtable)
    print(time_hash)

main()
