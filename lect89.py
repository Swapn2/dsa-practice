#  maiximum path sum 

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

def maxpathsum(root,maxi):
    if root == None:
        return 0
    lh = maxpathsum(root.left,maxi)
    rh = maxpathsum(root.right,maxi)
    maxi[0] = max(maxi[0], lh+rh+root.data)
    return max(lh,rh) + root.data

def findmaxpathsum(root, maxi):
    maxi = [float('-inf')]
    maxpathsum(root,maxi)
    return maxi[0]

maxi = [0]
print(findmaxpathsum(root,maxi))

