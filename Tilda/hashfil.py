class Hashtabell():
    def __init__(self, elements):
        self.elements = elements
        self.table = {}

    def __str__(self):
        s = ""
        for i in self.table.keys():
            s += "Atom: "+str(self.table[i])+"\n"
        return s

    def put(self, name, atom):
        hash_value = self.createHash(name)
        c = False
        while not c:
            try:
                if self.table[hash_value]:
                    hash_value += 1
            except KeyError:
                self.table[hash_value] = atom
                c = True
                
    def get(self, name):
        hash_value = self.createHash(name)
        try:
            return self.table[hash_value]
        except KeyError:
            print("Det fanns ingen atom som heter så.")
    
    def createHash(self, name):
        ALPH = "abcdefghijklmnopqrstuvwxyzåäö"
        ALPH = list(ALPH)
        VALS = [28, 1]
        name = list(name)
        hash_value = 0
        for i in range(len(name)):
            hash_value += (ALPH.index(name[i].lower())+1)*VALS[i]
        return hash_value
