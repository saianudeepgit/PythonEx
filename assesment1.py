def special_tree( values, k ) :
	myTree = MySpecialTree(values)
	soln = []
	for val in range(k):
		soln.append(myTree.pop_max_value())
	return soln
class MySpecialTree():
	def __init__(self, values=None):
		self.data = values or []
		for x in range(len(values)//2, -1, -1):
			self.__max_treeify__(x)

	def parent(self, x):
		return x >> 1

	def left_child(self, x):
		return (x << 1) + 1

	def right_child(self, x):
		return (x << 1) + 2

	def __max_treeify__(self, x):
		pass

	def pop_max_value(self):
		pass