from tkinter import *
import random

class Game:
    def __init__(self, root):
        self.SHIPS = [5,4,3,3,2]
        self.shots = 0
        self.hits = 0
        self.toggle_cheat = False
        self.placed_ships = []
        root.title("Sänka Skepp")
        self.box_list = self.createGrid()
        self.randomizeShipPlacement(self.box_list, self.placed_ships)

    def createGrid(self):
        Grid.rowconfigure(root,0,weight=1)
        Grid.columnconfigure(root,0,weight=1)
        columns = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]        
        for c in range(10):
            Label(text=columns[c], fg="darkgreen", bg="#95E895").grid(column=c+1, row=0, sticky=N+S+E+W)
        Label(text="", bg="#95E895").grid(column=0, row=0, sticky=N+S+E+W)
        for r in range(1,11):
            Label(text=r, fg="darkgreen", bg="#95E895").grid(column=0, row=r, sticky=N+S+E+W)
        box_list = []
        for i in range(1,11):
            row = []
            for j in range(1,11):
                coords = (i,j)
                row.append(Box(coords, root, "lightblue"))
            box_list.append(row)
        Label(text="Klicka på rutorna ovan för att skjuta!", fg="darkgreen", bg="#95E895").grid(row=11, columnspan=11, sticky=E+W+S+N)
        Label(text="Pricksäkerhet:", fg="darkgreen", bg="#95E895").grid(row=12, column=0, columnspan=5, sticky=E+W+S+N)
        Label(text="Antal försök:", fg="darkgreen", bg="#95E895").grid(row=12, column=5, columnspan=6, sticky=E+W+S+N)
        root.resizable(0,0)
        self.createCheatButton(self.placed_ships)
        return box_list
            
    def randomizeShipPlacement(self, box_list, placed_ships):
        for ship in self.SHIPS:
            placement_check = False
            while placement_check != True:
                placement_check, direction, x, y = self.controlPlacement(box_list, ship)
            if direction == "h":
                for n in range(ship):
                    box_list[x-1+n][y-1].status = 1
                    placed_ships.append(box_list[x-1+n][y-1])
            elif direction == "v":
                for n in range(ship):
                    box_list[x-1][y-1+n].status = 1
                    placed_ships.append(box_list[x-1][y-1+n])
        
    def controlPlacement(self, box_list, ship):
        control = False
        while control == False:
            start = random.choice(box_list[random.randint(0,9)])
            x = start.coords[0]
            y = start.coords[1]
            direction = random.choice(["h", "v"])
            try:
                for i in range(ship): ## Kolla om det kommer överlappa
                    if direction == "h":
                        if box_list[x-1+i][y-1].status != 0:
                            control = False
                            break
                        else:                       # MÅSTE SNYGGAS TILL FÖR FAN
                            control = True
                    elif direction == "v":
                        if box_list[x-1][y-1+i].status != 0:
                            control = False
                            break
                        else:
                            control = True
                if control == True: ## Kolla runt omkring skeppet
                    try:
                        
                        if direction == "h":
                            for i in range(ship):
                                if (
                                    box_list[x-2+i][y-1].status != 0 # vänster
                                    or box_list[x-1+i][y-2].status != 0 # ovanför
                                    or box_list[x+i][y-1].status != 0 # höger       
                                    or box_list[x-1+i][y].status != 0 # under
                                    ):
                                    control = False
                                    break
                                else:                                   # MÅSTE SNYGGAS TILL FÖR FAN
                                    control = True
                        elif direction == "v":
                            for i in range(ship):
                                check = controlBorders(direction)
                                if (
                                    box_list[x-2][y-1+i].status != 0 # vänster
                                    or box_list[x-1][y-2+i].status != 0 # ovanför
                                    or box_list[x][y-1+i].status != 0 # höger
                                    or box_list[x-1][y+i].status != 0 # under
                                    ):
                                    control = False
                                    break
                                else:
                                    control = True
                    except IndexError:
                        return False, direction, x, y
                return control, direction, x, y
            except IndexError:
                return False, direction, x, y
