#  Check for the balanced binary tree


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

# # brute approch 

# def height(root):
#     if root ==None:
#         return 0
#     lh = height(root.left)
#     rh = height(root.right)
#     return max(lh,rh)+1


# def balancedtree(root):
#     if root == None:
#         return True
#     lh = height(root.left)
#     rh = height(root.right)
#     if abs(lh-rh) >1:
#         return False
#     leftside = balancedtree(root.left)
#     rightside = balancedtree(root.right)

#     if (leftside == False or rightside == False):
#         return False
#     return True

#  optimal approach

def balancedtree(root):
    if dfsheight(root) ==-1:
        return False
    else:
        return True

def dfsheight(root):
    if root == None:
        return 0
    lh = dfsheight(root.left)
    if lh == -1:
        return -1
    rh = dfsheight(root.right)
    if rh ==-1:
        return -1
    if abs(lh-rh) >1:
        return -1
    return max(lh,rh)+1


print(balancedtree(root))

    