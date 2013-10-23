from tkinter import *
import time

class Game:
    def __init__(self, root):
        root.title("Sänka Skepp")
        Grid.rowconfigure(root,0,weight=1)
        Grid.columnconfigure(root,0,weight=1)
        bokstav = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
        
        for k in range(10):
            column = Label(text=bokstav[k], fg="darkgreen", bg="lightgreen").grid(column=k+1, row=0, sticky=N+S+E+W)
        utfyllnad = Label(text="", bg="lightgreen").grid(column=0, row=0, sticky=N+S+E+W)
        for r in range(1,11):
            row = Label(text=r, fg="darkgreen", bg="lightgreen").grid(column=0, row=r, sticky=N+S+E+W)
            
class Box(Game):
    def __init__(self, parent, coords, root, ship):
        self.status = 0
        self.coords = coords
        self.ship = ship
        self.SHIP = [5,4,3,3,2]
        self.root = root
        
    def createBox(self, parent, ship):
        b=Button(
            root, bg="lightblue",
            #activebackground="blue",
            relief=GROOVE,
            command=lambda x=self.coords[0], y=self.coords[1], ship=self.ship: directionPopup(x,y, ship, self.SHIP[ship[0]])
            )
        b.config(width="5",height="2")
        b.grid(column=self.coords[0], row=self.coords[1])
        Grid.columnconfigure(self.root,self.coords[0],weight=1)

def createGrid():
    ship = [0]
    box_list = []
    for i in range(1,11):
        row = []
        for j in range(1,11):
            coords = (i,j)
            box = Box(Game, coords, root, ship)
            row.append(box)
            box.createBox(Game, ship)
        box_list.append(row)
    label = Label(text="Placera ut dina skepp på spelplanen ovan.", bg="lightgreen").grid(columnspan=11, sticky=E+W)
    root.resizable(0,0)
    return box_list

def directionPopup(x,y, ship, length):
    win = Toplevel()
    win.title("Riktning")
    text = Label(
        win, text="Vill du placera skeppet vertikalt (nedåt) eller horisontellt (åt höger)?",
        bg="lightgreen", fg="darkgreen").grid(columnspan=2, sticky=N+S+E+W, ipadx=20, ipady=20)
    vert = Button(
        win, text="Vertikalt",
        command=lambda direction="v", pos=[x,y]: returnDir(direction, win, pos, length, ship)
        )
    vert.grid(column=0, row=1, sticky=E+W)
    hori = Button(
        win, text="Horisontellt",
        command=lambda direction="h", pos=[x,y]: returnDir(direction, win, pos, length, ship)
        )
    hori.grid(column=1, row=1, sticky=E+W)
    win.mainloop()

def returnDir(direction, win, pos, length, ship):
    if direction == "h":
        if (pos[0]+length)<=11:
            placeShip(pos[0], pos[1], length, direction, box_list, ship)
        else:
            err = messagebox.showinfo("Felaktig placering!", "Placeringen du har valt är felaktig, försök igen!")
    elif direction == "v":
        if pos[1]+length<=11:
            placeShip(pos[0], pos[1], length, direction, box_list, ship)
        else:
            err = messagebox.showinfo("Felaktig placering!", "Placeringen du har valt är felaktig, försök igen!")
    win.destroy()

