from bintreeFile import Bintree
from listQfile import *
from ParentNode import ParentNode
import sys



def main():
	swedish = Bintree()
	#Läs in hela filen till ett binärträd
	with open("word3.txt", "r", encoding = "utf-8") as swedishFile:
		for row in swedishFile:
			word = row.strip()
			swedish.put(word)

	startWord = input('Mata in startord: ')
	endWord = input('Mata in slutord: ')

	pn = ParentNode(startWord)
	q = ListQ()
	q.put(pn)

	while not q.isEmpty():
		parentNode = q.get()
		q = makeChildren(parentNode, endWord, swedish, q)
	print('Det ar omojligt att hitta en vag till', endWord)



def makeChildren(parentNode, endWord, swedish, q):
	alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','å','ä','ö']
	
	for i in range(len(parentNode.word)):
		wordList = list(parentNode.word)#läs in startordet som en lista för att lättare kunna byta ut bokstäver
		for letter in alphabet:
			wordList = list(wordList)
			wordList[i] = letter
			wordList = ''.join(wordList)
			child = ParentNode(wordList, parentNode)
			if swedish.exists(wordList) and not child.exists():
				q.put(child)
				if wordList == endWord:
					writeChain(child)
##					child.printParents()
					print('\n')
					#sys.exit()
	return q

def writeChain(child):
	if child.parent != None:
		writeChain(child.parent)
	print(child.word, '->', end=' ')

main()
