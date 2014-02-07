class Bintree:
    def __init__(self):
        self.root=None

    def put(self, n):
        if self.root == None:
            self.root = n
        self.root=putta(self.root,newvalue)

    def exists(self, v):
        if self.root == None:
            return False
        return finns(self.root,value)

    def write(self):
        skriv(self.root)
        print("\n")

class Node:
    def __init__(self, v):
        self.value = v
        self.left = None
        self.right = None
