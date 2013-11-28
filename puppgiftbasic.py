from tkinter import *
import winsound
import random

class Game:
    def __init__(self, root):
        self.SHIPS = [5,4,3,3,2]
        self.ship_list = []
        self.shots = 0
        self.hits = 0
        self.toggle_cheat = False
        self.cheater = False
        self.placed_ships = []
        self.bgcolor = "#689E68"
        self.terminal_font = ("terminal", 18, "bold")
        root.title("Sänka Skepp")
        root.geometry("+300+0")
        self.box_list = self.createGrid()
        self.randomizeShipPlacement()
        
        winsound.PlaySound("ship n stuff.wav", winsound.SND_ALIAS | winsound.SND_ASYNC | winsound.SND_LOOP)
        

    def createGrid(self):
        Grid.rowconfigure(root, 0, weight=1)
        Grid.columnconfigure(root, 0, weight=1)
        columns = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]        
        Label(text="", bg=self.bgcolor).grid(column=0, row=0, sticky=N+S+E+W)
        [Label(text=columns[c], fg="darkgreen", bg=self.bgcolor, font=self.terminal_font).grid(column=c+1, row=0, sticky=N+S+E+W) for c in range(10)]
        [Label(text=r, fg="darkgreen", bg=self.bgcolor, font=self.terminal_font).grid(column=0, row=r, sticky=N+S+E+W) for r in range(1,11)]
        box_list = []
        for i in range(1,11):
            row = []
            for j in range(1,11):
                coords = (i,j)
                row.append(Box(coords, root, "#1789C2"))
            box_list.append(row)
        self.info = Label(text="Klicka för att skjuta!", fg="darkgreen", bg=self.bgcolor, font=self.terminal_font).grid(row=11 ,columnspan=11, sticky=E+W+S+N)
        Label(text="Pricksäkerhet:", fg="darkgreen", bg=self.bgcolor, font=("terminal",18)).grid(row=12, column=0, columnspan=5, sticky=E+W+S+N)
        Label(text="Antal skott:", fg="darkgreen", bg=self.bgcolor, font=("terminal",18)).grid(row=12, column=5, columnspan=6, sticky=E+W+S+N)
        cheatbutton = self.buttonMaker(root, "fuska lite...", fg=self.bgcolor, bg=self.bgcolor, font=("terminal", 10))
        cheatbutton.configure(relief=FLAT, width="7", height="1", command=self.cheat)
        cheatbutton.grid(column=9, columnspan=2, row=11, sticky=N+S+E+W, padx=20)
        root.resizable(0,0)
        return box_list
            
    def randomizeShipPlacement(self):
        self.order = 0
        for ship in self.SHIPS:
            placement_check = False
            while placement_check != True:
                placement_check, direction, x, y = self.controlPlacement(ship)
            if direction == "h":
                for n in range(ship):
                    self.placeShip(n, 0, x, y)
                self.ship_list.append(Ship(ship, (x ,y), direction))
            elif direction == "v":
                for n in range(ship):
                    self.placeShip(0, n, x, y)
                self.ship_list.append(Ship(ship, (x, y), direction))
            self.order += 1
            
    def controlPlacement(self, ship):
        control = False
        while control == False:
            start = random.choice(self.box_list[random.randint(0,9)])
            x = start.coords[0]-1
            y = start.coords[1]-1
            direction = random.choice(["h", "v"])
            try:
                if direction == "h":
                    self.box_list[x+(ship-1)][y] # Kontrollera om skeppet slutar innanför spelplanen
                    for i in range(ship):
                        control = self.controlBorders(i, 0, x, y)
                        if control == False:
                            break
                elif direction == "v":
                    self.box_list[x][y+(ship-1)] # Kontrollera om skeppet slutar innanför spelplanen
                    for i in range(ship):
                        control = self.controlBorders(0, i, x, y)
                        if control == False:
                            break
            except IndexError: # Om skeppet skulle hamna utanför spelplanen
                return False, direction, x, y
            return control, direction, x, y

    def controlBorders(self, i, j, x, y):
        tests = [(x-1+i, y+j),(x+1+i, y+j),(x+i, y-1+j),(x+i, y+1+j),(x+i, y+j)]
        for n in tests:
            corrected = self.controlPastGridEdge(n)
            tests[tests.index(n)] = (corrected[0], corrected[1])
        try:
            if (
                self.box_list[tests[4][0]][tests[4][1]].status != 0 # kolla överlapp
                or self.box_list[tests[0][0]][tests[0][1]].status != 0 # vänster
                or self.box_list[tests[1][0]][tests[1][1]].status != 0 # höger
                or self.box_list[tests[2][0]][tests[2][1]].status != 0 # över
                or self.box_list[tests[3][0]][tests[3][1]].status != 0 # under
                ):
                control = False
            else:                                   
                control = True
        except IndexError:
            control = False
        return control

    def controlPastGridEdge(self, n):
        corrected = []
        for coord in n:
            if coord>9:
                corrected.append(9)
            elif coord<0:
                corrected.append(0)
            else:
                corrected.append(coord)
        return corrected

    def placeShip(self, i, j, x, y):
        self.box_list[x+i][y+j].status = 1
        self.box_list[x+i][y+j].order = self.order
        self.placed_ships.append(self.box_list[x+i][y+j])

    def fireInTheHole(self, coords, status):
        box = self.box_list[coords[0]-1][coords[1]-1]
        if box.status == 1:
            shot = "Träff!"
            self.shots += 1
            self.ship_list[box.order].hits += 1
            box.status = 3
            box.changeColor("red")
            self.hits += 1
            self.updateStats(self.shots, self.hits, shot)
            if self.hits==(17):
                self.endGameCheck()
            elif self.ship_list[box.order].hits == self.ship_list[box.order].length:
                #self.hitNSunk()
                shot = "Träff och sänk!"
                self.updateStats(self.shots, self.hits, shot)
        elif box.status == 0:
            shot = "Bom.."
            self.shots += 1
            box.status = 2
            box.changeColor("white")
            self.updateStats(self.shots, self.hits, shot)
        else:
            pass

    def hitNSunk(self, box, coords):
        """Tänkt att metoden ska färga det sänka skeppet samt "skjuta" på alla rutor runt skeppet
        då det inte kan vara något annat skepp där."""
        for i in range(box):
            pass
        
    def hitNSunk2(self): # om man vill ha popup för varje träff sänk? För tillfället avaktiverad.
        self.popup = Toplevel()
        self.popup.title("Träff & sänk!")
        self.popup.configure(background=self.bgcolor)
        self.popup.geometry("+520+250")
        text = Label(
            self.popup, text="Du sänkte skeppet!",
            bg=self.bgcolor, fg="darkgreen", font=("terminal", 18)).grid(columnspan=2, sticky=N+S+E+W, ipadx=10, ipady=10)
        ok = self.buttonMaker(self.popup)
        ok.configure(command=self.popup.destroy)
        ok.grid(columnspan=2, row=3, sticky=N+S+E+W, padx=10, pady=10)
        self.popup.resizable(0,0)
            
    def updateStats(self, shots, hits, shot):
        try:
            accuracy = (self.hits/self.shots)*100
        except ZeroDivisionError:
            accuracy = 1
        Label(text=shot, fg="darkgreen", bg=self.bgcolor, font=self.terminal_font).grid(row=11, column=2, columnspan=7, sticky=E+W+S+N)
        Label(text=str(accuracy)[:4]+"%", fg="darkgreen", bg=self.bgcolor, font=("terminal",18)).grid(row=12, column=4, sticky=W+N+S)
        Label(text=str(self.shots), fg="darkgreen", bg=self.bgcolor, font=("terminal",18)).grid(row=12, column=9, sticky=W+N+S)
            
    def endGameCheck(self):
        top_ten_pct = self.getTopTen(self.readFile())
        if (self.hits/self.shots)*100 > top_ten_pct[-1]:
            self.highScorePopup(self.shots, self.hits, "Grattis!",
                                "Grattis, du lyckades ta dig in på high-score-listan!\nVar god ange ditt namn i rutan nedanför.")
        else:
            self.highScorePopup(self.shots, self.hits, "Tyvärr..", "Du lyckades tyvärr inte ta dig in på high-score-listan..")
            
    def highScorePopup(self, shots, hits, title, info):
        accuracy = (self.hits/self.shots)*100
        self.popup = Toplevel()
        self.popup.title(title)
        self.popup.configure(background=self.bgcolor)
        self.popup.geometry("+310+250")
        text = Label(
            self.popup, text=info,
            bg=self.bgcolor, fg="darkgreen", font=("terminal", 18)).grid(columnspan=2, sticky=N+S+E+W, ipadx=20, ipady=20)
        if title == "Grattis!":
            name = StringVar()
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
        self.popup.resizable(0,0)
        self.popup.mainloop()

    def exitGame(self):
        winsound.PlaySound(None, winsound.SND_ASYNC)
        root.destroy()

    def restartGame(self, popup):
        popup.destroy()
        self.__init__(root)
            
    def readFile(self):
        text = open("highscores.txt", "r")
        self.info = text.read()
        return self.info

    def getTopTen(self, info):
        hs_list = []
        for entry in info.splitlines():
            entry = entry.split(" | ")
            hs_list.append((entry[0],entry[1]))
        sorted_hs = sorted(hs_list, key=lambda a: float(a[0]), reverse=True)
        top_ten_pct = []
        [top_ten_pct.append(float(sorted_hs[i][0])) for i in range(10)]
        return top_ten_pct

    def buttonMaker(self, win, info="OK", fg="darkgreen", bg="#93C993", font=("terminal", 18)):
        return Button(win, text=info, fg=fg, bg=bg, font=font)
        

    def highScoreEntry(self, accuracy, popup, name):
        hs_list = []
        for entry in self.info.splitlines():
            entry = entry.split(" | ")
            hs_list.append((entry[0],entry[1]))
        if self.cheater == False:
            hs_list.append((accuracy, name.get()))
        else:
            hs_list.append((accuracy, str(name.get())+" (med fusk!)"))
        sorted_hs = sorted(hs_list, key=lambda a: float(a[0]), reverse=True)
        updated_hs = open("highscores.txt", "w+")
        for i in sorted_hs:
            updated_hs.write(str(float(i[0]))+" | "+i[1]+"\n")
        updated_hs.close()
        self.listHighScores(sorted_hs)
        self.popup.destroy()
        
    def listHighScores(self, sorted_hs):
        high_scores = Toplevel()
        high_scores.title("High-score")
        high_scores.configure(background=self.bgcolor)
        high_scores.geometry("+345+110")
        Label(high_scores, text="Topp tio", font=self.terminal_font, fg="darkgreen",
              bg="#93C993").grid(columnspan=2, sticky=N+S+E+W, ipadx=20, ipady=20)
        for i in range(10):
            Label(high_scores, text=str(i+1)+". "+str(float(sorted_hs[i][0]))+"% | "+str(sorted_hs[i][1]), 
                bg=self.bgcolor, fg="darkgreen", font=("terminal", 12)).grid(sticky=N+S+W, ipadx=20, ipady=5, columnspan=2)
        ok = self.buttonMaker(high_scores, "Avsluta")
        ok.configure(command=self.exitGame)
        ok.grid(row=12, column=1, sticky=N+S+E+W, padx=4, pady=4)
        restart = self.buttonMaker(high_scores, "Spela igen")
        restart.configure(command=lambda: self.restartGame(high_scores))
        restart.grid(column=0, row=12, sticky=N+S+E+W, padx=4, pady=4)

    def cheat(self):
        if self.toggle_cheat == True: # Om fusket är påslaget
            for obj in self.placed_ships:
                if obj.status == 1:
                    obj.changeColor("#1789C2") # Dölj skeppen
            self.toggle_cheat = False # Om fusket är avslaget
        else:
            for obj in self.placed_ships:
                if obj.status == 1:
                    obj.changeColor("#8C8C8C") # Visa skeppen
            self.cheater, self.toggle_cheat = True, True

class Box(Game):
    def __init__(self, coords, root, color):
        self.status = 0
        self.coords = coords
        self.order = -1 # Rutor utan skepp får order -1
        self.root = root
        self.button = Button(
            self.root, bg=color,
            activebackground="blue",
            relief=GROOVE, cursor="target",
            command=lambda coords=self.coords, status=self.status: game.fireInTheHole(coords, status)
            )
        self.button.config(width="7",height="3")
        self.button.grid(column=self.coords[0], row=self.coords[1])
        Grid.columnconfigure(self.root,self.coords[0],weight=1)

    def changeColor(self, color):
        self.button.configure(bg=color)

class Ship():
    def __init__(self, ship, coords, direction):
        self.length = ship
        self.direction = direction
        self.coords = coords
        self.hits = 0
        self.adjacent = []
        for i in range(self.length): # Lägg till alla rutor runt omkring skeppet i self.adjacent
            pass
            
        


### Main ###
root=Tk()
game = Game(root)
root.mainloop()
winsound.PlaySound(None, winsound.SND_ASYNC)
############
