class ListQ():
	def __init__(self):
		self.hand = []	

	def put(self, n, rev=1):
                if rev == 1:
                        self.hand.append(n)
                else:
                        self.hand.insert(rev, n)

	def get(self, i):
		return self.hand.pop(i)

	def isEmpty(self):
                if len(self.hand) == 0:
                        return True
                else:
                        return False
