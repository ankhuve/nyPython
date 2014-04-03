from sys import stdin
from hashfil5 import *
from molgrafik1 import *

def readFormel():               #Läser in tecken för tecken
    mol = readMol()
    if que.peek() != "\n":              #Fångar upp ett enterslag
        raise SyntaxError ("Felaktig gruppstart vid radslutet ")
    return mol                  #Returnerar alla mol, dvs alla rutor 

def readMol():              #Anropa readGroup och ev sig själv (men inte om imatningen är slut eller om den just kommit tillbaka ifrån ett paratesuttryck)
    if que.isEmpty():
        return True
    mol = readGroup()
    x = que.peek()
    if x != None and x not in ")\n":
        mol.next = readMol()        # Så att vi kan skapa fler rutor
    return mol 

def readGroup():                #Anropar readAtom, eller läser en parantes och anropar readMol
    rutan = Ruta()
    x = que.peek()
    if x == "(":
        que.get()
        rutan.down = readMol()      #Gör så att atom inuti hamnar nere
        y = que.peek()
        if y == ")":                #Så länge vi har en högerparentes så kommer denna if-sats köras, alla siffror efter resp kommer tas upp av readNum()
            que.get()
            rutan.num = readNum()
        else:
            raise SyntaxError ("Saknad högerparentes vid radslutet")
    elif x in letter:
        raise SyntaxError ("Saknad stor bokstav vid radslutet ")
    else:
        if x not in LETTER:
            raise SyntaxError ("Felaktig gruppstart vid radslutet ")
        atomnamn = readAtom()               #Tar in hela atomen
        rutan.atom = atomnamn
        x = que.peek()
        if x !=None and x in number:
            rutan.num = readNum()
    return rutan # Retunerar hela rutan 

def readAtom():                 #Kollar om stor bokstav, eller stor bokstav & liten bokstav
    x = que.get()
    if x in LETTER:
        atomnamn = x
        y = que.peek()
        if y != None and y in letter:
            atomnamn += que.get()
        if atomnamn not in delar:
            raise SyntaxError ("Okänd atom vid radslutet ")
    else:
        raise SyntaxError("Saknad stor bokstav vid radslutet " + x)
    return atomnamn
    
def readNum():                 #Tänk på att man kan läsa in flera siffror
    x = que.peek()
    if x not in number:
        raise SyntaxError ("Saknad siffra vid radslutet ")
    else:
        siffror = ""
        if x=="0":
            x = que.get()
            raise SyntaxError ("För litet tal vid radslutet ")
        while que.peek()!=None and que.peek() in number:
            x= que.get()
            siffror = siffror + x 
        n = int(siffror)
        if n<2:                 #Täcker upp 10
            raise SyntaxError ("För litet tal vid radslutet ")
        else:
            pass
    return int(siffror)

def weight(mol):
    if mol== None:#om ingen molekyl
        return 0
    print (mol.atom)
    if mol.atom == "()": #om det är en parantesgrupp 
        vikt = weight(mol.down) * mol.num #vikten är rutan nedåt * nummer
    else:
        vikt = hashtabell.get(mol.atom)*mol.num# iannatfall fås vikten från hashtabellen * nummer
    vikt = vikt + weight(mol.next) #vikten + vikten av rutan brevid

    return vikt
    
    
        
    
    
    
    
class LinkedQ():
    
    def __init__(self):
        """Vilka attribut ska kön ha?"""
        self.first=None
        self.last=None

    def peek(self):
        if self.first==None:
            return None
        else:
            return self.first.value

    def put(self,x):
        """Stoppar in x sist i kön """
        q=Node(x)
        if self.first==None:
            self.first=q
            self.last=q
        else:
            self.last.next=q
            self.last=q

    def get(self):
        """Plockar ut och returnerar det som står först i kön """
        if self.first !=None:
            if self.first == self.last:
                self.last=None
            tmp=self.first
            self.first=self.first.next
            return tmp.value
        else:
            raise IndexError()

    def isEmpty(self):
         """Returnerar True om kön är tom, False annars """
         if self.first==None:
             
             return True
         else:
             
             return False

        
class Node():
    def __init__(self,k):
        self.value=k
        self.next=None
        

    def __str__(self):
        """Returnerar köns element som en sträng. (Vi retunerar ingen sträng.) 
        Tips: Titta på kursens FAQ (under Hjälp)"""
        return self.value

number = ("0123456789")
LETTER = ("ABCDEFGHIJKLMNOPQRSTUVWXYZÅÄÖ")
letter = ("abcdefghijklmnopqrstuvwxyzåäö")
godkandaAtomer = ("H He Li Be B C N O F Ne Na Mg Al Si P S Cl Ar")
delar = godkandaAtomer.split(" ")
mg = molgrafik1()       #Skapar ett objekt av klassen molgrafik1
mol = Ruta()            #Skapar ett objekt av klassen Ruta

atomlistan = skapaAtomlista()
hashtabell = lagra(atomlistan)

rad = input("Atom")
while rad.strip() != "#":
    que = LinkedQ()
    for t in rad:
        que.put(t)
    que.put("\n")                   #Lägger till ett enter för att kunna avsluta 
    try:
        mol = readFormel()
        print ("Formeln är syntaktiskt korrekt")
        vikt = weight()
        mg = show(mol)
        print ("Molekyl:" + str(vikt))
    except SyntaxError as e:
        """"e är vårt syntax fel, skriver ut det i slutet, samlar alla fel i en whileloop"""
        print (e,end="")                    #Vi samlar resten av kön
        while not que.isEmpty():
            print (que.get(),end="")        #Vi samlar resten av kön
    rad = input("Atom")
