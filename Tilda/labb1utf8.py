# Skriv en egen klass som representerar ett gympapass. 
# Klassen ska ha attributen lokal, tid, passtyp, rum, ledare och platser. 
# Klassen ska ha minst fem metoder, bland dem metoden__str__
# Skriv en funktion som läser in data från filen fsdata.txt, skapar gympapass-objekt, och lagrar objekten i en lista. (lista = []).
# Skriv ett huvudprogram där man kan söka efter önskat pass.

class GymClass:
	def __init__(self, data):
		self.data = data
		self.location = data[0]
		self.time = data[1]
		self.type = data[2]
		self.room = data[3]
		self.leader = data[4]
		self.slots = data[5]
		self.dataToString()

	def __str__(self):
		string = ""
		string += "Lokal: "+self.location
		string += "\nTid: "+self.time
		string += "\nPasstyp: "+self.type
		string += "\nRum: "+self.room
		string += "\nLedare: "+self.leader
		string += "\nPlatser: "+self.slots
		return string

	def matchQuery(self, query):
		if query.lower() in self.data_string.lower():
			return True
		else:
			return False

	def returnLocation(self):
		return self.location

	def dataToString(self):
		self.data_string = ""
		for i in self.data:
			self.data_string += i+", "

def createObjectList():
	txt_file = open("fsdata.txt", "r")
	data = txt_file.read()
	data = data.splitlines()
	object_list = []
	for i in range(0,len(data),7):
	    class_data = []
	    for k in range(6):
	        class_data.append(data[i+k])
	    object_list.append(GymClass(class_data))
	return object_list

def main():
	object_list = createObjectList()
	query = ""
	while query.lower() != "avsluta":
		query = input("Skriv in ett sökord (plats, ledare, passtyp etc.) eller skriv 'avsluta' för att avsluta: ")
		if query == "":
			print("Du måste skriva in ett sökord! Försök igen. ")
		elif query.lower() == "avsluta":
			print("Hejdå!")
		else:
			matches = 0
			search_matches = ""
			for i in object_list:
				if i.matchQuery(query) == True:
					matches += 1
					search_matches += str(i)+"\n\n"
			if matches == 0:
				print("Din sökning gav inga resultat. Försök med ett annat sökord.")
			else:
				print("Din sökning gav", matches, "resultat:\n")
				print(search_matches)

main()