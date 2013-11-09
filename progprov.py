d = 3
class Mupp:
    def __init__(self, q, w):
        global d
        d = 3
        self.z = q
        self.x = w
    def knasa(self):
        return self.z + self.x
     
    def smurfa(self, q):
        self.x = q
        
# Huvudprogram
m1 = Mupp("hej", "hopp")
m2 = Mupp("ding", "dong")
m1.smurfa("ett")
m2.smurfa("två")
print (m2)
print (d)
