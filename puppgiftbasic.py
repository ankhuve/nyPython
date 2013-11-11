from tkinter import *
import random

class Game:
    def __init__(self, root, box_list):
        self.SHIPS = [5,4,3,3,2]
        root.title("Sänka Skepp")
        Grid.rowconfigure(root,0,weight=1)
        Grid.columnconfigure(root,0,weight=1)
        bokstav = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
        self.hits = 0
        
        for k in range(10):
            column = Label(text=bokstav[k], fg="darkgreen", bg="lightgreen").grid(column=k+1, row=0, sticky=N+S+E+W)
        utfyllnad = Label(text="", bg="lightgreen").grid(column=0, row=0, sticky=N+S+E+W)
        for r in range(1,11):
            row = Label(text=r, fg="darkgreen", bg="lightgreen").grid(column=0, row=r, sticky=N+S+E+W)
        self.randomizeShipPlacement(box_list)
        
    def randomizeShipPlacement(self, box_list):
        placed_ships = []
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
        for obj in placed_ships:
            #obj.changeColor("grey") # Fusk!
            #print(obj.coords)
            pass
        
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
                        print(box_list[x-1+i][y-1].coords)
                        if box_list[x-1+i][y-1].status != 0:
                            control = False
                            break
                        else:
                            control = True
                    elif direction == "v":
                        print(box_list[x-1][y-1+i].coords)
                        if box_list[x-1][y-1+i].status != 0:
                            control = False
                            break
                        else:
                            control = True
                if control == True: ## Kolla runt omkring skeppet
                    try:
                        if direction == "h":
                            for i in range(ship):
                                print("    ",box_list[x-1+i][y-2].status,"\n",
                                      box_list[x-2+i][y-1].status,box_list[x-1+i][y-1].coords,box_list[x+i][y-1].status,"\n",
                                      "   ",box_list[x-1+i][y].status)
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
                                print("    ",box_list[x-1][y-2+i].status,"\n",
                                      box_list[x-2][y-1+i].status,box_list[x-1][y-1+i].coords,box_list[x][y-1+i].status,"\n",
                                      "   ",box_list[x-1][y+i].status)
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
                        print("utanför spelplan runtom")
                        return False, direction, x, y
                return control, direction, x, y
            except IndexError:
                print("utanför spelplan!")
                return False, direction, x, y

    def fireInTheHole(self, coords, status):
        print(coords)
        print(box_list[coords[0]-1][coords[1]-1].status)
        if box_list[coords[0]-1][coords[1]-1].status == 1:
            box_list[coords[0]-1][coords[1]-1].status = 3
            box_list[coords[0]-1][coords[1]-1].changeColor("red")
            self.hits += 1
        else:
            box_list[coords[0]-1][coords[1]-1].status = 2
            box_list[coords[0]-1][coords[1]-1].changeColor("white")
        if self.hits==(17):
            root.destroy()
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
    label = Label(text="Klicka på rutorna ovan för att skjuta!", bg="lightgreen").grid(columnspan=11, sticky=E+W)
    root.resizable(0,0)
    return box_list

root=Tk()
box_list = createGrid()
game = Game(root, box_list)


