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
