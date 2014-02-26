from tkinter import *; import string; import winsound
class SoundBoard:
    GRIDSIZE = 6 # 10 är standard. Går att välja tal mellan 10 och 26 (längden av engelska alfabetet)
    def __init__(self, root):
        """ Konstruktor, bestämmer variabler och kör igång createGrid, outerPlacementControl och sätter igång spelmusiken. 
        Inparameter är rotfönstret. """
        self.BGCOLOR = "#689E68" # Standardbakgrundsfärg för rutor.
        self.TERMINAL_FONT = ("Verdana", 18) # Standardfont för text i rutor.
        self.root = root # Rotfönstret.
        self.root.title("Sound Board") # Rotfönstrets titel.
        self.root.geometry("+300+0") # Rotfönstrets placering.
        self.createGrid()
        
    def createGrid(self):
        """ Skapar det grafiska rutnätet av knappar, koordinater och text samt skapar fuskknappen (döljs nere i det högra hörnet). """
        self.fixGridsize()
        COLUMNS = list(string.ascii_uppercase) # Lista med alfabetet
        Label(text="", bg=self.BGCOLOR).grid(column=0, row=0, sticky=N+S+E+W)
        [Label(text="Test", fg="darkgreen", bg=self.BGCOLOR, font=self.TERMINAL_FONT).grid(column=c+1, row=0, sticky=N+S+E+W) for c in range(self.GRIDSIZE)]
        [Label(text="Test", fg="darkgreen", bg=self.BGCOLOR, font=self.TERMINAL_FONT).grid(column=0, row=r, sticky=N+S+E+W) for r in range(1,self.GRIDSIZE+1)]
        for i in range(1,self.GRIDSIZE+1):
            row = [] # Lista som skapas för varje rad.
            for j in range(1,self.GRIDSIZE+1):
                coords = (i,j) # Koordinater på spelfältet, från 1 till GRIDSIZE.
                row.append(Box(self, coords, self.root, "#1789C2"))
        self.root.resizable(0,0)

    def fixGridsize(self):
        """ Kontroller för att fixa till storleken av rutnätet om det angetts ett för stort eller för litet värde. """
        if self.GRIDSIZE>26:
            self.GRIDSIZE=26 
        elif self.GRIDSIZE<5:
            self.GRIDSIZE=5
            
    def buttonMaker(self, win, info="OK", fg="darkgreen", bg="#93C993", font=("Arial", 18)):
        """ Metod för att skapa knappar.
        Inparametrar är vilket fönster knappen ska finnas i, vad som ska stå på knappen och med vilken textfärg, bakgrundsfärg och font.
        Returnerar knappen. """
        return Button(win, text=info, fg=fg, bg=bg, font=font)
    
class Box(SoundBoard):
    def __init__(self, parent, coords, root, color):
        """ Konstruktor, bestämmer variabler och skapar knappen.
        Inparametrar är rutans koordinater, rotfönstret samt rutans färg. """
        self.coords = coords # Rutans koordinater.
        self.root = root # Rotfönstret.
        self.color = color
        self.button = Button(
            self.root, bg=self.color,
            text="Testljud",
            activebackground="blue",
            relief=GROOVE,
            command=lambda: playSound()
            )
        self.button.config(width="10",height="3", padx="10", pady ="10")
        self.button.grid(column=self.coords[0], row=self.coords[1])
        Grid.columnconfigure(self.root,self.coords[0],weight=1)

    def changeColor(self, color):
        """ Byter färg på rutan.
        Inparameter är färgen man vill byta till. """
        self.color = color
        self.button.configure(bg=self.color)
def playSound():
    winsound.PlaySound("hearsomething.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)


########## Main ##########
def main():
    """ Main-funktion, skapar rotfönster och drar sen igång spelet. """
    root = Tk()
    game = SoundBoard(root)
    root.mainloop()

############
if __name__ == '__main__':
    main()
winsound.PlaySound(None, winsound.SND_ASYNC) # Sluta spela musik om rotfönstret stängs
############
