#Niklas Gustavsson, Cmete2, 920330-4077
#Datum

#Funktion som öppnar vår infil, där användaren själv får skriva in vad filen heter
#Hittar inte programmet filen så kommer den be användaren att försöka igen
#Return a returnerar vår infil i textformat. 
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


#En funktion för att göra om element i vår lista till int om det är möjligt, behövs
#i vår funktion listmaker för att göra om de delar av infilen som behövs till int, för att senare
#kunna göra matematiska beräkningar med dem. T.ex score samt games played
# http://stackoverflow.com/questions/9869524/how-to-convert-list-of-intable-strings-to-int
def convert_int(tempList2):
    for x in tempList2:
        try:
            x=int(x)
        except ValueError:
            pass
        yield x


#Den här funktionen är bland de viktigaste. Den använder vår infil som inparameter, gör om den
#i en serie av listor, från ett flertal strängar, till en lista av strängen, till en lista med
#all vår data. tempList är en lista med en enda lång sträng. Den strängen splittas sen upp
#och extendas till vår tempList2, där även de siffror som finns görs om till Int (ifrån strängar)
#Sist så appendas dessa listor till en slutlig lista ourList. Det här är en lista av listor med 6 värden
#Slutligen använder vi våran klass Teams för att göra om listan av listor till en lista av objekt
#för att lättare kunna hantera våra objekt!
#Inparametern är vår textfil, och returnvärdet är en lista av objekt.
#Funktionen använder sig av funktionen convert_int för att göra om elementen i vår tempList2 till int om möjligt.
def objectMaker(a):
    ourList = []
    next(a) #hoppar över första raden
    for Line in a:
        elements=Line.replace("-"," ").split(",")
        for i in elements:
            i = i.strip("\n")
            tempList=[]
            tempList.append(i)
            tempList2=[]
            for i in tempList:
                tempList2.extend(i.split())
            tempList2=list(convert_int(tempList2))
            ourList.append(tempList2 if (len(tempList2) <=6) else ["{0} {1}".format(tempList2[0],tempList2[1])]+tempList2[2:])
    teamObjects=[Teams(*p) for p in ourList]
    return teamObjects        

       
#En klass för att göra objekt av våra lag, konstruktorn använder vi i funktionen objectMaker.
#Här lagras alla lags information i form utav objekt.
#def __str__ är en funktion som används för att kunna printa ut vad som  finns lagrat i objekten
#Attributen som sätts i konstruktorn är självförklarande. 
class Teams():
    def __init__(self, teamname, wins, draws, losses, goals, neggoals):
        self.teamname = teamname
        self.wins = wins
        self.draws = draws
        self.losses = losses
        self.goals = goals
        self.neggoals = neggoals
        self.score = wins*3+draws*1
        self.played = wins+losses+draws
    def __str__(self):
        return "%s:\t%s\t%s\t%s\t%s\t%s-%s\t%s" % (self.teamname, self.played, self.wins, self.draws, self.losses, self.goals, self.neggoals, self.score)




#För att sen kunna söka efter ett lagnamn och ändra på ett attribut så gör vi om det till ett dictionary
#av objekt. Alltså är objekten fortfarande de samma, men de representeras på en annan form. Det här gör
#det väldigt simpelt att söka efter ett lagnamn, och sedan ändra något av attributen.
#ourDict innehåller samma objekt som vår teamObjects, bara på en annan form (i form av en dictionary)
#ändrar man på något i ourDict, ändras det även i teamObjects. 
def dictMaker(teamObjects):
    ourDict={x.teamname: x for x in teamObjects}
    return ourDict


#Funktion som sorterar vår lista av objekt efter Score.
#inparameter=utparameter, vår lista av objekt. Enbart att man sorterar den efter poäng.
#Funktionen kallas på varje tillfälle som användaren lägger in nytt resultat, samt när
#infilen hämtas in.
def sort(teamObjects):
    teamObjects.sort(key=lambda x: x.score, reverse=True)
    return teamObjects


