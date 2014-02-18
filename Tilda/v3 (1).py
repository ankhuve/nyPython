from bintreeFile import *
svenska = Bintree()
with open("word3.txt", "r", encoding = "utf-8") as svenskfil:
    for rad in svenskfil:
        ordet = rad.strip()                # Ett trebokstavsord per rad
        if svenska.exists(ordet):
            pass
        else:
            svenska.put(ordet)             # in i sökträdet
            
baklanges = Bintree()
f = open('word3.txt', "r", encoding = "utf-8")
data = f.read().replace('.',"").split()
for i in data:
    if baklanges.exists(i[::-1]):
        pass
    else:
        if(svenska.exists(i[::-1])):
            if(i == i[::-1]):
               pass
            
            elif(baklanges.exists(i)):
                 pass

            else:
                print(i, i[::-1], end = "\n")
        else:
            pass
        baklanges.put(i[::-1])
        
