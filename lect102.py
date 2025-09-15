#  nodes at distance k 

from collections import deque,defaultdict


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


def markparent(root, parent_track):
    if root == None:
        return None
    queue = deque()
    queue.append(root)
    while queue:
        current = queue.popleft()
        if current.left:
            parent_track[current.left] = current
            queue.append(current.left)
        if current.right:
            parent_track[current.right] = current
            queue.append(current.right)

        

def distancek(root,target, k):
    parent_track = {}
    markparent(root, parent_track)
    visited = set()
    queue = deque()
    queue.append(target)
    visited.add(target)
    curr_level =0 
    while queue:
        size = len(queue)
        if curr_level == k:
            break
        curr_level +=1
        for _ in range(size):
            current = queue.popleft()
            if current.left and current.left not in visited:
                queue.append(current.left)
                visited.add(current.left)
            if current.right and current.right not in visited:
                queue.append(current.left)
                visited.add(current.right)
            if current in parent_track and parent_track[current] not in visited:
                queue.append(parent_track[current])
                visited.add(parent_track[current])
        result = [node.data for node in queue]
        return result

print(distancek(root,root.left.right, 2))