#  same tree or not 

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



root1 = Node(1)
root1.left  = Node(2)
root1.right = Node(3)
root1.left.left = Node(4)
root1.left.right = Node(5)
root1.left.right.left = Node(8)
root1.right.left = Node(6)
root1.right.right = Node(7)
root1.right.right.left = Node(9)
root1.right.right.right = Node(10)



def issametree(p,q):
    if p == None and q == None:
        return True
    if p == None or q == None:
        return False
    if p.data != q.data:
        return False
    return issametree(p.left,q.left) and issametree(p.right,q.right)

print(issametree(root,root1))

