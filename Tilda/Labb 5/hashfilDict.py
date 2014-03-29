class Hashtable():
    """Klass för hashtabellen."""
    def __init__(self, elements):
        """Konstruktor. Inparameter är antal element. """
        self.elements = elements # antal element
        self.table = {} # Hashtabellen som dict

    def __str__(self):
        """För att skriva ut hashtabellen. Returnerar tabellen som sträng."""
        s = ""
        for i in self.table.keys():
            s += "Atom: "+str(self.table[i])+"\n"
        return s

    def put(self, name, atom):
        """Sätter in atomen i self.table med name som key."""
        self.table[name] = atom
                
    def get(self, name):
        """Metod för att hämta en atom. Raise KeyError om atomen ej finns.
    Inparameter är sökordet, returnerar atomen om den finns."""
        try:
            return self.table[name]
        except:
            raise KeyError
