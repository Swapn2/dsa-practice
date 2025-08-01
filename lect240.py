# Reverse a DLL 

class Node:
    def __init__(self, val = 0 , next = None, prev = None):
        self.val = val 
        self.next = next 
        self.prev = prev
    
arr = list(map(int,input().split()))

def create_dll(arr):
    head = Node(arr[0])
    curr = head
    for i in range(1, len(arr)):
        new_node = Node(arr[i])
        curr.next = new_node
        new_node.prev = curr
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
    last = None
    while(curr):
        last = curr.prev
        curr.prev = curr.next
        curr.next = last
        curr = curr.prev 
    head = last.prev
    return head 



#  function calls
head = create_dll(arr) 
traverse(head)
head = Reverse(head)
traverse(head)
head = Reverse1(head)
traverse(head)

