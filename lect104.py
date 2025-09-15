#  count the total nodes in the complete binary tree

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

def countnodes(root):
    if root == None:
        return 0 
    lh = findheightleft(root)
    rh = findheightright(root)
    if lh == rh:
        return (1<<lh)-1
    else:
        return 1+ countnodes(root.left) + countnodes(root.right)
    
def findheightleft(root):
    if root == None:
        return None
    height = 0
    while root:
        height +=1
        root = root.left
    return height

def findheightright(root):
    if root == None:
        return 0
    height = 0 
    while root:
        height +=1
        root = root.right
    return height

print(countnodes(root))