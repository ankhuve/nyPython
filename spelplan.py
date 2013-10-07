from tkinter import *
import time

class App:
    def __init__(self):
        self.SKEPP = [5,4,3,3,2]
        self.placering = placering
        
        

root=Tk()
root.title("Sänka Skepp")
Grid.rowconfigure(root,0,weight=1)
Grid.columnconfigure(root,0,weight=1)
knappar = []
bokstav = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
##for i in bokstav:
##    for j in range(1,11):
##        knappar.append(i+str(j))
##    #knappar.append(li)
##print(knappar)


for k in range(10):
    column = Label(text=bokstav[k], fg="darkgreen", bg="lightgreen").grid(column=k+1, row=0, sticky=N+S+E+W)
utfyllnad = Label(text="", bg="lightgreen").grid(column=0, row=0, sticky=N+S+E+W)
for r in range(1,11):
    row = Label(text=r, fg="darkgreen", bg="lightgreen").grid(column=0, row=r, sticky=N+S+E+W)
y=0

def spread(x,y,b,c):
    if c=="lb":
        
        for i in range(10):
            b=Button(
                root, bg="green",
                #activebackground="blue",
                relief=GROOVE,
                command=lambda x=i+1, y=y: color_change(x,y,b,spread)
                )
            b.config(width="5",height="2")
            b.grid(column=i+1, row=y)
            time.sleep(0.01)
            root.update()
            
        for j in range(10):
            b=Button(
                root, bg="green",
                #activebackground="blue",
                relief=GROOVE,
                command=lambda x=x, y=j+1: color_change(x,y,b,spread)
                )
            b.config(width="5",height="2")
            b.grid(column=x, row=j+1)
            time.sleep(0.01)
            root.update()
    else:
        for i in range(10):
            b=Button(
                root, bg="lightblue",
                #activebackground="blue",
                relief=GROOVE,
                command=lambda x=i+1, y=y: color_change(x,y,b,spread)
                )
            b.config(width="5",height="2")
            b.grid(column=i+1, row=y)
            time.sleep(0.01)
            root.update()
            
        for j in range(10):
            b=Button(
                root, bg="lightblue",
                #activebackground="blue",
                relief=GROOVE,
                command=lambda x=x, y=j+1: color_change(x,y,b,spread)
                )
            b.config(width="5",height="2")
            b.grid(column=x, row=j+1)
            time.sleep(0.01)
            root.update()
        

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
    
for i in range(1,11):
    Grid.rowconfigure(root,i,weight=1)
    for j in range(1,11):
        b=Button(
            root, bg="lightblue",
            #activebackground="blue",
            relief=GROOVE,
            command=lambda x=j, y=i: color_change(x,y,b,spread)
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


