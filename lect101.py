#  children sum property 

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


def childrensumproperty(root):
    if root == None:
        return 
    child = 0 
    if root.left:
        child += root.left.data
    if root.right:
        child += root.right.data
    if child >= root.data:
        root.data = child
    else:
        if root.left:
            root.left.data = root.data
        if root.left:
            root.right.data = root.data
    childrensumproperty(root.left)
    childrensumproperty(root.right)
    tot = 0
    if root.left:
        tot += root.left.data
    if root.right:
        tot += root.right.data
    if root.left or root.right:
        root.data = tot

print(childrensumproperty(root))