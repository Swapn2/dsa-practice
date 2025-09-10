
#  check that tree is symmetric 

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

def trysymmetric(root):
    return root ==None or issymmetrichelp(root.left,root.right)
def issymmetrichelp(left,right):
    if left == None or right == None:
        return left == right
    if left.data != right.data:
        return False
    return issymmetrichelp(left.left,right.right) and issymmetrichelp(left.right , right.left)

print(trysymmetric(root))

