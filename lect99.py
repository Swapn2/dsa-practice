#  lowest common ancestor in a binary tree

class Node:
    def __init__(self, data , left = None , right = None):
        self.data = data 
        self.right = right 
        self.left = left 

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


def lca(root , n1 , n2):
    if root == None or root == n1 or root == n2:
        return root
    leftside = lca(root.left, n1,n2)
    rightside = lca(root.right , n1,n2)
    if leftside ==None:
        return rightside
    elif rightside == None:
        return leftside
    else:
        return root.data
    
print(lca(root, root.left.right.left, root.right.right.right))

