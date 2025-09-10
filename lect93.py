#  vertical order traversal 
from collections import defaultdict
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

def verticaltraversal(root):
    node = defaultdict(lambda: defaultdict(list))
    todo = deque([(root,(0,0))])
    if root == None:
        return []
    while todo:
        temp , (x,y) = todo.popleft()
        node[x][y].append(temp.data)
        if temp.left:
            todo.append((temp.left,(x-1,y+1)))
        if temp.right:
            todo.append((temp.right,(x+1,y+1)))
    ans = []
    for x,y in sorted(node.items()):
        col = []
        for y,values in sorted(y.items()):
            col.extend(sorted(values))
        ans.append(col)
    return ans
            

print(verticaltraversal(root))