class Bintree:
    def __init__(self):
        self.root=None

    def put(self, new_value):
        """skickar sin rotpekare och det nya
    ordet till en rekursiv funktion putFunc"""
        self.root=putFunc(self.root, new_value)

    def exists(self,value):
        return existsFunc(self.root, value)

    def write(self):
        writeFunc(self.root)
        print("\n")

class Node:
    def __init__(self, v):
        self.value = v
        self.left = None
        self.right = None


def putFunc(root, value):
    """ser till att en ny nod skapas på rätt ställe"""
    if root == None:
        root = Node(value)
    else:
        if value > root.value and not root.right:
            root.right = Node(value)
        elif value < root.value and not root.left:
            root.left = Node(value)
        else:
            if value > root.value:
                putFunc(root.right, value)
            else:
                putFunc(root.left, value)

            
def existsFunc(root, v):
    if root == None:
        return False
    else:
        if root.value == v:
            return True
        else:
            if v > root.value and root.right:
                existsFunc(root.right, v)
            elif v < root.value and root.left:
                existsFunc(root.left, v)
            else:
                return False

            
def writeFunc(root):
    if root == None:
        print("Det finns inget i trädet.")
    elif root and not root.left and not root.right:
        l = []
        l.append(root.value)
        print(l)
    
        




