#  min time taken to burn a BT from a node
from collections import deque
class Node:
    def __init__(self, data , left = None, right = None):
        self.data = data
        self.left = None
        self.right= None

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


def bfstomapparent(root,start,map):
    queue = deque()
    queue.append(root)
    res = Node(0)
    while queue:
        node = queue[-1]
        if node.data == start:
            res = node
        queue.pop()
        if node.left:
            map[node.left] = node
        if node.right:
            map[node.right] = node
    return res

def findmintime(map , target):
    queue = deque()
    queue.append(target)
    visited = set()
    visited.add(target)
    maxi = 0
    while queue:
        fl = 0
        for i in range(len(queue)):
            node = queue[-1]
            queue.pop()
            if node.left and node.left not in visited:
                fl =1
                visited.add(node.left)
                queue.append(node.left)
            if node.right and node.right not in visited:
                fl = 1
                visited.add(node.right)
                queue.append(node.right)
            if map[node] and map[node] not in visited:
                fl = 1
                visited.add(map[node])
                queue.append(map[node])
        if fl:
            maxi +=1
    return maxi
map = dict()
target = root.right
print(findmintime(map,target))