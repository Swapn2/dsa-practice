#  right / left view of the binary tree

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

#  right view 
def leftview(root,level,ds):
    if root == None:
        return []
    if level == len(ds):
        ds.append(root.data)
    leftview(root.right,level+1,ds)
    leftview(root.left, level+1,ds)
    return ds

ds = []
print(leftview(root,0,ds))
