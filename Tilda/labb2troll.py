from linkedQfile import *
from listQfile import ListQ

def forwardTrick():
##    q = ListQ()
    q = LinkedQ()
    k = input("Vilka kort vill du lägga till i listan? Separera siffrorna med ett mellanslag: ")
    k = k.split()
    for i in k:
        q.put(Node(i))
    table = []
    for i in range(0,len(k)*2):
        if i%2==0:
            x = q.get()
            q.put(x)
        else:
            y = q.get()
            table.append(y.value)
    printResult(table)

def backwardTrick():
##    q = ListQ()
##    hand = ListQ()
    q = LinkedQ()
    hand = LinkedQ()
    k = input("Vilka kort vill du lägga till i listan? Separera siffrorna med ett mellanslag: ")
    k = k.split()
    for i in k:
        q.put(Node(i))
    for i in range(len(k)):
        if hand.isEmpty() == True:
            x = q.get(-1)
            hand.put(x)
        else:
            x = q.get(-1)
            hand.put(x, 0)
            y = hand.get(-1)
            hand.put(y, 0)
    printResult(hand)

def printResult(l):
    table_string = ""
    if isinstance(l, ListQ) == True:
        for k in l.hand:
            table_string += k.value+" "
    elif isinstance(l, LinkedQ) == True:
        c = l.first
        while c != None:
            table_string += c.value+" "
            c = c.next
    else:
        for i in l:
            if isinstance(i, str) == True:
                table_string += i+" "
            else:
                table_string += i.value+" "
    print("Resultatet blev:", table_string, "\n")
    
            
def main():
    c = ""
    print("Hej och välkommen till trolleriprogrammet!")
    while c != "0":
        c = input("1 - Vanliga korttricket\n2 - Korttricket baklänges\n0 - Avsluta\n\nGör ditt val: ")
        if c == "1":
            forwardTrick()
        elif c == "2":
            backwardTrick()
        elif c == "0":
            print("Hejdå!")
        else:
            print("\nAnge ett giltigt val!")

main()
