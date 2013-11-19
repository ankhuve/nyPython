from tkinter import *
import random

class Game:
    """ Skapar attribut såsom skeppens längder, spelplansstorlek och
    och andra attribut. Skapar även rotfönstret. """
    def __init__(self, root, box_list):
        
    """ Skapar en lista med datorns slumpvis placerade skepp. """ 
    def randomizeShipPlacement(self, box_list, placed_ships):

    """ Kontrollerar så att föregående metod gör en giltig placering.
    (inte utanför spelplan eller överlapp) """
    def controlPlacement(self, box_list, ship):
        
    """ Metod för användarens 'skott'. Kontrollerar status för rutan (finns skepp?). """
    def fireInTheHole(self, coords, status):

    """ Uppdaterar statistiken för rutan (pricksäkerhet och antal skott). """        
    def updateStats(self, shots, hits):

    """ Kontrollerar om resultatet platsar på top-10 i high-score-listan. Avslutar om man inte platsar. """
    def endGame(self):

    """ Läser in high-score-listan från textfil. """        
    def readFile(self):
        
    """ Om man platsar på top-10 så skapas en popup-ruta som meddelar användaren och ber om namn. """
    def highScorePopup(self, shots, hits):
        
    """ Lägger till namn och pricksäkerhet i high-score-listan om man platsar. Avslutar sedan spelet. """
    def highScoreEntry(self, accuracy, popup, name):
        
    """ Skapar en 'fuskknapp'. """
    def createCheatButton(self, placed_ships):

    """ Kör 'fusket', dvs visar skeppens placering när man klickar på den. Döljer skeppen om fusket är påslaget redan. """
    def cheat(self, placed_ships, toggle_cheat):


class Box(Game):
    """ Skapar en knapp med attribut så som koordinater, status (skepp? beskjuten? träffad? missad?) och lägger till dessa
    knappar i rotfönstret. """
    def __init__(self, coords, root, color):

    """ Byter färg på knappen. Kan bli vit/röd beroende på miss/träff eller grå vid fusk påslaget. """
    def changeColor(self, color):


""" Skapar rutnätet av knappar. Skapar alltså en instans av Box för varje knapp. Returnerar en array med instanserna. """
def createGrid():


""" Main-funktionen. Initierar hela spelet tills dess att det väntar på användarinput. """
def main():

