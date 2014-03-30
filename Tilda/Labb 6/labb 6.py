from linkedQfile import *

class ErrorInSyntax(Exception):
	def __init__(self, reason, q):
		self.reason = reason
		self.end_of_line = str(q)
	def __str__(self):
		return self.reason + " vid radslutet " + self.end_of_line

class MolQOps():
	def __init__(self, in_str):
		self.q = LinkedQ()
		self.NUMS = ["0","1","2","3","4","5","6","7","8","9"]
		self.ALPH = "ACBDEFGHIJKLMNOPQRSTUVWXYZ"
		self.ATOMS = ["H",
"He",
"Li",
"Be",
"B",
"C",
"N",
"O",
"F",
"Ne",
"Na",
"Mg",
"Al",
"Si",
"P",
"S",
"Cl",
"K",
"Ar",
"Ca",
"Sc",
"Ti",
"V",
"Cr",
"Mn",
"Fe",
"Ni",
"Co",
"Cu",
"Zn",
"Ga",
"Ge",
"As",
"Se",
"Br",
"Kr",
"Rb",
"Sr",
"Y",
"Zr",
"Nb",
"Mo",
"Tc",
"Ru",
"Rh",
"Pd",
"Ag",
"Cd",
"In",
"Sn",
"Sb",
"I",
"Te",
"Xe",
"Cs",
"Ba",
"La",
"Ce",
"Pr",
"Nd",
"Pm",
"Sm",
"Eu",
"Gd",
"Tb",
"Dy",
"Ho",
"Er",
"Tm",
"Yb",
"Lu",
"Hf",
"Ta",
"W",
"Re",
"Os",
"Ir",
"Pt",
"Au",
"Hg",
"Tl",
"Pb",
"Bi",
"Po",
"At",
"Rn",
"Fr",
"Ra",
"Ac",
"Pa",
"Th",
"Np",
"U",
"Am",
"Pu",
"Cm",
"Bk",
"Cf",
"Es",
"Fm",
"Md",
"No",
"Lr",
"Rf",
"Db",
"Hs",
"Sg",
"Bh",
"Mt",
"Rg",
"Ds",
"Cn"]
		self.createMolQ(in_str)

	def createMolQ(self, in_str):
		for i in in_str:
			self.q.put(Node(i))
		print(self.q)
		self.readFormula()

	def readFormula(self):
		print("Startar readFormula")
		self.readMol()
		print("Klar med readMol")
		if self.q.peek() == "(":
			self.q.get()

	def readMol(self):
		print("Startar readMol")
		self.readGroup()
		print("Klar med readGroup")
		if not self.q.peek() == None:
			if not self.q.peek() == ")":
				self.readMol()
			else:
				if self.q.peek() not in self.NUMS:
					if self.q.peek() == ")":
						self.q.get()
						if self.q.peek() not in self.NUMS:
							raise ErrorInSyntax("Saknad siffra", self.q)
				else:
					self.readMol()

	def readGroup(self):
		print("Startar readGroup")
		if not self.q.peek() == None:
			print("Queue:", str(self.q))
			if self.q.peek() == "(": # Startar en molekyl
				self.q.get()
				self.readMol()
				if not self.q.peek() == None:
					if self.q.get() != ")":
						raise ErrorInSyntax("Saknad hogerparentes", self.q)
				else:
					raise ErrorInSyntax("Saknad hogerparentes", self.q)
			elif self.q.peek() in self.ALPH: # Om nasta ar en stor bokstav
				self.readAtom()
			elif self.q.peek() in self.NUMS: # Om nasta ar en siffra 0-9
				num = self.getNums()
				if len(num) < 2:
					if num == "1" or num == "0":
						raise ErrorInSyntax("For litet tal", self.q)
				else:
					if num[0] == "0":
						raise ErrorInSyntax("For litet tal", self.q)
				# readMol(self.q)
			elif self.q.peek() in self.ALPH.lower():
				raise ErrorInSyntax("Saknad stor bokstav", self.q)
	def getNums(self):
		num = ""
		while self.q.peek() in self.NUMS:
			get = self.q.get()
			num += get.value
		return num

	def readAtom(self):
		print("Startar readAtom")
		atom = self.q.get().value
		if not self.q.isEmpty():
			if self.q.peek() in self.ALPH.lower():
				atom += self.q.get().value
				if self.existsAtom(atom): # Om atomen godkanns
					pass
			elif self.q.peek() in self.ALPH:
				if self.existsAtom(atom):
					pass
				else:
					raise ErrorInSyntax("Okand atom", self.q)
		if self.existsAtom(atom):
			pass
		else:
			raise ErrorInSyntax("Okand atom", self.q)

	def existsAtom(self, atom):
		if atom in self.ATOMS:
			print("Atomen fanns")
			return True

in_str = "Ge)"
m = MolQOps(in_str)
# createMolQ(in_str, molQ)
print("Formeln ar syntaktiskt korrekt")


# Na
# H2O
# Si(C3(COOH)2)4(H2O)7
# Na332
# C(Xx4)5
# C(OH4)C
# C(OH4C
# H2O)Fe
# H0
# H1C
# H02C
# Nacl
# a
# (Cl)2)3
# )
# 2
# si
# Si)
# (Si3)
# Si(C3
# ()
# Si103
# Si10340
# Si10(C)3
# Si(C)