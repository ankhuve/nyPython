from linkedQfile import *
from molgrafik import *
############## Programmets borjan ################

class MolReader():
	def __init__(self, in_str):
		self.q = LinkedQ()
		self.mol = None
		self.NUMS = ["0","1","2","3","4","5","6","7","8","9"]
		self.ALPH = "ACBDEFGHIJKLMNOPQRSTUVWXYZ"
		self.ATOMS = ["H","He","Li","Be","B","C","N","O","F","Ne","Na","Mg","Al","Si","P","S",
				"Cl","K","Ar","Ca","Sc","Ti","V","Cr","Mn","Fe","Ni","Co","Cu","Zn","Ga","Ge",
				"As","Se","Br","Kr","Rb","Sr","Y","Zr","Nb","Mo","Tc","Ru","Rh","Pd","Ag","Cd",
				"In","Sn","Sb","I","Te","Xe","Cs","Ba","La","Ce","Pr","Nd","Pm","Sm","Eu","Gd",
				"Tb","Dy","Ho","Er","Tm","Yb","Lu","Hf","Ta","W","Re","Os","Ir","Pt","Au","Hg",
				"Tl","Pb","Bi","Po","At","Rn","Fr","Ra","Ac","Pa","Th","Np","U","Am","Pu","Cm",
				"Bk","Cf","Es","Fm","Md","No","Lr","Rf","Db","Hs","Sg","Bh","Mt","Rg","Ds","Cn"]
		self.data = self.createMolQ(in_str)
		# self.mg.show(self.createMolQ(in_str))

	def createMolQ(self, in_str):
		for i in in_str:
			self.q.put(Node(i))
		mol = self.readFormula()
		return mol

	def readFormula(self):
		mol = self.readMol()
		print("Formeln är syntaktiskt korrekt")
		return mol

	def readMol(self):
		if self.q.peek() == None:
			return True
		mol = self.readGroup()
		if self.q.peek() != None:
			mol.next = self.readMol()
		return mol

	def readGroup(self):
		box = Ruta()
		if self.q.peek() == "(":
			self.q.get()
			box.down = self.readMol()
			if self.q.peek() == ")":
				self.q.get()
				box.num = int(self.readNum())
			else:
				raise SyntaxError("Saknad högerparentes vid radslutet " + str(self.q))
		elif self.q.peek() in self.ALPH.lower():
			raise SyntaxError("Saknad stor bokstav vid radslutet " + str(self.q))
		else:
			if self.q.peek() not in self.ALPH:
				print("keff")
				raise SyntaxError("Felaktig gruppstart vid radslutet " + str(self.q))
			box.atom = self.readAtom()
			if self.q.peek() != None and self.q.peek() in self.NUMS:
				box.num = int(self.readNum()) # Om det finns en siffra efter atomen
		return box
			
	def readNum(self):
		print("HA")
		num = ""
		if self.q.peek() == None or self.q.peek() not in self.NUMS:
			raise SyntaxError("Saknad siffra vid radslutet " + str(self.q))
		else:
			while self.q.peek() in self.NUMS:
				num += self.q.get().value
			if len(num) < 2:
				if num == "0" or num == "1":
					raise SyntaxError("För litet tal vid radslutet " + str(self.q))
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
					raise SyntaxError("För litet tal vid radslutet " + str(self.q))
		return num
	
	def readAtom(self):
		atom = self.q.get().value
		if atom in self.ALPH:
			if self.q.peek() != None and self.q.peek() in self.ALPH.lower():
				atom += self.q.get().value
			if not self.existsAtom(atom):
				raise SyntaxError("Okänd atom vid radslutet " + str(self.q))
		else:
			print("lol")
			raise SyntaxError("Saknad stor bokstav vid radslutet " + atom + str(self.q))
		return atom
		
	def existsAtom(self, atom):
		if atom in self.ATOMS:
			return True


###### Lista med testfall #######
li = ["Na","H2O","Si(C3(COOH)2)4(H2O)7","Na332","C(Xx4)5","C(OH4)C","C(OH4C","H2O)Fe","H0",
"H1C","H02C","Nacl","a","(Cl)2)3",")","2","si","Si)","(Si3)","Si(C3","()","Si103","","Si10340",
"Si(C)","!¤%&&%/=?","()3","C(Xx4","#"]
######################

in_str = ""

# För att testa med vanlig input
mg = Molgrafik()
while in_str != "#":
	
	in_str = input()
	try:
			m = MolReader(in_str)
			mg.show(m.data)
	except SyntaxError as msg:
			print(msg)
mg.root.destroy()
# # För att testa hela listan med testfallen
# for i in li:
# 	in_str = i
# 	if in_str != "#":
# 		try:
# 				MolReader(in_str)
# 		except SyntaxError as msg:
# 				print(msg)
