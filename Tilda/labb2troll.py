from labb2 import *
from listQfile import ListQ

def main():
    q = ListQ()
    ##q = LinkedQ()
    k = input("Vilka kort vill du lägga till i listan? Separera siffrorna med ett mellanslag: ")
    k = k.split()
    for i in k:
        q.put(Node(i))
        
    bord = []
    for i in range(0,len(k)*2):
        if i%2==0:
            x = q.get()
            q.put(x)
    ##        print("Kort", x.value, "flyttades bak i leken.")
        else:
            y = q.get()
            bord.append(y)
    ##        print("Kort", y.value, "läggs på bordet.")
    for i in bord:
            print(i.value)

main()
