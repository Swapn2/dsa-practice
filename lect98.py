#  print root to node path is binary tree

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


def function(root, arr, x):
    if root == None:
        return []
    arr.append(root.data)
    if root.data == x:
        return True
    if function(root.left , arr,x) or function(root.right , arr,x):
        return True
    arr.pop()
    return False
def solve(root , x):
    arr = []
    function(root,arr,x)
    return arr
print(solve(root,5))