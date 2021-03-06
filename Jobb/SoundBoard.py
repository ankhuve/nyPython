from tkinter import *; import string; import winsound
class SoundBoard:
    GRIDSIZE = 6 # 10 är standard. Går att välja tal mellan 10 och 26 (längden av engelska alfabetet)
    def __init__(self, root):
        """ Konstruktor, bestämmer variabler och kör igång createGrid, outerPlacementControl och sätter igång spelmusiken. 
        Inparameter är rotfönstret. """
        self.BGCOLOR = "#689E68" # Standardbakgrundsfärg för rutor.
        self.STD_FONT = ("Verdana", 18) # Standardfont för text i rutor.
        self.sound_list = ["hearsomething.wav", "fellowscientist.wav", "hearsomething.wav"]
        self.root = root # Rotfönstret.
        self.root.title("Sound Board") # Rotfönstrets titel.
        self.root.geometry("+10+10") # Rotfönstrets placering.
        self.createGrid()
        
    def createGrid(self):
        """ Skapar det grafiska rutnätet av knappar, koordinater och text samt skapar fuskknappen (döljs nere i det högra hörnet). """
        COLUMNS = list(string.ascii_uppercase) # Lista med alfabetet
        Label(text="", bg=self.BGCOLOR).grid(column=0, row=0, sticky=N+S+E+W)
        [Label(text="Kolumn "+str(c+1), fg="darkgreen", bg=self.BGCOLOR, font=self.STD_FONT).grid(column=c+1, row=0, sticky=N+S+E+W) for c in range(len(self.sound_list))] # Kolumner
        [Label(text="Rad "+str(r), fg="darkgreen", bg=self.BGCOLOR, font=self.STD_FONT).grid(column=0, row=r, sticky=N+S+E+W) for r in range(1,len(self.sound_list)+1)] # Rader
        button = Button(
            self.root, bg="darkred",
            text="Stoppa ljud",
            font=("Verdana", 13),
            activebackground="gray",
            relief=GROOVE,
            command=lambda: stopSound(self)
            )
        button.config(width="2",height="3")
        button.grid(column=1, row=3, columnspan=3, sticky=N+S+E+W)
        #Grid.columnconfigure(self.root,weight=1)
        for i in range(1,len(self.sound_list)+1):
            row = [] # Lista som skapas för varje rad.
            for j in range(1,len(self.sound_list)):
                coords = (i,j) # Koordinater på spelfältet, från 1 till GRIDSIZE.
                row.append(SoundButton(self, coords, self.root, "#1789C2", self.sound_list[j]))
        self.makeMuteButton()
        self.root.resizable(0,0)

    def makeMuteButton(self):
        button = Button(
            self.root, bg="darkred",
            text="Stoppa ljud",
            font=("Verdana", 13),
            activebackground="gray",
            relief=GROOVE,
            command=lambda: stopSound(self)
            )
        button.config(width="2",height="3")
        button.grid(column=1, row=3, columnspan=3, sticky=N+S+E+W)
            
    def buttonMaker(self, win, info="OK", fg="darkgreen", bg="#93C993", font=("Arial", 18)):
        """ Metod för att skapa knappar.
        Inparametrar är vilket fönster knappen ska finnas i, vad som ska stå på knappen och med vilken textfärg, bakgrundsfärg och font.
        Returnerar knappen. """
        return Button(win, text=info, fg=fg, bg=bg, font=font)
    
class SoundButton(SoundBoard):
    def __init__(self, parent, coords, root, color, sound):
        """ Konstruktor, bestämmer variabler och skapar knappen.
        Inparametrar är rutans koordinater, rotfönstret samt rutans färg. """
        self.coords = coords # Rutans koordinater.
        self.root = root # Rotfönstret.
        self.color = color
        self.button = Button(
            self.root, bg=self.color,
            text="Testljud "+str(coords[1]),
            font=("Verdana", 13),
            activebackground="gray",
            relief=GROOVE,
            command=lambda: playSound(self, sound)
            )
        self.button.config(width="10",height="3", padx="20", pady ="10")
        self.button.grid(column=self.coords[0], row=self.coords[1])
        Grid.columnconfigure(self.root,self.coords[0],weight=1)

    def changeColor(self, color):
        """ Byter färg på rutan.
        Inparameter är färgen man vill byta till. """
        self.color = color
        self.button.configure(bg=self.color)

def playSound(box, sound):
    #box.button.configure(command=lambda: stopSound(box, sound))
    winsound.PlaySound(sound, winsound.SND_FILENAME | winsound.SND_ASYNC)

def stopSound(box):
    #box.button.configure(command=lambda: playSound(box, sound))
    winsound.PlaySound(None, winsound.SND_ASYNC)


########## Main ##########
def main():
    """ Main-funktion, skapar rotfönster och drar sen igång spelet. """
    root = Tk()
    app = SoundBoard(root)
    root.mainloop()

############
if __name__ == '__main__':
    main()
winsound.PlaySound(None, winsound.SND_ASYNC) # Sluta spela musik om rotfönstret stängs
############
