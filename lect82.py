# inorder traversal iterative
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


def inordertraversal(root):
    inorder = []
    node = root
    st = []
    while(True):
        if node != None:
            st.append(node)
            node = node.left
        else:
            if len(st) ==0:
                break
            else:
                node = st[-1]
                st.pop()
                inorder.append(node.data)
                node = node.right
    return inorder

print(inordertraversal(root))

