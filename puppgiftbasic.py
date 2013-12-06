########################################
#####  Erik Forsberg   2013-12-06  #####
########################################

from tkinter import *
import winsound, random, string, math

class Game:
    GRIDSIZE = 10 # 10 är standard. Går att välja tal mellan 10 och 26 (längden av engelska alfabetet)
    def __init__(self, root):
        """ Konstruktor, bestämmer variabler och kör igång createGrid, outerPlacementControl och sätter igång spelmusiken. 
        Inparameter är rotfönstret. """
        self.root = root
        self.SHIPLENGTHS = [5,4,3,3,2] # Antal skepp och hur långa de är.
        self.ship_list = [] # Placerade skepp, fylls med objekt av klassen Ship.
        self.shots = 0 # Antal gånger spelaren skjutit.
        self.hits = 0 # Antal gånger spelaren träffat.
        self.toggle_cheat = False # Är fusk påslaget?
        self.cheater = False # Har spelaren tryckt på fuskknappen?
        self.taken_boxes = [] # Fylls med alla rutor som är upptagna av skepp, objekt av klassen Box.
        self.BGCOLOR = "#689E68" # Standardbakgrundsfärg för rutor.
        self.TERMINAL_FONT = ("terminal", 18, "bold") # Standardfont för text i rutor.
        self.root.title("Sänka Skepp") # Rotfönstrets titel.
        self.root.geometry("+300+0") # Rotfönstrets placering.
        self.box_list = [] # Varje objekt av Box sparas i listor om varje rad i denna lista.
        self.createGrid()
        self.outerPlacementControl()
        winsound.PlaySound("ship n stuff.wav", winsound.SND_ALIAS | winsound.SND_ASYNC | winsound.SND_LOOP) # Starta spelmusiken!

    def createGrid(self):
        """ Skapar det grafiska rutnätet av knappar, koordinater och text samt skapar fuskknappen (döljs nere i det högra hörnet). """
        Grid.rowconfigure(self.root, 0, weight=1)
        Grid.columnconfigure(self.root, 0, weight=1)
        COLUMNS = list(string.ascii_uppercase) # Lista med alfabetet
        Label(text="", bg=self.BGCOLOR).grid(column=0, row=0, sticky=N+S+E+W)# Skapar en lista med alfabetet
        if self.GRIDSIZE>26:
            self.GRIDSIZE=26 # Kontroller för att fixa till storleken av rutnätet om det angetts ett för stort eller för litet värde.
        elif self.GRIDSIZE<10:
            self.GRIDSIZE=10
        [Label(text=COLUMNS[c], fg="darkgreen", bg=self.BGCOLOR, font=self.TERMINAL_FONT).grid(column=c+1, row=0, sticky=N+S+E+W) for c in range(self.GRIDSIZE)] # Sätter ut bokstäver ovanför kolumnerna.
        [Label(text=r, fg="darkgreen", bg=self.BGCOLOR, font=self.TERMINAL_FONT).grid(column=0, row=r, sticky=N+S+E+W) for r in range(1,self.GRIDSIZE+1)] # Sätter ut siffror vänster om raderna.
        for i in range(1,self.GRIDSIZE+1):
            row = [] # Lista som skapas för varje rad.
            for j in range(1,self.GRIDSIZE+1):
                coords = (i,j) # Koordinater på spelfältet, från 1 till GRIDSIZE.
                row.append(Box(self, coords, self.root, "#1789C2"))
            self.box_list.append(row)
        self.info = Label(text="Klicka för att skjuta!", fg="darkgreen", bg=self.BGCOLOR, font=self.TERMINAL_FONT).grid(row=self.GRIDSIZE+1 ,columnspan=self.GRIDSIZE+1, sticky=E+W+S+N) # Text som ger instruktioner samt uppdateras om användaren missar/träffar/sänker
        Label(text="Pricksäkerhet:", fg="darkgreen", bg=self.BGCOLOR, font=("terminal",18)).grid(row=self.GRIDSIZE+2, column=0, columnspan=(math.floor(self.GRIDSIZE/2)), sticky=E+W+S+N)
        Label(text="Antal skott:", fg="darkgreen", bg=self.BGCOLOR, font=("terminal",18)).grid(row=self.GRIDSIZE+2, column=(math.floor(self.GRIDSIZE/2)), columnspan=(math.ceil(self.GRIDSIZE/2)+1), sticky=E+W+S+N)
        cheatbutton = self.buttonMaker(self.root, "fuska lite...", fg=self.BGCOLOR, bg=self.BGCOLOR, font=("terminal", 10)) # Skapar fuskknappen
        cheatbutton.configure(relief=FLAT, width="7", height="1", command=self.cheat)
        cheatbutton.grid(column=self.GRIDSIZE-1, columnspan=2, row=self.GRIDSIZE+1, sticky=N+S+E+W, padx=20)
        self.root.resizable(0,0)
            
    def outerPlacementControl(self):
        """ Kollar om placering av skepp är OK och lägger till skeppen i self.ship_list om så är fallet. """
        self.order = 0 # Håller reda på vilket skepp som försöker slumpas fram.
        for length in self.SHIPLENGTHS:
            placement_check = False # Är placeringen godkänd?
            while placement_check != True:
                placement_check, direction, x, y = self.randomizeAndControl(length) # Kör metoden randomizeAndControl, returnerar om placeringen var godkänd, vilken riktning skeppet har samt dess startkoorinater.
            if direction == "h": # Om horisontell.
                for n in range(length):
                    self.placeShip(n, 0, x, y)
            elif direction == "v":
                for n in range(length):
                    self.placeShip(0, n, x, y)
            self.ship_list.append(Ship(length, (x, y), direction, self.box_list))
            self.order += 1
            
    def randomizeAndControl(self, length):
        """ Slumpar fram en startkoordinat samt riktning och kollar sedan om skeppet går att placera där.
        Inparameter är skeppets längd i antal rutor. 
        Returnerar värden om placeringen blev godkänd, riktning samt startkoordinater. """
        control = False
        while control == False:
            start = random.choice(self.box_list[random.randint(0,self.GRIDSIZE-1)]) # Slumpa fram koordinater för skeppets första ruta.
            x = start.coords[0]-1 # Index i box_list, INTE koordinater på spelplanen.
            y = start.coords[1]-1
            direction = random.choice(["h", "v"])
            try:
                if direction == "h":
                    self.box_list[x+(length-1)][y] # Kontrollera om skeppet slutar innanför spelplanen.
                    for i in range(length):
                        control = self.controlBorders(i, 0, x, y)
                        if control == False:
                            break
                elif direction == "v":
                    self.box_list[x][y+(length-1)] # Kontrollera om skeppet slutar innanför spelplanen.
                    for i in range(length):
                        control = self.controlBorders(0, i, x, y)
                        if control == False:
                            break
            except IndexError: # Om skeppet skulle hamna utanför spelplanen.
                return False, direction, x, y
            return control, direction, x, y

    def controlBorders(self, i, j, x, y):
        """ Kontrollerar så att det inte ligger något skepp inom en rutas avstånd (jag låter dock skepp ligga diagonellt kant-i-kant). 
        Körs lika många gånger som skeppet är rutor långt.
        Inparameterförklaring: i eller j ökar med ett för varje körning. Ett av dessa värden är alltid 0 
        beroende på slumpad riktning av skeppet. x och y är startkoordinaterna för skeppet. 
        Skeppen växer alltså från startkoordinaterna, till höger eller neråt beroende på riktning.
        Returnerar True om det inte överlappar något skepp eller ligger bredvid ett annat, False annars."""
        tests = [(x-1+i, y+j),(x+1+i, y+j),(x+i, y-1+j),(x+i, y+1+j),(x+i, y+j)] # Varje kontroll som ska göras, ovanför, under, till höger och till vänster om den rutan i skeppet som kontrolleras.
        for n in tests:
            corrected = self.controlPastGridEdge(n) # Fixar till kontrollerna om det behövs (om den skulle försöka kontrollera utanför spelplanen eller så). Lista med fixade koordinater sparas i corrected.
            tests[tests.index(n)] = (corrected[0], corrected[1]) # Värdena förs över till tests som tuple.
        try:
            for k in range(5):
                if self.box_list[tests[k][0]][tests[k][1]].status != 0: # Om status inte är noll betyder det att rutan är upptagen, sätter då control till False.
                    control = False
                    break
                else:
                    control = True
        except IndexError:
            control = False
        return control

    def controlPastGridEdge(self, n):
        """ Fixar till koordinaterna som ska kontrolleras om de skulle gå utanför spelplanen.
        Inparameter är koordinaterna som ska kollas.
        Returnerar lista med fixade koordinater. """
        corrected = []
        for coord in n:
            if coord>(self.GRIDSIZE-1):
                corrected.append(self.GRIDSIZE-1)
            elif coord<0:
                corrected.append(0)
            else:
                corrected.append(coord)
        return corrected

    def placeShip(self, i, j, x, y):
        """ Om placeringen blivit godkänd så läggs de tagna rutorna till i taken_boxes och status för de tagna rutorna ändras. 
        Rutorna får också order, vilket motsvarar vilket skepp som ligger på de rutorna.
        Inparametrar är samma som för controlBorders."""
        self.box_list[x+i][y+j].status = 1
        self.box_list[x+i][y+j].order = self.order
        self.taken_boxes.append(self.box_list[x+i][y+j])

    def fireInTheHole(self, coords):
        """ Metod som körs när användaren klicka på en ruta. Kontrollerar om det är en träff/miss/träff&sänk. Färgar rutan enligt träff=röd, miss=vit. Kontrollerar om användaren har sänkt alla skepp och kör då endGameCheck. Uppdaterar text om pricksäkerhet och antal skott samt infotext som talar om för användaren vad som hänt. Gör ingenting om rutan redan är skjuten på.
        Inparameter är koordinater (på spelplanen) för den klickade rutan."""
        box = self.box_list[coords[0]-1][coords[1]-1] # Gör om koordinaterna så att de motsvarar korrekt index i box_list.
        if box.status == 1: # Om rutan innehåller ett skepp.
            shot_status = "Träff!"
            self.shots += 1
            self.ship_list[box.order].hits += 1
            box.status = 3
            box.changeColor("red")
            self.hits += 1
            self.updateStats(self.shots, self.hits, shot_status)
            if self.hits==(sum(self.SHIPLENGTHS)):
                self.hitNSunk(box)
                self.endGameCheck()
            elif self.ship_list[box.order].hits == self.ship_list[box.order].length:
                self.hitNSunk(box)
        elif box.status == 0: # Om rutan inte innehåller ett skepp.
            shot_status = "Bom.."
            self.shots += 1
            box.status = 2
            box.changeColor("white")
            self.updateStats(self.shots, self.hits, shot_status)
        else: # Om rutan redan är skjuten på.
            pass

    def hitNSunk(self, box):
        """Färga det sänka skeppet samt "skjuta" på alla rutor runt skeppet
        då det inte kan vara något annat skepp där.
        Inparameter är rutan man klickade på senast (objekt av Box)"""
        for ship in self.ship_list:
            if box in ship.includes: # Leta igenom ship_list efter skeppet som innehåller rutan som sänkte skeppet.
                for adjacent in ship.adjacent:
                    adjacent.changeColor("white")
                    adjacent.status = 2
                for ship_part in ship.includes:
                    ship_part.changeColor("#8A5353")
                break
        shot_status = "Träff och sänk!"
        self.updateStats(self.shots, self.hits, shot_status)
        
    def hitNSunk2(self):
        """Om man vill ha popup för varje träff sänk? För tillfället avaktiverad."""
        self.popup = Toplevel()
        self.popup.title("Träff & sänk!")
        self.popup.configure(background=self.BGCOLOR)
        self.popup.geometry("+520+250")
        text = Label(
            self.popup, text="Du sänkte skeppet!",
            bg=self.BGCOLOR, fg="darkgreen", font=("terminal", 18)).grid(columnspan=2, sticky=N+S+E+W, ipadx=10, ipady=10)
        ok = self.buttonMaker(self.popup)
        ok.configure(command=self.popup.destroy)
        ok.grid(columnspan=2, row=3, sticky=N+S+E+W, padx=10, pady=10)
        self.popup.resizable(0,0)
            
    def updateStats(self, shots, hits, shot_status):
        """ Uppdaterar texten i rotfönstret med info om träff/miss/sänk, samt antal skott och pricksäkerhet.
        Inparametrar är antal skott, antal träffar och vad det senaste skottet var (miss/träff/sänk)."""
        try:
            accuracy = (self.hits/self.shots)*100
        except ZeroDivisionError: # Om första skottet är en träff.
            accuracy = 1
        Label(text=shot_status, fg="darkgreen", bg=self.BGCOLOR, font=self.TERMINAL_FONT).grid(row=self.GRIDSIZE+1, column=math.ceil(self.GRIDSIZE/7), columnspan=math.floor(self.GRIDSIZE*0.75), sticky=E+W+S+N)
        Label(text=str(accuracy)[:4]+"%", fg="darkgreen", bg=self.BGCOLOR, font=("terminal",18)).grid(row=self.GRIDSIZE+2, column=math.ceil(self.GRIDSIZE/3), sticky=W+N+S)
        Label(text=str(self.shots), fg="darkgreen", bg=self.BGCOLOR, font=("terminal",18)).grid(row=self.GRIDSIZE+2, column=self.GRIDSIZE-1, sticky=W+N+S)
            
    def endGameCheck(self):
        """ Hämtar först de tio bästa resultatet från textfilen och kontrollerar sedan om resultatet platsar på high-score-listan. """
        top_ten_pct = self.getTopTen(self.readFile())
        try:
            if (self.hits/self.shots)*100 > top_ten_pct[-1] or len(top_ten_pct)<10:
                self.highScorePopup(self.shots, self.hits, "Grattis!",
                                    "Grattis, du lyckades ta dig in på high-score-listan!\nVar god ange ditt namn i rutan nedanför.")
            else:
                self.highScorePopup(self.shots, self.hits, "Tyvärr..", "Du lyckades tyvärr inte ta dig in på high-score-listan..")
        except IndexError: # Om high-score-listan är tom.
            self.highScorePopup(self.shots, self.hits, "Grattis!",
                                    "Grattis, du lyckades ta dig in på high-score-listan!\nVar god ange ditt namn i rutan nedanför.")
    def highScorePopup(self, shots, hits, title, info):
        """ Skapar en popup som antingen berättar att man kvalificerats till high-score-listan, eller att man inte gjorde det.
        Inparametrar är antal skott, antal träffar, titel på det nya fönstret och vad som ska stå i texten i fönstret. """
        accuracy = (self.hits/self.shots)*100 # Procentuell pricksäkerhet.
        self.popup = Toplevel() # Skapar nytt fönster på högsta nivån.
        self.popup.title(title)
        self.popup.configure(background=self.BGCOLOR)
        self.popup.geometry("+310+250")
        text = Label(
            self.popup, text=info,
            bg=self.BGCOLOR, fg="darkgreen", font=("terminal", 18)).grid(columnspan=2, sticky=N+S+E+W, ipadx=20, ipady=20)
        if title == "Grattis!":
            name = StringVar() # Skapa strängvariabel för namnet.
            entry = Entry(self.popup, font=("terminal", 18), textvariable=name).grid(row=3, sticky=E+W+N+S, padx=8, pady=8)
            ok = self.buttonMaker(self.popup)
            ok.configure(command=lambda accuracy=str(accuracy)[:4]: self.highScoreEntry(accuracy, self.popup, name))
            ok.grid(column=1, row=3, sticky=E+W, padx=8, pady=8)
        elif title == "Tyvärr..":
            ok = self.buttonMaker(self.popup, "Avsluta")
            ok.configure(command=self.exitGame)
            ok.grid(row=3, column=1, sticky=N+S+E+W, padx=4, pady=4)
            restart = self.buttonMaker(self.popup, "Spela igen")
            restart.configure(command=lambda: self.restartGame(self.popup))
            restart.grid(column=0, row=3, sticky=N+S+E+W, padx=4, pady=4)
            list_hs = self.buttonMaker(self.popup, "Visa high-scores")
            list_hs.configure(command=lambda: self.listHighScores(self.getTopTen(self.readFile(), 0)))
            list_hs.grid(column=2, row=3, sticky=N+S+E+W, padx=4, pady=4)
        self.popup.resizable(0,0)
        self.popup.mainloop()

    def exitGame(self):
        """ Stoppar musiken och stänger spelet. """
        winsound.PlaySound(None, winsound.SND_ASYNC)
        self.root.destroy()

    def restartGame(self, popup):
        """ Stänger popup-rutan och startar om spelet.
        Inparameter är popup-rutan. """
        popup.destroy()
        self.__init__(self.root)
            
    def readFile(self):
        """ Öppnar textfilen som innehåller high-scores samt läser in vad som finns i listan. 
        Returnerar det som stod i textfilen. """
        text = open("highscores.txt", "r")
        self.info = text.read()
        return self.info

    def getTopTen(self, info, qualified=1):
        """ Hämta topp tio från high-score-listan.
        Inparametrar är det som stod i textfilen och om man är kvalificerad till high-score eller inte.
        Returnerar den sorterade high-score-listan om man inte är kvalificerad, och topp tio om man är det. """
        hs_list = []
        for entry in self.info.splitlines():
            entry = entry.split(" | ")
            hs_list.append((entry[0],entry[1]))
        sorted_hs = sorted(hs_list, key=lambda a: float(a[0]), reverse=True)
        if qualified==1:
            top_ten_pct = []
            if len(sorted_hs)>10:
                [top_ten_pct.append(float(sorted_hs[i][0])) for i in range(10)]
            else: 
                [top_ten_pct.append(float(sorted_hs[i][0])) for i in range(len(sorted_hs))]
            return top_ten_pct
        else:
            self.popup.destroy()
            return sorted_hs

    def buttonMaker(self, win, info="OK", fg="darkgreen", bg="#93C993", font=("terminal", 18)):
        """ Metod för att skapa knappar.
        Inparametrar är vilket fönster knappen ska finnas i, vad som ska stå på knappen och med vilken textfärg, bakgrundsfärg och font.
        Returnerar knappen. """
        return Button(win, text=info, fg=fg, bg=bg, font=font)

    def highScoreEntry(self, accuracy, popup, name):
        """ Skriver in namn och pricksäkerhet i high-scorelistan. Kollar också om man har fuskat eller ej och märker high-scoren om man har fuskat.
        Inparametrar är pricksäkerhet, popup-rutan och strängvariabeln name. """
        hs_list = []
        for entry in self.info.splitlines():
            entry = entry.split(" | ")
            hs_list.append((entry[0],entry[1]))
        if self.cheater == False:
            hs_list.append((accuracy, name.get())) # name.get() hämtar namnet man skrev in i textfältet.
        else:
            hs_list.append((accuracy, str(name.get())+" (med fusk!)")) # Lägg till "(med fusk!)" om man har fuskat.
        sorted_hs = sorted(hs_list, key=lambda a: float(a[0]), reverse=True)
        updated_hs = open("highscores.txt", "w+")
        [updated_hs.write(str(float(i[0]))+" | "+i[1]+"\n") for i in sorted_hs]
        updated_hs.close()
        self.listHighScores(sorted_hs)
        self.popup.destroy()
        
    def listHighScores(self, sorted_hs):
        """ Skapar ett nytt fönster där high-score-listan visas.
        Inparameter är den sorterade high-score-listan. """
        high_scores = Toplevel()
        high_scores.title("High-score")
        high_scores.configure(background=self.BGCOLOR)
        high_scores.geometry("+345+110")
        Label(high_scores, text="Topp tio", font=self.TERMINAL_FONT, fg="darkgreen",
              bg="#93C993").grid(columnspan=2, sticky=N+S+E+W, ipadx=20, ipady=20)
        for i in range(len(sorted_hs)):
            if i>9:
                break
            Label(high_scores, text=str(i+1)+". "+str(float(sorted_hs[i][0]))+"% | "+str(sorted_hs[i][1]), 
                bg=self.BGCOLOR, fg="darkgreen", font=("terminal", 12)).grid(sticky=N+S+W, ipadx=20, ipady=5, columnspan=2)
        ok = self.buttonMaker(high_scores, "Avsluta")
        ok.configure(command=self.exitGame)
        ok.grid(row=12, column=1, sticky=N+S+E+W, padx=4, pady=4)
        restart = self.buttonMaker(high_scores, "Spela igen")
        restart.configure(command=lambda: self.restartGame(high_scores))
        restart.grid(column=0, row=12, sticky=N+S+E+W, padx=4, pady=4)

    def cheat(self):
        """ Fuskfunktionen, visar skeppen om de är dolda, döljer skeppen om de visas. Sätter self.cheater till True om man slagit på fusket någon gång. """
        if self.toggle_cheat == True: # Om fusket är påslaget
            for obj in self.taken_boxes:
                if obj.status == 1:
                    obj.changeColor("#1789C2") # Dölj skeppen
            self.toggle_cheat = False # Om fusket är avslaget
        else:
            for obj in self.taken_boxes:
                if obj.status == 1:
                    obj.changeColor("#8C8C8C") # Visa skeppen
            self.cheater, self.toggle_cheat = True, True

