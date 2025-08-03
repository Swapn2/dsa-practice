# Reverse a sLL 

class Node:
    def __init__(self, val = 0 , next = None):
        self.val = val 
        self.next = next 

    
arr = list(map(int,input().split()))

def create_ll(arr):
    head = Node(arr[0])
    curr = head
    for i in range(1, len(arr)):
        new_node = Node(arr[i])
        curr.next = new_node
        curr = new_node
    return head
    

def traverse(head):
    while(head):
        print(head.val, end =" ")
        head = head.next
    print("\n")
#  Reverse brute approach 

def Reverse(head):
    curr = head
    stack = []
    while(curr):
        stack.append(curr.val)
        curr = curr.next
    curr = head
    while(curr):
        curr.val = stack.pop()
        curr = curr.next 
    return head 

#  Reverse optimal approach 

def Reverse1(head):
    curr = head 
    prev = None
    while(curr):
        nextnode = curr.next 
        curr.next = prev
        prev = curr
        curr = nextnode
    return prev


#  recursive approach
def Reverse2(head):
    if head == None or head.next == None:
        return head
    newhead = Reverse2(head.next)
    front = head.next
    front.next = head 
    head.next = None
    return newhead

#  function calls
head = create_ll(arr) 
traverse(head)
# head = Reverse(head)
# traverse(head)
head = Reverse2(head)
traverse(head)