def placeShip(x, y, length, direction, box_list, ship):
    overlap=0
    if direction == "h":
        for j in range(length):
            if box_list[y-1][x+j-1].status != 0:
                overlap = 1
        if overlap<1:  
            for i in range(length):
                b=Button(
                    root, bg="green",
                    relief=GROOVE
                    )
                b.config(width="5",height="2")
                b.grid(column=x+i, row=y)
                time.sleep(0.01)
                root.update()
                box_list[y-1][x+i-1].status = 1
            ship[0] += 1
        else:
            err = messagebox.showinfo("Felaktig placering!", "Placeringen du har valt överlappar ett av dina skepp, försök igen!")
    elif direction=="v":
        for j in range(length):
            if box_list[y+j-1][x-1].status != 0:
                overlap = 1
        if overlap<1:
            for i in range(length):
                b=Button(
                    root, bg="green",
                    relief=GROOVE
                    )
                b.config(width="5",height="2")
                b.grid(column=x, row=y+i)
                time.sleep(0.01)
                root.update()
                box_list[y+i-1][x-1].status = 1
            ship[0] += 1
                #Label(text="", bg="lightgreen").grid(row=11, columnspan=11, sticky=E+W)
        else:
            err = messagebox.showinfo("Felaktig placering!", "Placeringen du har valt överlappar ett av dina skepp, försök igen!")


#################################
root=Tk()
Game(root)

box_list = createGrid()





##def createBoard():
##    SHIP = [5,4,3,3,2]
##    ship=[0]
##    for i in range(1,11):
##        Grid.rowconfigure(root,i,weight=1)
##        for j in range(1,11):
##            b=Button(
##                root, bg="lightblue",
##                #activebackground="blue",
##                relief=GROOVE,
##                command=lambda x=j, y=i, ship=ship: directionPopup(x,y, ship, SHIP[ship[0]])
##                )
##            b.config(width="5",height="2")
##            b.grid(column=j, row=i)
##            Grid.columnconfigure(root,j,weight=1)
##            #knappar.append(b)
##                   
##    Label(text="Placera ut dina skepp på spelplanen ovan.", bg="lightgreen").grid(columnspan=11, sticky=E+W)
##    #Label(text="Skjut på ruta:").grid(row=13,column=3, columnspan=2, sticky=E)
##    #Entry(root).grid(row=13, column=5, columnspan=3, sticky=W)
##    root.resizable(0,0)



##def color_change(x,y,b,spread):
##    if b["bg"]=="lightblue":
##        c = "lb"
##        spread(x,y,b,c)
##        b=Button(
##            root, bg="green",
##            activebackground="blue",
##            relief=GROOVE,
##            command=lambda x=x, y=y: color_change(x,y,b)
##            )
##    else:
##        c = "gr"
##        spread(x,y,b,c)
##        b=Button(
##            root, bg="lightblue",
##            activebackground="blue",
##            relief=GROOVE,
##            command=lambda x=x, y=y: color_change(x,y,b,spread)
##            )
##    b.config(width="5",height="2")
##    b.grid(column=x, row=y)
##def spread(x,y,b,c):
##    if c=="lb":
##        
##        for i in range(10):
##            b=Button(
##                root, bg="green",
##                #activebackground="blue",
##                relief=GROOVE,
##                command=lambda x=i+1, y=y: color_change(x,y,b,spread)
##                )
##            b.config(width="5",height="2")
##            b.grid(column=i+1, row=y)
##            time.sleep(0.01)
##            root.update()
##            
##        for j in range(10):
##            b=Button(
##                root, bg="green",
##                #activebackground="blue",
##                relief=GROOVE,
##                command=lambda x=x, y=j+1: color_change(x,y,b,spread)
##                )
##            b.config(width="5",height="2")
##            b.grid(column=x, row=j+1)
##            time.sleep(0.01)
##            root.update()
##    else:
##        for i in range(10):
##            b=Button(
##                root, bg="lightblue",
##                #activebackground="blue",
##                relief=GROOVE,
##                command=lambda x=i+1, y=y: color_change(x,y,b,spread)
##                )
##            b.config(width="5",height="2")
##            b.grid(column=i+1, row=y)
##            time.sleep(0.01)
##            root.update()
##            
##        for j in range(10):
##            b=Button(
##                root, bg="lightblue",
##                #activebackground="blue",
##                relief=GROOVE,
##                command=lambda x=x, y=j+1: color_change(x,y,b,spread)
##                )
##            b.config(width="5",height="2")
##            b.grid(column=x, row=j+1)
##            time.sleep(0.01)
##            root.update()
