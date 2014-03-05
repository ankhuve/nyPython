##import math
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
        while not self.isPrime(n):
            n += 1
        for i in range(n):
            l.append(None)
        print("Tabellen blev", len(l), "platser stor.")
        return l

    def put(self, name, atom):
        hash_value = self.createHash(name)
        
        c = False
        i = 0
        while not c:
            hash_value = hash_value % len(self.table)
            i += 1
            try:
                if self.table[hash_value]:
                    hash_value += i**2
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
##        hash_value = hash_value % len(self.table)
        i = 0
        c = False
        try:
            while not c:
                hash_value = hash_value % len(self.table)
                if self.table[hash_value].name.lower() == name.lower():
                    c = True
                    return self.table[hash_value]
                else:
                    i += 1
                    hash_value += i**2
                    print("Inte rätt!")
##                    hash_value = hash_value%len(self.table)
        except (IndexError, AttributeError):
            raise KeyError
            
    def createHash(self, key):
        nums = [6547, 233]
        hash_value = 0
        for i in range(len(key)):
            hash_value += ord(key[i]) * (nums[0] + ord(key[i]))
            nums[0] = nums[1] % (hash_value*nums[0])
        return hash_value

    def isPrime(self, key):
        import math
        prime = None
        while prime == None:
            for i in range(2, math.ceil(key**0.5)+1):
                if key==i:
                    prime = True
                    return prime
                elif key%i == 0:
                    prime = False
                    return prime
            prime = True
        return prime