##    def controlBorders(self, direction):   EXPERIMENTELLT
##        if direction == "h":
##            check_list = [(x-2+i, y-1),(x-1+i, y-2),(x+i, y-1),(x-1+i, y)]
##        elif direction == "v":
##            check_list = [(x-2, y-1+i),(x-1, y-2+i),(x, y-1+i),(x-1, y+i)]
##
##        for i in range(ship):
##            for i in check_list:
##                if box_list[i[0]][i[1]].status != 0:
##                    control = False
##                    break
##        
##        return check_list
        

    def fireInTheHole(self, coords, status, box_list):
        box = box_list[coords[0]-1][coords[1]-1]
        if box.status == 1:
            box.status = 3
            box.changeColor("red")
            self.hits += 1
            self.shots += 1
        elif box.status == 0:
            box.status = 2
            box.changeColor("white")
            self.shots += 1
        else:
            pass
        self.updateStats(self.shots, self.hits)
        if self.hits==(17):
            self.endGameCheck()
            
    def updateStats(self, shots, hits):
        try:
            accuracy = (self.hits/self.shots)*100
        except ZeroDivisionError:
            accuracy = 1
        Label(text=str(accuracy)[:4]+"%", fg="darkgreen", bg="#95E895").grid(row=12, column=4, sticky=E+W+N+S)
        Label(text=str(self.shots), fg="darkgreen", bg="#95E895").grid(row=12, column=9, sticky=E+W+N+S)
            
    def endGameCheck(self):
        top_ten_pct = self.getTopTen(self.readFile())
        print(top_ten_pct)
        if (self.hits/self.shots)*100 > top_ten_pct[-1]:
            self.highScorePopup(self.shots, self.hits)
        else:
            print("Du kvalade inte till high-scoren....")
            self.exitGame()

    def exitGame(self):
        root.destroy()

    def restartGame(self, high_scores):
        high_scores.destroy()
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
        return top_ten_pct # Kanske kan returnera sorted_hs istället och ta [10] vid kontrollen?

    def highScorePopup(self, shots, hits):
        accuracy = (self.hits/self.shots)*100
        self.popup = Toplevel()
        self.popup.title("Grattis!")
        text = Label(
            self.popup, text="Grattis, du lyckades ta dig in på high-score-listan!\nVar god ange ditt namn i rutan nedanför.",
            bg="lightgreen", fg="darkgreen", font=("", 12)).grid(columnspan=2, sticky=N+S+E+W, ipadx=20, ipady=20)
        name = StringVar()
        entry = Entry(self.popup, textvariable=name).grid(row=3, sticky=E+W+N+S)
        
        ok_button = Button(
            self.popup, text="OK!", fg="darkgreen", bg="lightgreen",
            command=lambda accuracy=str(accuracy)[:4]: self.highScoreEntry(accuracy, self.popup, name)
            )
        ok_button.grid(column=1, row=3, sticky=E+W)
        self.popup.resizable(0,0)
        self.popup.mainloop()

    def highScoreEntry(self, accuracy, popup, name):
        hs_list = []
        for entry in self.info.splitlines():
            entry = entry.split(" | ")
            hs_list.append((entry[0],entry[1]))
        hs_list.append((accuracy, name.get()))
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
        high_scores.configure(background="lightgreen")
        Label(high_scores, text="Topp tio", font=("Verdana", 16), fg="darkgreen", bg="#81C981").grid(columnspan=2, sticky=N+S+E+W, ipadx=20, ipady=20)
        for i in range(10):
            Label(
                high_scores, text=str(i+1)+". "+str(float(sorted_hs[i][0]))+"% | "+str(sorted_hs[i][1]), 
                bg="#95E895", fg="darkgreen", font=("", 10)).grid(sticky=N+S+W, ipadx=20, columnspan=2)
        ok = Button(
            high_scores, text="Avsluta", fg="darkgreen", bg="#81C981",
            command=self.exitGame
            ).grid(row=12, column=1, sticky=N+S+E+W, padx=4, pady=4)
        play_again = Button(
            high_scores, text="Spela igen", fg="darkgreen", bg="#81C981",
            command=lambda: self.restartGame(high_scores)
            )
        play_again.grid(column=0, row=12, sticky=N+S+E+W, padx=4, pady=4)
        
    def createCheatButton(self, placed_ships):
        self.cheatbutton = Button(
            root, text="fuska lite..",fg="#95E895", bg="#95E895", relief=FLAT,
            command=lambda: self.cheat(self.placed_ships, self.toggle_cheat)
            )
        self.cheatbutton.config(width="7", height="1")
        self.cheatbutton.grid(column=9, columnspan=2, row=11)

    def cheat(self, placed_ships, toggle_cheat):
        if self.toggle_cheat == True: # Om fusket är påslaget
            for obj in placed_ships:
                if obj.status == 1:
                    obj.changeColor("lightblue") # Dölj skeppen
            self.toggle_cheat = False # Om fusket är avslaget
        else:
            for obj in placed_ships:
                if obj.status == 1:
                    obj.changeColor("grey") # Visa skeppen
            self.toggle_cheat = True

class Box(Game):
    def __init__(self, coords, root, color):
        self.status = 0
        self.coords = coords
        self.root = root
        self.button = Button(
            root, bg=color,
            activebackground="blue",
            relief=GROOVE, cursor="target",
            command=lambda coords=self.coords, status=self.status: game.fireInTheHole(coords, status, game.box_list)
            )
        self.button.config(width="5",height="2")
        self.button.grid(column=self.coords[0], row=self.coords[1])
        Grid.columnconfigure(self.root,self.coords[0],weight=1)

    def changeColor(self, color):
        self.button.configure(bg=color)

root=Tk()
game = Game(root)
