from tkinter import *
import time
SKEPP = [5,4,3,3,2]
#ship = 0
class App:
    def __init__(self):
        self.SKEPP = [5,4,3,3,2]
        self.placering = placering
        pass
        

root=Tk()
root.title("Sänka Skepp")
Grid.rowconfigure(root,0,weight=1)
Grid.columnconfigure(root,0,weight=1)
occupied = []
bokstav = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]

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
            placeraSkepp(pos[0], pos[1], length, direction, occupied, ship)
        else:
            err = messagebox.showinfo("Felaktig placering!", "Placeringen du har valt är felaktig, försök igen!")
    elif direction == "v":
        if pos[1]+length<=11:
            placeraSkepp(pos[0], pos[1], length, direction, occupied, ship)
        else:
            err = messagebox.showinfo("Felaktig placering!", "Placeringen du har valt är felaktig, försök igen!")
    win.destroy()

for k in range(10):
    column = Label(text=bokstav[k], fg="darkgreen", bg="lightgreen").grid(column=k+1, row=0, sticky=N+S+E+W)
utfyllnad = Label(text="", bg="lightgreen").grid(column=0, row=0, sticky=N+S+E+W)
for r in range(1,11):
    row = Label(text=r, fg="darkgreen", bg="lightgreen").grid(column=0, row=r, sticky=N+S+E+W)
y=0

def placeraSkepp(x,y,length,direction,occupied,ship):
    overlap=0
    if direction == "h":
        for j in range(length):
            if str(x+j)+str(y) in occupied:
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
                occupied.append(str(x+i)+str(y))
            ship += 1
            print(ship)
        else:
            err = messagebox.showinfo("Felaktig placering!", "Placeringen du har valt överlappar ett av dina skepp, försök igen!")

    elif direction=="v":
        for j in range(length):
            if str(x)+str(y+j) in occupied:
                overlap = 1
        if overlap<1:
            for j in range(length):
                if (str(x)+str(y+j)) in occupied:
                    overlap = True
                else:
                    overlap = False
            if overlap == False:
                for i in range(length):
                    b=Button(
                        root, bg="green",
                        relief=GROOVE
                        )
                    b.config(width="5",height="2")
                    b.grid(column=x, row=y+i)
                    time.sleep(0.01)
                    root.update()
                    occupied.append(str(x)+str(y+i))
                ship+=1
                print(ship)
        else:
            err = messagebox.showinfo("Felaktig placering!", "Placeringen du har valt överlappar ett av dina skepp, försök igen!")
def color_change(x,y,b,spread):
    if b["bg"]=="lightblue":
        c = "lb"
        spread(x,y,b,c)
##        b=Button(
##            root, bg="green",
##            activebackground="blue",
##            relief=GROOVE,
##            command=lambda x=x, y=y: color_change(x,y,b)
##            )
    else:
        c = "gr"
        spread(x,y,b,c)
##        b=Button(
##            root, bg="lightblue",
##            activebackground="blue",
##            relief=GROOVE,
##            command=lambda x=x, y=y: color_change(x,y,b,spread)
##            )
##    b.config(width="5",height="2")
##    b.grid(column=x, row=y)

def createBoard(SKEPP):
    ship=0
    for i in range(1,11):
        Grid.rowconfigure(root,i,weight=1)
        for j in range(1,11):
            b=Button(
                root, bg="lightblue",
                #activebackground="blue",
                relief=GROOVE,
                command=lambda x=j, y=i, ship=ship: directionPopup(x,y, ship, SKEPP[ship])
                )
            #photo=PhotoImage(file="smiley.gif")
            b.config(width="5",height="2")
            b.grid(column=j, row=i)
            Grid.columnconfigure(root,j,weight=1)
            #knappar.append(b)
                   
    Label(text="Det här är spelplanen!", bg="lightgreen").grid(columnspan=11, sticky=E+W)
    #Label(text="Skjut på ruta:").grid(row=13,column=3, columnspan=2, sticky=E)
    #Entry(root).grid(row=13, column=5, columnspan=3, sticky=W)
    root.resizable(0,0)

createBoard(SKEPP)

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
