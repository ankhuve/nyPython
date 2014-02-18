class Bintree:
    def __init__(self):
        """ Konstruktor. Skapar en rot till trädet. """
        self.root=None #trädets rot

    def put(self, new_value):
        """ Skickar sin rotpekare och det nya
    ordet till en rekursiv funktion putFunc. Inparameter är det nya värdet. """
        self.root=putFunc(self.root, new_value)

    def exists(self,value):
        """Skickar sin rotpekare och ordet till en rekursiv funktion existFunc och
    returnerar nod som söks, om nod inte finns returneras None.
    Inparameter är det nya värdet"""
        return existsFunc(self.root, value)

    def write(self):
        """Kör metoden writeFunc med trädets rot som inparameter"""
        writeFunc(self.root)
        print("\n")

class Node:
    """ Klass för nod. """
    def __init__(self, v):
        """Skapar en nod som har info om sitt eget värde samt info om noderna till höger resp vänster.
    Inparameter är värdet"""
        self.value = v # Nodens värde
        self.left = None # Nodens "gren" till vänster
        self.right = None # Nodens "gren" till höger

def putFunc(node, value):
    """Ser till att en ny nod skapas på rätt ställe. Inparameter är aktuell nod samt det nya värdet.
    Returnerar uppdaterad nod. """
    if node is None:
        return Node(value)
    else:
        if value > node.value and not node.right:
            node.right = Node(value)
        elif value < node.value and not node.left:
            node.left = Node(value)
        elif value > node.value:
            node.right = putFunc(node.right, value)
        else:
            node.left = putFunc(node.left, value)
        return node
    
def existsFunc(node, v):
    """Kollar om noden finns i trädet. Inparameter är aktuell nod och det nya värdet.
    Returnerar noden när den hittats/inte hittats. Noden är None om den inte hittats.""" 
    if node is None or node.value == v:
        return node
    elif v > node.value:
        return existsFunc(node.right, v)
    else:
        return existsFunc(node.left, v)
            
def writeFunc(node):
    """Skriver ut trädets värden. Inparameter aktuell nod"""
    if node is not None:
        writeFunc(node.left)
        print(node.value)
        writeFunc(node.right)
