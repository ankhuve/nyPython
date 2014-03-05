class Hashtabell():
    def __init__(self, elements):
        self.elements = elements
        self.table = self.makeTable(elements*2)

    def __str__(self):
        s = ""
        for i in range(len(self.table)):
            s += "Atom: "+str(self.table[i])+"\n"
        return s

    def makeTable(self, n):
        l = []
        for i in range(n):
            l.append(None)
        return l

    def put(self, name, atom):
        hash_value = self.createHash(name)
        c = False
        i = 0
        while not c:
            i += 1
            try:
                if self.table[hash_value]:
                    hash_value += i**2
                    hash_value%len(self.table)
                else:
                    self.table[hash_value] = atom
                    c = True
            except:
                print("Sätter in..")
                print(hash_value, len(self.table))
                self.table[hash_value] = atom
                c = True
                
    def get(self, name):
        hash_value = self.createHash(name)
        i = 0
        c = False
        try:
            while not c:
                if self.table[hash_value].name.lower() == name.lower():
                    c = True
                    return self.table[hash_value]
                else:
                    i += 1
                    hash_value += i**2
                    hash_value = hash_value%len(self.table)
        except (IndexError, AttributeError):
            raise KeyError
            
    def createHash(self, name):
##        ALPH = list("""abcdefghijklmnopqrstuvwxyzåäö!'#¤%&/()=?\}][{€,*^~¨ôõ~.-"_1234567+890;:ïñãüêúùéóáøàíìçã|""")
        VALS = [26, 1]
        name = list(name)
        hash_value = 0
        for i in range(len(name)):
            if i == 0:
                hash_value += ord(name[i])*VALS[i]
            else:
                hash_value += ord(name[i])*1
##            hash_value += (ALPH.index(name[i].lower())+1)*VALS[i]
        return hash_value%len(self.table)

