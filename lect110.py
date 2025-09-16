#  flatten the tree 

class Node:
    def __init__(self, data , left = None, right = None):
        self.data = data
        self.left = None
        self.right= None

root = Node(1)
root.left  = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.right.left = Node(8)
root.right.left = Node(6)
root.right.right = Node(7)
root.right.right.left = Node(9)
root.right.right.right = Node(10)

def flatten(self , root):
    prev = None
    self._flatten(root)

def _flatten(self , root):
    if root == None:
        return 
    self._flatten(root.right)
    self._flatten(root.left)

    root.right = self.prev
    root.left = None
    self.prev = root