#  level order traversal 
from collections import deque

class Node:
    def __init__(self, val , left = None , right = None):
        self.val = val 
        self.left = left 
        self.right = right


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



def levelordertraversal(root):
    if root == None:
        return []
    result = []
    queue = deque([root])
    while queue:
        level = []
        for i in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)

    return result

print(levelordertraversal(root))
        