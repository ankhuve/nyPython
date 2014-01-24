# Skriv en egen klass som representerar ett gympapass. 
# Klassen ska ha attributen lokal, tid, passtyp, rum, ledare och platser. 
# Klassen ska ha minst fem metoder, bland dem metoden__str__
# Skriv en funktion som läser in data från filen fsdata.txt, skapar gympapass-objekt, och lagrar objekten i en lista. (lista = []).
# Skriv ett huvudprogram där man kan söka efter önskat pass.

class GympaPass:
	def __init__(self, info):
		self.lokal = info[0]
		self.tid = info[1]
		self.passtyp = info[2]
		self.rum = info[3]
		self.ledare = info[4]
		self.platser = info[5]

	def __str__(self):
		string = ""
		string += "Lokal: "+self.lokal
		string += "\nPasstyp: "+self.passtyp
		string += "\nRum: "+self.rum
		string += "\nLedare: "+self.ledare
		string += "\nPlatser: "+self.platser
		return string

	def matchQuery(self, query):
		if query.lower() in self.__str__().lower():
			return True
		else:
			return False

	def metodAwesome(self):
		pass

	def metodAwesomer(self):
		pass

def readFile():
	text = open("fsdata.txt", "r")
	info = text.read()
	info = info.splitlines()
	objekt_lista = []
	for i in range(0,len(info),7):
	    info_lista = []
	    for k in range(7):
	        info_lista.append(info[i+k])
	    objekt_lista.append(GympaPass(info_lista))
	return objekt_lista

def main():
	objekt_lista = readFile()
	query = ""
	while query.lower() != "avsluta":
		query = input("Skriv in ett sökord (plats, ledare, passtyp etc.) eller skriv 'Avsluta' för att avsluta: ")
		if query == "":
			print("Du måste skriva in ett sökord! Försök igen. ")
		else:
			for i in objekt_lista:
				if i.matchQuery(query) == True:
					print(i,"\n")

main()
