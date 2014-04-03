class LinkedQ():
    """Vilka attribut ska kön ha?"""
    def __init__(self):
        self.first = None
        self.last = None

    def __str__(self):
        """Returnerar köns element som en sträng.
        Tips: Titta på kursens FAQ (under Hjälp)"""
        s = ""
        p = self.first
        while p != None:
            s += str(p.value)+""
            p = p.next
        return s

    def put(self, x, rev=1):
        """Stoppar in x sist i kön """
        if self.isEmpty() == True:
                self.first = x
                self.last = x
        elif rev == 1: # Sätt in sist i kön
            if self.last == x:
                self.first = x
                self.last = None
            else:
                self.last.next = x
                self.last = x
                x.next = None
        else: # Sätt in först i kön
            if self.first == x:
                x.next = self.first
                self.first = x
                self.last = self.first.next
            else:
                x.next = self.first
                self.first = x
    
    def peek(self):
        if self.first == None:
            return None
        else:
            return self.first.value

    def get(self, rev=1):
        """Plockar ut och returnerar det som står först i kön """
        
        if self.isEmpty() == True:
            print("Det finns inga kort i högen.")
        else:
            if rev == 1: # Ta längst fram i kön
                if self.first == self.last:
                    x = self.first
                    self.first = None
                    self.last = None
                else:
                    x = self.first
                    self.first = self.first.next
            else: # Ta längst bak från kön
                x = self.last
                c = self.first
                while c != None:
                    if c.next == x:
                        self.last = c
                        c.next = None
                        break
                    else:
                        c = c.next
        return x

    def isEmpty(self):
        """Returnerar True om kön är tom, False annars """
        if self.first == None and self.last == None:
            return True
        else:
            return False

class Node:
    def __init__(self, v):
            self.value = v
            self.next = None

class MolQOps():
    def __init__(self, in_str):
        self.q = LinkedQ()
        self.previous = ""
        self.open = 0
        self.NUMS = ["0","1","2","3","4","5","6","7","8","9"]
        self.ALPH = "ACBDEFGHIJKLMNOPQRSTUVWXYZ"
        self.ATOMS = ["H","He","Li","Be","B","C","N","O","F","Ne","Na","Mg","Al","Si","P","S",
                "Cl","K","Ar","Ca","Sc","Ti","V","Cr","Mn","Fe","Ni","Co","Cu","Zn","Ga","Ge",
                "As","Se","Br","Kr","Rb","Sr","Y","Zr","Nb","Mo","Tc","Ru","Rh","Pd","Ag","Cd",
                "In","Sn","Sb","I","Te","Xe","Cs","Ba","La","Ce","Pr","Nd","Pm","Sm","Eu","Gd",
                "Tb","Dy","Ho","Er","Tm","Yb","Lu","Hf","Ta","W","Re","Os","Ir","Pt","Au","Hg",
                "Tl","Pb","Bi","Po","At","Rn","Fr","Ra","Ac","Pa","Th","Np","U","Am","Pu","Cm",
                "Bk","Cf","Es","Fm","Md","No","Lr","Rf","Db","Hs","Sg","Bh","Mt","Rg","Ds","Cn"]
        self.createMolQ(in_str)

    def createMolQ(self, in_str):
            for i in in_str:
                self.q.put(Node(i))
            self.readFormula()

    def readFormula(self):
        print("readFormula")
        self.readMol()

    def readMol(self):
        print("readMol")
        if self.q.isEmpty():
            print("kön är tom")
            return True
        self.readGroup()
        if self.q.peek() != None:
            print("read mol för andra gången")
            self.readMol()

    def readGroup(self):
        print("readGroup")
        if self.q.peek() == "(":
            self.q.get()
            self.readMol()
            if self.q.peek() == ")":
                self.q.get()
                self.readNum()
            else:
                raise SyntaxError ("Saknad högerparentes vid radslutet " + str(self.q))
        elif self.q.peek() in self.ALPH.lower():
            raise SyntaxError ("Saknad stor bokstav vid radslutet " + str(self.q))
        else:
            print("yolo")
            if self.q.peek() not in self.ALPH:
                raise SyntaxError ("Felaktig gruppstart vid radslutet " + str(self.q))
            self.readAtom()
            print(self.q.peek())
            if self.q.peek() !=None and self.q.peek() in self.NUMS:
                self.readNum()
                
            
        

    def readAtom(self):
        print("readAtom")
        a = self.q.get().value
        print(a)
        if a in self.ALPH:
            atomname = a
            if self.q.peek()!= None and self.q.peek() in self.ALPH.lower():
                atomname += self.q.get().value
            if atomname not in self.ATOMS:
                raise SyntaxError ("Okänd atom vid radslutet "+str(self.q))
        else:
            raise SyntaxError("Saknad siffra vid radslutet "+ a)
            
            
        
    def readNum(self):
        print("readNum")
        if self.q.peek() not in self.NUMS:
            raise SyntaxError ("Saknad siffra vid radslutet "+str(self.q))
        else:
            numbers=""
            if self.q.peek()=="0":
                raise SyntaxError("För litet tal vid radslutet "+str(self.q))
            while self.q.peek()!=None and self.q.peek() in self.NUMS:
                n=self.q.get().value
                numbers += n
            n = int(numbers)
            if n<2:
                raise SyntaxError ("För litet tal vid radslutet "+ str(self.q))
            

def main():
    in_str = ""
    while in_str != "#":
        in_str = input()
        try:
            MolQOps(in_str)
            print("formeln är syntaktiskt korrekt")
        except SyntaxError as msg:
            print(msg)
        
main()
