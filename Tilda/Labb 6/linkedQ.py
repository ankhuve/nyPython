class LinkedQ(object):

    def __init__(self,first=None,last=None): 
        """Vilka attribut ska kön ha?"""
        self.first=first
        self.last=last


    def __str__(self):
        s = ""
        p = self.first
        while p != None:
            s = s + str(p.varde)
            p = p.next
        return s
	    #Returnerar köns element som en sträng.
        #Tips: Titta på kursens FAQ (under Hjälp)'''

    def put(self,x):
        """Stoppar in x sist i kön """
        ny= Nod(x)
        if self.isEmpty():  
            self.last= ny
            self.first=ny
        else:
            self.last.next=ny   #sista nuvarande noden pekar på ny
            self.last=ny        #referensen last ändras till att peka på ny.



    def get(self):
        """Plockar ut och returnerar det som står först i kön """
        try:
            taUt=self.first.varde
            self.first=self.first.next  #ändrar starten på länkade listan
            if self.first==None:
                self.last=None
        except AttributeError:  #dvs blir tom lista!
            #Fångas ej upp i vårt program.
            taUt='listan är tom'
        return taUt

    def peek(self):
        return self.first.varde



    def isEmpty(self):
        """Returnerar True om kön är tom, False annars """
        if self.first == None:
            return True
        else:
            return False

        

class Nod(object):

    def __init__(self,varde,next=None): 
        """Vilka attribut ska kön ha?"""
        self.next=next
        self.varde=varde

    def __str__(self):  
        """Returnerar köns element som en sträng.
        Tips: Titta på kursens FAQ (under Hjälp)"""
        return (str(self.varde)+', ')

