# Skriv en egen klass som representerar ett gympapass. 
# Klassen ska ha attributen lokal, tid, passtyp, rum, ledare och platser. 
# Klassen ska ha minst fem metoder, bland dem metoden__str__
# Skriv en funktion som läser in data från filen fsdata.txt, skapar gympapass-objekt, och lagrar objekten i en lista. (lista = []).
# Skriv ett huvudprogram där man kan söka efter önskat pass.

######################################
###           Laboration 1         ###
###        Tillämpad Datalogi      ###
### Erik Forsberg och Gustav Fridh ###
###  eforsbe@kth.se gfridh@kth.se  ###
######################################

class GymClass:
	def __init__(self, data):
		""" Konstruktor. Bestämmer attribut från data samt kör metoden dataToString. 
		Inparameter är listan data. """
		self.data = data # Lista med data om passet
		self.location = data[0] # Passets plats
		self.time = data[1] # Passets tid
		self.type = data[2] # Passets typ
		self.room = data[3] # Passets rum
		self.leader = data[4] # Passers ledare
		self.slots = data[5] # Passets platser
		self.dataToString()

	def __str__(self):
		""" Bestämmer hur objekt av klassen ska skrivas ut. 
		Returnerar textsträng. """
		string = ""
		string += "Lokal: "+self.location
		string += "\nTid: "+self.time
		string += "\nPasstyp: "+self.typeg
		string += "\nRum: "+self.room
		string += "\nLedare: "+self.leader
		string += "\nPlatser: "+self.slots
		return string

	def matchSearch(self, search):
		""" Del av sökfunktionen för att kontrollera om sökordet finns i passets data. 
		Inparameter är användarens sökning. 
		Returnerar True om det gav en träff, annars False."""
		if search.lower() in self.data_string.lower():
			return True
		else:
			return False

	def dataToString(self):
		""" Gör om listan data till en sträng för att lättare kunna söka igenom den. """
		self.data_string = ""
		for i in self.data:
			self.data_string += i+"\n"

	def returnData(self):
		""" Returnerar passets data. """
		return self.data_string


def createObjectList():
	""" Funktion för att läsa in data från textfilen, skapa gympapass-objekt och lagra objekten i en lista. 
	Returnerar listan med objekt. """
	txt_file = open("fsdata.txt", "r")
	data = txt_file.read()
	data = data.splitlines()
	object_list = [] # Lista som innehåller alla passen.
	for i in range(0,len(data),7):
	    class_data = [] # Temporär lista som innehåller data för ett pass åt gången.
	    for k in range(6):
	        class_data.append(data[i+k])
	    object_list.append(GymClass(class_data))
	return object_list

def main():
	""" Huvudfunktionen. Kallar på funktionen createObjectList samt innehåller sökfunktionen. """
	object_list = createObjectList()
	search = "" # Sträng för användarens sökord
	print("\nVälkommen till gympassökningsprogrammet, så kul att just du har hittat hit!\n")
	while search.lower() != "avsluta":
		search = input("Skriv in ett sökord (plats, ledare, passtyp etc.) eller skriv 'avsluta' för att avsluta: ")
		if search == "":
			print("Du måste skriva in ett sökord! Försök igen. ")
		elif search in ",.- ¨'^!#¤%&/()=?`'*@£$€{[]}":
			print("Använd bokstäver och siffror istället, det blir så mycket lättare då!")
		elif search.lower() == "avsluta":
			print("Hejdå!")
		else:
			matches = 0 # Räknare som håller koll på hur många träffar sökningen gav.
			search_matches = ""
			for i in object_list:
				if i.matchSearch(search) == True:
					matches += 1
					search_matches += "\n"+str(i)+"\n"
			if matches == 0:
				print("Din sökning gav inga resultat. Försök med ett annat sökord.")
			else:
				print(search_matches)
				print("Din sökning gav", matches, "resultat.\n")

	# print(object_list[4].returnData()) # Test av den femte metoden.

main()