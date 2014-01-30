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
##    table_string = ""
##    for i in table:
##        table_string += i+" "
##    print("Resultatet blev:", table_string, "\n")

def backwardTrick():
    q = ListQ()
    hand = ListQ()
    k = input("Vilka kort vill du lägga till i listan? Separera siffrorna med ett mellanslag: ")
    k = k.split()
    for i in k:
        q.put(Node(i))
    table = []
    
    for i in range(len(k)):
        if hand.isEmpty() == True:
            x = q.get(-1)
            hand.put(x)
        else:
            x = q.get(-1)
            hand.put(x, 0)
            y = hand.get(-1)
            hand.put(y, 0)
    printResult(hand.hand)
##    table_string = ""
##    for i in hand.hand:
##        table_string += i.value+" "
##    print("Resultatet blev:", table_string, "\n")

def printResult(l):
    table_string = ""
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
