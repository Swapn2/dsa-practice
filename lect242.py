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


# def group_odd_even(head):
#     temp = head
#     arr = []
#     while(temp!= None and temp.next!= None ):
#         arr.append(temp.val)
#         temp = temp.next.next
#     if temp:
#         arr.append(temp.val)
#         temp = temp.next
#     temp = head.next
#     while(temp != None and temp.next != None):
#         arr.append(temp.val)
#         temp = temp.next.next
#     if temp:
#         arr.append(temp.val)
#         temp = temp.next
#     temp = head
#     for i in range(len(arr)):
#         temp.val = arr[i]
#         temp = temp.next
#     return head

#  optimal approach 

def group_odd_even_optimal(head):
    odd = head
    evenhead = head.next
    even = evenhead
    while(even != None and even.next != None):
        odd.next = odd.next.next
        even.next = even.next.next
        odd = odd.next
        even = even.next
    odd.next = evenhead
    return head
        
head = create_ll(arr)
traverse(head)
head = group_odd_even_optimal(head)
traverse(head)