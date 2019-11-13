
class Node:
	def __init__(self,weights,offset):
		self.weights = weights
		self.offset=offset
		
	def eval(self,inputList):
		total=self.offset
		for w,v in zip(self.weights,inputList):
			total+=w*v
		return 1 if total>0 else 0
		#return total>0?1:0


ned =Node([.5,.5],-.5)

print(ned.eval([0,1]))
