#  top view of the binary tree
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


def function(root):
    if root == None:
        return []
    ans = []
    queue = deque([(root,0)])
    map = dict()
    while queue:
        node,line = queue.popleft()
        if line not in map:
            map[line] = node.data
        if node.left:
            queue.append((node.left, line-1))
        if node.right:
            queue.append((node.right, line+1))
    for line,val in sorted(map.items()):
        ans.append(val)
    return ans

print(function(root))

