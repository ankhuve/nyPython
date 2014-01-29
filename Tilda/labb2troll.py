from linkedQfile import *
from listQfile import ListQ

def main():
    q = ListQ()
##    q = LinkedQ()
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
    table_string = ""
    for i in table:
        table_string += i+" "
    print(table_string)

main()
