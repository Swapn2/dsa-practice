#  diameter of the binary tree


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

def height(root):
    if root == None:
        return 0
    lh = height(root.left)
    rh = height(root.right)
    return max(lh,rh)+1


def daimeter(root):
    
    if root == None:
        return 0
    lh = height(root.left)
    rh = height(root.right)

    maxi = lh+rh

    leftside = daimeter(root.left)
    rightside = daimeter(root.right)

    return max(leftside,rightside,maxi)


print(daimeter(root))