from linkedQfile import *
from molgrafik import *

############## Programmets början ################

class MolQOps():
	def __init__(self, in_str):
		self.q = LinkedQ()
		self.previous = ""
		self.open = 0
		self.NUMS = ["0","1","2","3","4","5","6","7","8","9"]
		self.ALPH = "ACBDEFGHIJKLMNOPQRSTUVWXYZ"
		self.ATOMS = ["H","He","Li","Be","B","C","N","O","F","Ne","Na","Mg","Al","Si","P","S",
				"Cl","K","Ar","Ca","Sc","Ti","V","Cr","Mn","Fe","Ni","Co","Cu","Zn","Ga","Ge",
				"As","Se","Br","Kr","Rb","Sr","Y","Zr","Nb","Mo","Tc","Ru","Rh","Pd","Ag","Cd",
				"In","Sn","Sb","I","Te","Xe","Cs","Ba","La","Ce","Pr","Nd","Pm","Sm","Eu","Gd",
				"Tb","Dy","Ho","Er","Tm","Yb","Lu","Hf","Ta","W","Re","Os","Ir","Pt","Au","Hg",
				"Tl","Pb","Bi","Po","At","Rn","Fr","Ra","Ac","Pa","Th","Np","U","Am","Pu","Cm",
				"Bk","Cf","Es","Fm","Md","No","Lr","Rf","Db","Hs","Sg","Bh","Mt","Rg","Ds","Cn"]
		self.createMolQ(in_str)

	def createMolQ(self, in_str):
		for i in in_str:
			self.q.put(Node(i))
		self.readFormula()

	def readFormula(self):
		if self.q.peek() == "#":
			pass
		elif self.q.isEmpty():
			raise SyntaxError("Saknad stor bokstav" + " vid radslutet " + str(self.q))
		else:
			self.readMol()
			if self.q.peek() == "(":
				self.previous += self.q.get().value
			print("Formeln är syntaktiskt korrekt")

	def readMol(self):
		self.readGroup()
		if not self.q.peek() == None:
			if not self.q.peek() == ")":
				self.readMol()
			else:
				if self.q.peek() not in self.NUMS:
					if self.q.peek() == ")":
						if self.open < 1:
							raise SyntaxError("Felaktig gruppstart" + " vid radslutet " + str(self.q))
						self.previous += self.q.get().value
						if self.q.peek() not in self.NUMS:
							raise SyntaxError("Saknad siffra" + " vid radslutet " + str(self.q))
						self.open -= 1
				else:
					self.readMol()

	def readGroup(self):
		box = Ruta()
		if not self.q.peek() == None:
			if self.q.peek() == "(": # Startar en molekyl
				self.open += 1
				self.previous += self.q.get().value
				self.readMol()
				if not self.q.peek() == None:
					if self.q.peek() == ")":
						raise SyntaxError("Saknad högerparentes" + " vid radslutet " + str(self.q))
				else:
					if self.previous[:2] == "()" and self.previous[-1] in self.NUMS:
						pass
					else:
						raise SyntaxError("Saknad högerparentes" + " vid radslutet " + str(self.q))
			elif self.q.peek() in self.ALPH: # Om nasta är en stor bokstav
				self.readAtom()
			elif self.q.peek() in self.NUMS: # Om nasta är en siffra 0-9
				if len(self.previous)<1:
					raise SyntaxError("Felaktig gruppstart" + " vid radslutet " + str(self.q))
				elif self.previous[-1].upper() == ")":
					pass
				elif self.previous[-1].upper() not in self.ALPH:
					print(self.previous)
					if self.q.peek() in self.NUMS:
						pass
					else:
						raise SyntaxError("Felaktig gruppstart 1" + " vid radslutet " + str(self.q))
				num = self.getNums()
				self.previous += num
				if len(num) < 2:
					if num == "1" or num == "0":
						raise SyntaxError("För litet tal" + " vid radslutet " + str(self.q))
				else:
					if num[0] == "0":
						check = False
						for i in num[::-1]:
							if not check:
								if i=="0":
									check = True
								else:
									self.q.put(Node(i),0)
							else:
								self.q.put(Node(i),0)
						raise SyntaxError("För litet tal" + " vid radslutet " + str(self.q))
			elif self.q.peek() in self.ALPH.lower():
				raise SyntaxError("Saknad stor bokstav" + " vid radslutet " + str(self.q))
			elif self.q.peek() ==")":
				if self.previous == "(":
					self.previous += self.q.get().value
					if self.q.peek() not in self.NUMS:
						raise SyntaxError("Saknad siffra" + " vid radslutet " + str(self.q))
				else:
					raise SyntaxError("Felaktig gruppstart" + " vid radslutet " + str(self.q))
			else:
				raise SyntaxError("Felaktig gruppstart" + " vid radslutet " + str(self.q))

	def getNums(self):
		num = ""
		while self.q.peek() in self.NUMS:
			get = self.q.get()
			num += get.value
		return num

	def readAtom(self):
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
					raise SyntaxError("Okänd atom" + " vid radslutet " + str(self.q))
		if self.existsAtom(atom):
			self.previous += atom
			pass
		else:
			raise SyntaxError("Okänd atom" + " vid radslutet " + str(self.q))

	def existsAtom(self, atom):
		if atom in self.ATOMS:
			return True


###### Lista med testfall #######
li = ["Na","H2O","Si(C3(COOH)2)4(H2O)7","Na332","C(Xx4)5","C(OH4)C","C(OH4C","H2O)Fe","H0",
"H1C","H02C","Nacl","a","(Cl)2)3",")","2","si","Si)","(Si3)","Si(C3","()","Si103","","Si10340",
"Si(C)","!¤%&&%/=?","()3","C(Xx4","#"]
######################

in_str = ""
mg = Molgrafik()

# För att testa med vanlig input
while in_str != "#":
	in_str = input("Molekyl: ")
	try:
			MolQOps(in_str)
	except SyntaxError as msg:
			print(msg)

# # För att testa hela listan med testfallen
# for i in li:
# 	in_str = i
# 	if in_str != "#":
# 		try:
# 				MolQOps(in_str)
# 		except SyntaxError as msg:
# 				print(msg)