#Funktion som skriver ut vad som för nuvarande finns lagrat i våra objekt, så att användaren
#kan se tabellen. 
def scoreboard(teamObjects):
    print("\n\nThe current scoreboard is as follows: \n\n")
    print("\t\tP\tW\tD\tL\tG\tSc")
    n=0
    for x in teamObjects:
        n+=1
        print(n,str(x))

#Funktion för att användaren ska kunna lägga till matchresultat.
#Här använder vi oss av vårt dictionary. Användaren skriver först in lagnamnen,
#och sedan resultatet. Funktionen uppdaterar då de relevanta objekten och de
#attribut som ändrats.
#Inparameter är våran dictionary över objekten. Vi behöver ingen utparameter,
#eftersom våra objekt uppdateras automatiskt i funktionen.
def add_score(ourDict):
    score = False
    while score == False:
        try:
            
            hometeam = input("      What's the hometeam called?       ").title()
            awayteam = input("      What's the away team called?        ").title()
            userinput = input("What was the score? On the form X-Y   ")
            templist=userinput.split("-")
            x=int(templist[0])
            y=int(templist[1])
    
        
            ourDict[hometeam].goals += x
            ourDict[awayteam].goals += y
            ourDict[hometeam].neggoals += y
            ourDict[awayteam].neggoals += x
            ourDict[hometeam].played += 1
            ourDict[awayteam].played += 1
            if x > y:
                ourDict[hometeam].wins +=1
                ourDict[awayteam].losses +=1
                ourDict[hometeam].score +=3
            elif x < y:
                ourDict[hometeam].losses +=1
                ourDict[awayteam].wins +=1
                ourDict[awayteam].score +=3
            elif x == y:
                ourDict[hometeam].draws +=1
                ourDict[awayteam].draws +=1
                ourDict[hometeam].score +=1
                ourDict[awayteam].score +=1
            score=True
        except:
            print("That did not work, please try again!")


#Användaren kan när som helst spara den nuvarande tabellen på en textfil som väljs.
#inparametern är våran lista av objekt, eftersom det är denna som ska skrivas ut på en fil. Ingen
#utparameter behövs. Allting sker i funktionen.
def savefile(teamObjects):
    read = False
    for i in teamObjects:
        while read == False:
            try:
                fileName=input("Please enter the name of the file you want to save the score in: ")
                b=open(fileName, "w")
                b.write("\t\tP\tW\tD\tL\tG\tSc\n")
                b.write("\n".join(str(x) for x in teamObjects))
                read = True
            except IOError:
                print ("That file could not be found, please try again!")

    

#Menyfunktionen, där användaren väljer vad han vill göra för något. Varje val här kallar på en eller flera
#av de funktioner som programmet använder. 
def menu():
    print("""\n\n\n\n\nHello! This is a program designed to import a textfile containing
numerous teams and their current scores. When starting the program, you will be introduced to
a menu function. The first thing you should do is import a textfile containing your teams.
This is option 1 in the menu.

When you have done this, you have 4 different choices. The first one is to enter a result of
a game. You will be prompted to enter which 2 teams have faced off, and what the result was.
The second option is to see the current scoreboard, which will be sorted after the score of each
team in descending order. The third option is to save your current scoreboard on a textfile of
your choosing. And the fifth and final option is to exit the program when you are done! Enjoy!!\n\n\n""")
    s = 0;
    while(s != "5"):
        print("\n\n1 - Fetch your chart")
        print("2 - Enter a score")
        print("3 - See current scoreboard")
        print("4 - Save current score as text file")
        print("5 - Exit program")
        s=(input("What would you like to do??  "))
        if s=="1":
            a=openfile()
            teamObjects=objectMaker(a)
            sort(teamObjects)
            ourDict=dictMaker(teamObjects)
        if s=="2":
            add_score(ourDict)
            sort(teamObjects)
        if s=="3":
            scoreboard(teamObjects)
        if s=="4":
            savefile(teamObjects)
        if s=="5":
            break
                      

def main():
    menu()

main()

