#  zig zag traversal 
from collections import deque
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

def zigzagtraversal(root):
    if root == None:
        return []
    res = []
    nodequeue = deque()
    nodequeue.append(root)
    lefttoright = True
    while nodequeue:
        row = [0]*len(nodequeue)
        for i in range(len(nodequeue)):
            node = nodequeue.popleft()
            if lefttoright:
                index = i
            else:
                index = len(row)-1-i
            row[index] = node.data
            if node.left:
                nodequeue.append(node.left)
            if node.right:
                nodequeue.append(node.right)
        res.append(row)
        lefttoright = not lefttoright
    return res

print(zigzagtraversal(root))
