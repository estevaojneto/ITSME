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
		
	def add_node(self):
		val = input("Insert node value for adding:")
		new_node = Node(val, None, None)
		if(self.root == None):
			self.root = new_node
		else:
			
		return
		
	def del_node(self, root):
		val = input("Insert node value for deleting:")
		print(value)
		return
		
	def tree_rebalance(self):
		return
		
loop = True
tree = Tree()

while(loop):
	print("0 - Add Node")
	print("1 - Delete Node")
	print("2 - Print Tree")
	print("Any - Exit")
	sel = input("Insert option:")
	options = {
	"0": tree.add_node(),
	"1": "Você escolheu 1",
	"2": "Você escolheu 3"
	}
	try:
	    result = options[int(sel)]
	except ValueError:
		loop = False;
	except KeyError:
	    loop = False
