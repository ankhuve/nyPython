import os
def openfile():
    read = False
    while read == False:
        try:
            fileName=input("Please enter the name of the file you want to open: ")
            a=open(fileName,"r")
            read = True
        except IOError:
            print ("That file could not be found, please try again!")
    return a

# http://stackoverflow.com/questions/9869524/how-to-convert-list-of-intable-strings-to-int
def convert_int(c):
    for x in c:
        try:
            x=int(x)
        except ValueError:
            pass
        yield x


def listmaker(a):
    ourList = []
    next(a) #hoppar över första raden
    for Line in a:
        elements=Line.replace("-"," ")
        for i in elements:
            i = i.strip("!\n,. \t=!_ -'")
            b=[]
            b.append(i)
            c=[]
            for i in b:
                c.extend(i.split())
            c=list(convert_int(c))                  #gör en ny lista för att redan här        
            ourList.append(c)                       #kunna splitta vår string till flera bitar
    for i in ourList:                               #och därefter kunna göra om str till int för poängen
        ourList[ourList.index(i)]=i[::-1]
    return ourList


def savefile(ourList):
    read = False
    for i in ourList:
        ourList[ourList.index(i)]=i[::-1]
    while read == False:
        try:
            fileName=input("Please enter the name of the file you want to save the score in: ")
            b=open(fileName, "w")
            b.write("        V O F  M\n")
            for i in ourList:
                b.write("%s\n" % i)
            read = True
        except IOError:
            print ("That file could not be found, please try again!")
    return b



def menu():
    s = 0;
    while(s != "4"):
        print("\n\n1 - Fetch your chart")
        print("2 - Enter a score")
        print("3 - See current scoreboard")
        print("4 - Exit program and save current score as text file")
        s=(input("What would you like to do??  "))
        if s=="1":
            a=openfile()
            ourList=listmaker(a)
            c=convert_int(ourList)
        if s=="2":
            if not ourList:
                print("No chart has been retrieved, please try again")
            else:
                print (ourList)
        if s=="3":
            print("najs")
        if s=="4":
            savefile(ourList)
            break
                      



def main():
    a=openfile()
    ourList=listmaker(a)
    

menu()

