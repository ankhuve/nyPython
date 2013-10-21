from tkinter import *
class Box:
    def __init__(self, coords):
        self.status = 0
        self.coords = coords
        self.ship = [0]
        self.SHIP = [5,4,3,3,2]
        
    def createBox(self):
        b=Button(
            root, bg="lightblue",
            #activebackground="blue",
            relief=GROOVE,
            command=lambda x=self.coords[0], y=self.coords[1], ship=self.ship: directionPopup(x,y, ship, self.SHIP[ship[0]])
            )
        b.config(width="5",height="2")
        b.grid(column=coords[0], row=coords[1])
        Grid.columnconfigure(root,coords[0],weight=1)


li = []
root = Tk()
for i in range(1,11):
    temp = []
    for j in range(1,11):
        coords = (i,j)
        box = Box(coords)
        temp.append(box)
        box.createBox()
    li.append(temp)


