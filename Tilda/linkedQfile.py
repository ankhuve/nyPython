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
            s += str(p.value)+" "
            p = p.next
        return s

    def put(self,x):
        """Stoppar in x sist i kön """
        if self.isEmpty() == True:
            self.first = x
            self.last = x
        elif self.last == x:
            self.first = x
            self.last = None
        else:
            self.last.next = x
            self.last = x

    def get(self):
        """Plockar ut och returnerar det som står först i kön """
        if self.isEmpty() == True:
            print("Det finns inga kort i högen.")
        else:
            x = self.first
            self.first = self.first.next
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
