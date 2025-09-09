#  boundary traversal 

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


def isleaf(root):
    return not root.left and not root.right

def addleftboundary(root, res):
    curr = root.left
    while curr:
        if not isleaf(curr):
            res.append(curr.data)
        if curr.left:
            curr = curr.left
        else:
            curr = curr.right
    return res

def addleaves(root,res):
    if isleaf(root):
        res.append(root.data)
    if root.left:
        addleaves(root.left, res)
    if root.right:
        addleaves(root.right,res)
    return res

def addrightboundary(root,res):
    curr = root.right
    temp = []
    while curr:
        if not isleaf(curr):
            temp.append(curr.data)
        if curr.right:
            curr = curr.right
        else:
            curr = curr.left
    for i in range(len(temp)-1,-1,-1):
        res.append(temp[i])
    return res


def printboundary(root):
    res = []
    if root ==None:
        return []
    if not isleaf(root):
        res.append(root.data)
    addleftboundary(root,res)
    addleaves(root,res)
    addrightboundary(root,res)
    return res


print(printboundary(root))