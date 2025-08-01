#  group odd and even index in a linked list
class Node:
    def __init__(self,val =0,next = None):
        self.val = val
        self.next = next

arr = list(map(int,input().split()))

def create_ll(arr):
    head = Node(arr[0])
    curr = head
    for i in range(1,len(arr)):
        new_node = Node(arr[i])
        curr.next = new_node
        curr = new_node
    return head

def traverse(head):
    while(head):
        print(head.val, end = " ")
        head = head.next
    print("\n")


# Brute force approach 

def group_odd_even(head):
    curr = head
    newhead = Node(-1)
    dummy = newhead
    # for even index
    while curr:
        newnode = Node(curr.val)
        dummy.next = newnode
        dummy = dummy.next
        if curr.next.next: 
            curr = curr.next.next
    # for odd index 
    curr = head.next
    while curr:
        newnode = Node(curr.val)
        dummy.next = newnode
        dummy = dummy.next
        if curr.next.next:
            curr = curr.next.next
    return dummy.next

        
head = create_ll(arr)
traverse(head)
head = group_odd_even(head)
traverse(head)