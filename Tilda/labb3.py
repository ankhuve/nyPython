from bintreeFile import *
def main():
    tree = Bintree()
    v = 1
    while v != "0":
        v = input("Vilket värde vill du sätta in i trädet? ")
        if tree.exists(v):
            print("Värdet finns redan i trädet!")
        elif v == "0":
            print("Hejdå!")
        else:
            tree.put(v)
            print(v, "sattes in i trädet.")

main()
