# postorder traversal iterative ( 2 stack)
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


def postordertraversal(root):
    st1 = []
    st2 = []
    postorder = []
    if root == None:
        return []
    st1.append(root)
    while(st1):
        node = st1[-1]
        st1.pop()
        st2.append(node)
        if node.left:
            st1.append(node.left)
        if node.right:
            st1.append(node.right)
    while(st2):
        postorder.append(st2[-1].data)
        st2.pop()
    return postorder



print(postordertraversal(root))
