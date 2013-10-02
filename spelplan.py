from tkinter import *

class App:
    def __init__(self, master):
        pass

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
##for ruta in knappar:
##    x = (knappar.index(ruta)%10)+1
##    if x==1:
##        y+=1
##    ruta = Button(root)
##    #photo=PhotoImage(file="smiley.gif")
##    ruta.config(width="5",height="2")
##    ruta.grid(column=x, row=y, sticky=E+W+N+S)
##    Grid.columnconfigure(root,x,weight=1)
##    Grid.rowconfigure(root,y,weight=1)

##def color_toggle():
##    if b["bg"]=="lightblue":
##        b["bg"]="red"
##    else:
##        b["bg"]="lightblue"

def color_change(x,y):
    b=Button(root, bg="green", activebackground="blue", relief=GROOVE, command=lambda x=j, y=i: color_change(x,y))
    b.config(width="5",height="2")
    b.grid(column=x, row=y)
    
for i in range(1,11):
    Grid.rowconfigure(root,i,weight=1)
    for j in range(1,11):
        b=Button(root, bg="lightblue", activebackground="blue", relief=GROOVE, command=lambda x=j, y=i: color_change(x,y))
        #photo=PhotoImage(file="smiley.gif")
        b.config(width="5",height="2")
        b.grid(column=j, row=i)
        Grid.columnconfigure(root,j,weight=1)
        #knappar.append(b)

##button=Button(root, bg="yellow")
##button.config(width="5", height="2")
##button.grid(column=5, row=4)
        
        
Label(text="Det här är spelplanen!", bg="lightgreen").grid(columnspan=11, sticky=E+W)
Label(text="Skjut på ruta:").grid(row=13,column=3, columnspan=2, sticky=E)
Entry(root).grid(row=13, column=5, columnspan=3, sticky=W)
root.resizable(0,0)
root.mainloop()


