class Node:
	def __init__(self, value, left, right):
		self.value = value
		self.left = left
		self.right = right
	
	def print_node(self):
		print(self.value)

class Tree:
	root = Node(None, None, None)
	def set_root(self, root):
		self.root = root

loop = True
options = {
	"0": "Você escolheu zero",
	"1": "Você escolheu 1",
	"2": "Você escolheu 3"
}

while(loop):
	print("0 - Add Node")
	print("1 - Delete Node")
	print("2 - Print Tree")
	print("Any - Exit")
	sel = input("Insert option:")
	try:
	    result = options[sel]
	except KeyError:
	    loop = False
