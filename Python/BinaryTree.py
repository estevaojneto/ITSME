from dataclasses import dataclass

@dataclass
class Node:
	def __init__(self, key):
		self.key = key
		self.left = None
		self.right = None

class Tree:
	root = None
	def add_node(self, curr_node, new_node):
		if(curr_node.key > new_node.key):
			if(curr_node.left == None):
				curr_node.left = new_node
			else:
				self.add_node(curr_node.left, new_node)
		else:
			if(curr_node.right == None):
				curr_node.right = new_node
			else:
				self.add_node(curr_node.right, new_node)
		return True
		
	def print_tree(self, root):
		if(root != None):
			self.print_tree(root.left)
			print(root.key)
			self.print_tree(root.right)
		
	def del_node(self, root):
		val = input("Insert node key for deleting:")
		return True
		
	def tree_rebalance(self):
		return True
		
def menu_function():
    return {
		0: tree.add_node(),
		1: "TODO",
		2: tree.print_tree(tree.root)
	}[x]
	
tree = None
while True:
	print("0 - Add Node")
	print("1 - Delete Node")
	print("2 - Print Tree")
	print("Any - Exit")
	sel = int(input("Insert option:"))
	if sel == 0: 
		val = int(input("Insert node key for adding:"))
		if(tree == None):
			tree = Tree()
			tree.root = Node(int(val))
		else:
			tree.add_node(tree.root, Node(int(val)))
	elif sel == 1: 
		print("Escolheu 1")
	elif sel == 2: 
		tree.print_tree(tree.root)
	else:
		break
	continue