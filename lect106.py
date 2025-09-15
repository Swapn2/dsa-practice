#  construct tree from inorder and preorder 

inorder = list(map(int,input().split()))
preorder = list(map(int,input().split()))

class Node:
    def __init__(self, data , left = None, right = None):
        self.data = data
        self.left = None
        self.right= None


def buildtree(inorder , preorder):
    inmap = {val : idx for idx,val in enumerate(inorder)}
    root = _buildtree(preorder , 0, len(preorder)-1, inorder , 0, len(inorder)-1, inmap)
    return root

def _buildtree(preorder , prestart ,preend , inorder , instart , inend, inmap):
    
    if prestart > preend or instart > inend:
        return None
    root = Node(preorder[prestart])
    inroot = inmap[root.val]
    numsleft = inroot - instart
    root.left = _buildtree(preorder , prestart+1 , prestart+numsleft , inorder , instart , inroot-1 , inmap)
    root.right = _buildtree(preorder , prestart+numsleft+1 , preend , inorder , inroot+1 , inend , inmap)
    return root

print(buildtree(inorder , preorder))
