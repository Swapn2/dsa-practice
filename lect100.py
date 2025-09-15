#  widht of binary tree

from queue import Queue


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

class Solution:
    def widthOfBinaryTree(self, root) -> int:
        if root == None:
            return 0
        ans = 0
        q = Queue()
        q.put((root,0))
        while not q.empty():
            size = q.qsize()
            mmin = q.queue[0][1]
            first = None
            last = None
            for i in range(size):
                node, cur_id = q.get() 
                if i ==0:
                    first = cur_id
                if i == size-1:
                    last = cur_id
                if node.left:
                    q.put((node.left,2*cur_id+1))
                if node.right:
                    q.put((node.right, 2*cur_id+2))
            ans = max(ans , last-first+1)
        return ans 


print(Solution().widthOfBinaryTree(root))