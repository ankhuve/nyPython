from bintreeFile import *
svenska = Bintree()
with open("word3.txt", "r", encoding = "utf-8") as svenskfil:
    for rad in svenskfil:
        ordet = rad.strip()                # Ett trebokstavsord per rad
        if svenska.exists(ordet):
            pass
        else:
            svenska.put(ordet)             # in i sökträdet
            
