from tkinter import *
import random

class Game:
    def __init__(self, root, box_list):
        self.SHIPS = [5,4,3,3,2]
        self.shots = 0
        self.hits = 0
        self.toggle_cheat = False
        self.placed_ships = []
        root.title("Sänka Skepp")
        Grid.rowconfigure(root,0,weight=1)
        Grid.columnconfigure(root,0,weight=1)
        columns = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
        

##        self.cheatbutton = Button(root, bg="lightgreen", command=self.cheat(placed_ships))
##        self.cheatbutton.config(width="5", height="1")
##        self.cheatbutton.grid(column=9, row=11)
        
        for c in range(10):
            Label(text=columns[c], fg="darkgreen", bg="#95E895").grid(column=c+1, row=0, sticky=N+S+E+W)
        Label(text="", bg="#95E895").grid(column=0, row=0, sticky=N+S+E+W)
        for r in range(1,11):
            Label(text=r, fg="darkgreen", bg="#95E895").grid(column=0, row=r, sticky=N+S+E+W)
        self.randomizeShipPlacement(box_list, self.placed_ships)
            
    def randomizeShipPlacement(self, box_list, placed_ships):
        ##placed_ships = []
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
        self.createCheatButton(placed_ships)
##        for obj in placed_ships:
##            obj.changeColor("grey") # Fusk!
##            #print(obj.coords)
##            pass
        
    def controlPlacement(self, box_list, ship):
        control = False
        while control == False:
            start = random.choice(box_list[random.randint(0,9)])
            x = start.coords[0]
            y = start.coords[1]
            direction = random.choice(["h", "v"])
            try:
                for i in range(ship):
                    if direction == "h":
                        if box_list[x-1+i][y-1].status != 0:
                            control = False
                            break
                        else:
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
##                                print("    ",box_list[x-1+i][y-2].status,"\n",
##                                      box_list[x-2+i][y-1].status,box_list[x-1+i][y-1].coords,box_list[x+i][y-1].status,"\n",
##                                      "   ",box_list[x-1+i][y].status)
                                if (
                                    box_list[x-2+i][y-1].status != 0 # vänster
                                    or box_list[x-1+i][y-2].status != 0 # ovanför
                                    or box_list[x+i][y-1].status != 0 # höger
                                    or box_list[x-1+i][y].status != 0 # under
                                    ):
                                    control = False
                                    break
                                else:
                                    control = True
                        elif direction == "v":
                            for i in range(ship):
##                                print("    ",box_list[x-1][y-2+i].status,"\n",
##                                      box_list[x-2][y-1+i].status,box_list[x-1][y-1+i].coords,box_list[x][y-1+i].status,"\n",
##                                      "   ",box_list[x-1][y+i].status)
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

    def fireInTheHole(self, coords, status):
        if box_list[coords[0]-1][coords[1]-1].status == 1:
            box_list[coords[0]-1][coords[1]-1].status = 3
            box_list[coords[0]-1][coords[1]-1].changeColor("red")
            self.hits += 1
            self.shots += 1
        elif box_list[coords[0]-1][coords[1]-1].status == 0:
            box_list[coords[0]-1][coords[1]-1].status = 2
            box_list[coords[0]-1][coords[1]-1].changeColor("white")
            self.shots += 1
        else:
            pass
        self.updateStats(self.shots, self.hits)
        if self.hits==(17):
            self.endGame()
            ##self.highScorePopup(self.shots, self.hits)
            root.destroy()
            
    def updateStats(self, shots, hits):
        try:
            accuracy = (self.hits/self.shots)*100
        except ZeroDivisionError:
            accuracy = 1
        Label(text=str(accuracy)[:4]+"%", fg="darkgreen", bg="#95E895").grid(row=12, column=4, sticky=E+W+N+S)
        Label(text=str(self.shots), fg="darkgreen", bg="#95E895").grid(row=12, column=9, sticky=E+W+N+S)
            
    def endGame(self):
        self.high_scores = self.readFile()
        self.high_scores.seek(0)
        hs_list = self.high_scores.read()
        for line in hs_list:
            entries = line.split("\n")
        print(entries)
        self.highScorePopup(self.shots, self.hits)
            
    def readFile(self):
        read = False
        while read != True:
            try:
                high_scores = open("highscores.txt", "a+")
                read = True
            except IOError:
                print("High-score-listan gick inte att läsa in. Försök igen!")
        return high_scores

    def highScorePopup(self, shots, hits):
        accuracy = (self.hits/self.shots)*100
        popup = Toplevel()
        popup.title("Grattis!")
        text = Label(
            popup, text="Grattis, du lyckades ta dig in på high-score-listan!\nVar god ange ditt namn i rutan nedanför.",
            bg="lightgreen", fg="darkgreen").grid(columnspan=2, sticky=N+S+E+W, ipadx=20, ipady=20)
        entry = Entry(popup).grid(row=3, sticky=E+W+N+S)
        ok_button = Button(
            popup, text="OK!", fg="darkgreen", bg="lightgreen",
            command=lambda name=entry.get(), accuracy=str(accuracy)[:4]: self.highScoreEntry(name, accuracy, popup, self.high_scores)
            )
        ok_button.grid(column=1, row=3, sticky=E+W)
        popup.mainloop()

    def highScoreEntry(self, name, accuracy, popup, hs_list):
        self.high_scores.write(name+"|"+accuracy)
        popup.destroy()
            
    def createCheatButton(self, placed_ships):
        self.cheatbutton = Button(
            root, text="fuska lite..",fg="#95E895", bg="#95E895", relief=FLAT,
            command=lambda: self.cheat(self.placed_ships, self.toggle_cheat)
            )
        self.cheatbutton.config(width="7", height="1")
        self.cheatbutton.grid(column=9, columnspan=2, row=11)

    def cheat(self, placed_ships, toggle_cheat):
        if self.toggle_cheat == True:
            for obj in placed_ships:
                if obj.status == 1:
                    obj.changeColor("lightblue") # Dölj skeppen
            self.toggle_cheat = False
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
            relief=GROOVE,
            command=lambda coords=self.coords, status=self.status: game.fireInTheHole(coords, status)
            )
        self.button.config(width="5",height="2")
        self.button.grid(column=self.coords[0], row=self.coords[1])
        Grid.columnconfigure(self.root,self.coords[0],weight=1)

    def changeColor(self, color):
        self.button.configure(bg=color)

def createGrid():
    box_list = []
    for i in range(1,11):
        row = []
        for j in range(1,11):
            coords = (i,j)
            row.append(Box(coords, root, "lightblue"))
        box_list.append(row)
    Label(text="Klicka på rutorna ovan för att skjuta!", fg="darkgreen", bg="#95E895").grid(columnspan=11, sticky=E+W+N+S)
    Label(text="Pricksäkerhet:", fg="darkgreen", bg="#95E895").grid(column=0, columnspan=5, sticky=E+W+S+N)
    Label(text="Antal försök:", fg="darkgreen", bg="#95E895").grid(column=5, row=12, columnspan=6, sticky=E+W+S+N)
    root.resizable(0,0)
    return box_list

root=Tk()
box_list = createGrid()
game = Game(root, box_list)


