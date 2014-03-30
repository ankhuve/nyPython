from sys import *
from linkedQfile import LinkedQ

class Syntaxfel(Exception):
    def __init__(self,value,q):
        self.value = value
        self.rest = ""
        while not(q.isEmpty()):            
            self.rest = self.rest + q.get()

    def __str__(self):
        return self.value + " vid radslutet" + self.rest

def readformel(mol):
    global valid
    molq = LinkedQ()
    for letter in mol:
        molq.put(letter)
    if(molq.isEmpty()):
        print("Formeln är syntaktiskt korrekt")
        return 0
    elif(molq.peek() in "1234567890"):
        print("Felaktig gruppstart vid radslutet" + writeq(molq))
        valid = False
    readmol(molq)
    if not(molq.isEmpty()):
        if(molq.peek() == ")"):
            if(valid):
                print("Felaktig gruppstart vid radslutet" + writeq(molq))
                valid = False
    if(valid):print("Formeln är syntaktiskt korrekt")
    
def readmol(molq):
    global valid
    readgroup(molq)
    if not(molq.isEmpty()):
        if not(molq.peek() == ")"):
            readmol(molq)

def readgroup(molq):
    global valid
    if not(molq.isEmpty()):
        if(molq.peek() == "("):        
            molq.get()
            readmol(molq)
            if not(molq.isEmpty()):
                if(molq.get() != ")"):
                    if(valid):
                        valid = False
                        print("Saknad högerparentes vid radslutet" + writeq(molq))#raise Syntaxfel("Saknad högerparentes vid", molq) 
            else:
                if(valid):
                    valid = False
                    print("Saknad högerparentes vid radslutet" + writeq(molq))#raise Syntaxfel("Saknad högerparentes vid", molq) 
            if not(check_num(molq)):
                if(valid):
                    print("Saknad siffra vid radslutet" + writeq(molq))
                    valid = False                
        else:        
            if(molq.peek() == ")"):
                if(valid):
                    print("Felaktig gruppstart vid radslutet" + writeq(molq))
                    valid = False
                    return 0
            if(molq.peek() in "1234567890"):
                print("Felaktig gruppstart vid radslutet" + writeq(molq))
                valid = False
            readatom(molq)
            if not(molq.isEmpty()):
                if(molq.peek() in "1234567890"): check_num(molq)
           

def readatom(molq):
    global valid
    
    if not(molq.isEmpty()):LETTER2  = molq.peek()
    else: LETTER2 = "ä"
    
    if not(check_LETTER2(LETTER2)):
        if(valid):
            valid = False
            print("Saknad stor bokstav vid radslutet" + writeq(molq))# raise Syntaxfel("Saknad stor bokstav",molq)

    if not(molq.isEmpty()): molq.get()
    letter = "ä"
    if not(molq.isEmpty()):
        letter = molq.peek()
        
    if(check_letter(letter)):
        if not(molq.isEmpty()): molq.get()
        if not(LETTER2 + letter in ["He","Li","Be","Ne","Na","Mg","Al","Si","Cl","Ar"]):
            if(valid):
                valid = False
                print("Okänd atom vid radslutet" + writeq(molq))#
    elif not(LETTER2 in ["H","B","C","N","O","F","P","S"]):
        if(valid):
            valid = False
            print("Okänd atom vid radslutet" + writeq(molq))#

def check_LETTER2(LETTER):
    if(LETTER in "QWERTYUIOPASDFGHJKLZXCVBNMMNBVCXZLKJHGFDSAPOIUYTREWQ"):
        return True
    return False

def check_letter(letter):
    if(letter in "qwertyuiopasdfghjklzxcvbnmmnbvcxzllkjhgfdsapoiuytrewq"):
        return True
    return False

def check_num(molq):
    global valid
    ret = False
    num = "ä"
    if not(molq.isEmpty()):
        if(molq.peek() in "1234567890"):
            num = molq.get()
            
        if(num in "0"):
            if(valid):
                valid = False
                print("För litet tal vid radslutet" + writeq(molq))
        elif(num in "1"):
            if not(molq.isEmpty()):                
                if not(molq.peek() in "1234567890"):
                    if(valid):
                        valid = False
                        print("För litet tal vid radslutet" + writeq(molq))
            if(molq.isEmpty()):
                if(valid):
                    valid = False
                    print("För litet tal vid radslutet" + writeq(molq))
        elif(num in "23456789"):
            ret = True
            
    if not(molq.isEmpty()):
        while(molq.peek() in "1234567890"):
            ret = True
            molq.get()
            if(molq.isEmpty()): break
    return ret

def writeq(q):
    if(q.isEmpty()):
        return ""
    else:
        rest = " "
        while not(q.isEmpty()):            
            rest = rest + q.get()
        return rest
                                     

inrad = stdin.readline()

while inrad:
    listan =inrad.split()
    for rad in listan:        
        if(rad.strip() == "#"): break
        valid = True
        readformel(rad.strip())
    inrad = stdin.readline()
