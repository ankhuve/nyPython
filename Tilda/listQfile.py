class ListQ(object):
	def __init__(self):
		self.hand = []	

	def put(self, n):
		self.hand.append(n)

	def get(self):
		return self.hand.pop(0)

	def isEmpty(self):
                if len(self.hand) == 0:
                        return True
                else:
                        return False
