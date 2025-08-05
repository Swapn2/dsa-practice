#   add 1 to linklist 
class Node:
    def __init__(self,val = 0 ,next = None):
        self.val = val
        self.next = next

arr = list(map(int, input().split()))

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
        print(head.val, end=" ")
        head = head.next
    print("\n")

# def reverse(head):
#     prev=None
#     curr = head
#     while(curr):
#         nextnode = curr.next
#         curr.next = prev 
#         prev = curr
#         curr= nextnode 
#     return prev
    


# def addOne(head):
#     carry = 1
#     head = reverse(head)
#     temp = head
#     while(temp):
#         sum = temp.val +carry
#         temp.val = sum%10
#         temp = temp.next
#         carry = sum//10
#         if carry == 0:
#             break
#     if carry:
#         # print(carry)
#         head = reverse(head)
#         newnode = Node(carry)
#         newnode.next = head
#         return newnode
#     else:
#         head = reverse(head)
#         return head
        
#  optimal approach (recursive):

def helper(temp):
    if temp == None:
        return 1
    carry = helper(temp.next)
    temp.val = temp.val + carry
    if temp.val < 10:
        return 0
    temp.val =0
    return 1



def addOne(head):
    carry = helper(head)
    if carry == 1:
        newnode = Node(carry)
        newnode.next = head
        return newnode
    else:
        return head


#  functional calls 
head = create_ll(arr)
traverse(head)
# head = reverse(head)
# traverse(head)
head = addOne(head)
traverse(head)


