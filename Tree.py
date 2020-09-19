"""Simple Tree"""


__author__ = "Sá, G. N. B."
__credits__ = ["Sá, G. N. B."]
__license__ = "MIT"
__version__ = "1.0.1"	
__maintainer__ = "Sá, G. N. B."
__email__ = "guinbsa@gmail.com"
__status__ = "Development"

__all__ = ['Node']


class Node(object):
	"""Node of Simple Tree. Base of all others"""
	def __init__(self, data, *children):
		"""Constructor

		Parameters:
		data (?): Any information
		children (Node): Any son of this node

		"""
		self.data = data
		self.children = list(children)
		self.search_type = 'depth'

	def __str__(self):
		"""Returns a string with the node information
		
		Return:
		str: The data from this node

		"""
		return str(self.data)

	def __iter__(self):
		"""Returns an iterable object, starting a queue or stack
		
		Return:
		list: An iterator object of this node, containing itself

		"""
		self.iter = [self]
		return self

	def __next__(self):
		"""Returns a next node of Tree
		
		Return:
		Node: next node or None, depending on the number of children
		
		"""
		if self.iter:
			current = None
			if self.search_type == 'depth':
				current = self.iter.pop()
			elif self.search_type == 'width':
				current = self.iter.pop(0)
			else:
				current = None
			if current != None:
				[self.iter.append(son) for son in current.lst_of_children]
			return current
		else:
			raise StopIteration

	@property
	def is_leaf(self):
		"""Returns whether this node is a leaf or not
		
		Return:
		bool: True if this node is a leaf. False, otherwise
		
		"""
		return len(self.lst_of_children) == 0

	@property
	def height(self):
		"""Returns the height of this node in the tree

		Return:
		int: Height of this node

		"""
		if self.is_leaf:
			return 0
		else:
			return max([son.height + 1 for son in self.lst_of_children])

	def depth(self, node, node_depth=0):
		"""Returns the depth of node in the subtree

		Parameters:
		node (Node): The interest node
		node_depth (int): Depth until then

		Return:
		int: The depth of the node passed as a parameter 
			within the subtree of this node

		"""
		if self == node:
			return node_depth
		elif self.is_leaf:
			return
		else:
			for son in self.lst_of_children:
				son_depth = son.depth(node, node_depth+1)
				if son_depth != None:
					return son_depth

	def level(self, node):
		"""Returns the level of node in the subtree

		Parameters:
		node (Node): The interest node

		Return:
		int: The Level of the node passed as a parameter
			within the subtree of this node

		"""
		return self.height - self.depth(node)

	def equals(self, node):
		"""Returns whether a node is equals to another
		
		Parameters:
		node (Node): The interest node

		Return:
		bool: True if equals
		
		"""
		return self.data == node.data

	def search(self, goal):
		"""Returns the node that matches the search

		Parameters:
		goal (Node): Research node

		Return:
		Node: Node that matches the search

		"""
		for current in self:
			if current.equals(goal):
				return current

	def new_son(self, *data):
		"""Adds a new node in the subtree
		
		Parameters:
		data (?): Any information
		
		"""
		[self.children.append(Node(d)) for d in data]

	@property
	def lst_of_children(self):
		"""Returns the list of children for this node
		
		Return:
		list: List of children of this node
		
		"""
		return self.children


if __name__ == '__main__':
	pass