class Box(Game):
    def __init__(self, parent, coords, root, color):
        """ Konstruktor, bestämmer variabler och skapar knappen.
        Inparametrar är rutans koordinater, rotfönstret samt rutans färg. """
        self.status = 0 # Rutans status. Sätts till 0 från början. 0=rutan ej beskjuten, inget fartyg ligger här, 1=rutan ej beskjuten, del av fartyg ligger här, 2=rutan beskjuten, bom, 3=rutan beskjuten, träff.
        self.coords = coords # Rutans koordinater.
        self.order = -1 # Rutor utan skepp får order -1
        self.root = root # Rotfönstret.
        self.button = Button(
            self.root, bg=color,
            activebackground="blue",
            relief=GROOVE, cursor="target",
            command=lambda coords=self.coords, game=parent: Game.fireInTheHole(game, coords)
            )
        self.button.config(width="7",height="3")
        self.button.grid(column=self.coords[0], row=self.coords[1])
        Grid.columnconfigure(self.root,self.coords[0],weight=1)

    def changeColor(self, color):
        """ Byter färg på rutan.
        Inparameter är färgen man vill byta till. """
        self.button.configure(bg=color)

class Ship(Game):
    def __init__(self, length, coords, direction, box_list):
        """ Konstruktor, bestämmer variabler och hämtar närliggande rutor.
        Inparametrar: skeppets längd, koordinater, riktning, game.box_list. """
        self.length = length # Skeppets längd.
        self.direction = direction # Skeppets riktning.
        self.coords = coords # Skeppets koordinater.
        self.hits = 0 # Antal träffar som skeppet fått.
        self.includes = [] # Lista med rutor som skeppet täcker.
        self.adjacent = [] # Lista med rutor som är runt omkring skeppet.
        self.getAdjacent(box_list)

    def getAdjacent(self, box_list):
        """ Lägg till alla rutor runt omkring skeppet i self.adjacent.
        Inparameter är game.box_list. """
        if self.direction == "h":
            c, d = 1, 0
        elif self.direction == "v":
            c, d = 0, 1
        for l in range(self.length): # Körs för varje ruta i skeppet
            self.includes.append(box_list[self.coords[0]+l*c][self.coords[1]+l*d])
            tests = [(self.coords[0]-1+l*c, self.coords[1]+l*d),(self.coords[0]+1+l*c, self.coords[1]+l*d),(self.coords[0]+l*c, self.coords[1]-1+l*d),(self.coords[0]+l*c, self.coords[1]+1+l*d)]
            for n in tests:
                corrected = Game.controlPastGridEdge(self, n)
                tests[tests.index(n)] = (corrected[0], corrected[1])
            try:
                for k in range(4):
                    if not box_list[tests[k][0]][tests[k][1]] in self.includes:
                        self.adjacent.append(box_list[tests[k][0]][tests[k][1]])
            except IndexError:
                pass
        for n in self.includes:
            if n in self.adjacent:
                self.adjacent.remove(n) # Plocka bort skeppets rutor från adjacent

    def getInbound(self, box_list):
        """ Lägger till alla rutor som skeppet täcker i includes.
        Inparameter är game.box_list. """
        if self.direction == "h":
            c, d = 1, 0
        elif self.direction == "v":
            c, d = 0, 1
        for l in range(self.length):
            self.includes.append()


########## Main ##########
def main():
    """ Main-funktion, skapar rotfönster och drar sen igång spelet. """
    root=Tk()
    game = Game(root)
    root.mainloop()

############
main()
winsound.PlaySound(None, winsound.SND_ASYNC) # Sluta spela musik om rotfönstret stängs
############