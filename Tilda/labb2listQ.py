from listQfile import ListQ

class LinkedQ(object):
        """Vilka attribut ska kön ha?"""
        def __init__(self, q):
                self.first = None
                self.last = None

        def __str__(self):
        """Returnerar köns element som en sträng.
           Tips: Titta på kursens FAQ (under Hjälp)"""

        def put(self,x):
                # q.hand.append(x)
                if self.isEmpty == True:
                        self.first = x
                        self.last = x
                else:
                        x.next = self.first
                        self.first = x
        """Stoppar in x sist i kön """

        def get(self):
                if self.isEmpty == True:
                        print("Det finns inga kort i högen.")
                else:
                        x = self.first.value
                        self.first = self.first.next
                return x
        """Plockar ut och returnerar det som står först i kön """

        def isEmpty(self):
                if self.first = None:
                        return True
                else:
                        return False
        """Returnerar True om kön är tom, False annars """

class Node:
        def __init__(self, v):
                self.value = v
                self.next = None

q = ListQ()
lq = LinkedQ(q)
k = input("Vilka kort vill du lägga till i listan? Separera siffrorna med ett mellanslag: ")
k = k.split()
for i in k:
	lq.put(Node(i))

bord = []
for i in range(0,len(k)*2):
	if i%2==0:
		x = lq.get()
		lq.put(x)
	else:
		bord.append(lq.get())
	# print(q.hand)
print(bord)

