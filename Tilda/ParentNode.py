

class ParentNode:
	def __init__(self, word, parent = None):
		self.word = word
		self.parent = parent

	def exists(self):
		return existsFunc(self.parent, self.word)

	def printParents(self):
		printParentFunc(self.parent)

def existsFunc(parent, searchWord):
	if parent != None:
		if parent.word == searchWord:
			return True
		else:
			return existsFunc(parent.parent, searchWord)
	return False

def printParentFunc(parent):
	if parent != None:
		printParentFunc(parent.parent)
		print(parent.word, end = " ")