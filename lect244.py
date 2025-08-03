#  delete Nth node from the end of a linked list

class Node:
    def __init__(self,val = 0 , next =None):
        self.val = val 
        self.next = next

arr = list(map(int,input().split()))
n = int(input())
def create_ll(arr):
    head = Node(arr[0])
    curr = head
    for i in range(1,len(arr)):
        curr.next = Node(arr[i])
        curr = curr.next
    return head 

def traverse(head):
    while(head):
        print(head.val ,end = " ")
        head = head.next
    print("\n")

# #  brute approach

# def Nthfromlast(head,N):
#     count = 0 
#     temp = head
#     while(temp):
#         count+=1
#         temp = temp.next
    
#     if N == count:
#         head = head.next
#         return head
#     res = count - N
#     temp = head
#     if res < 0:
#         return head
#     while(temp):
#         res -= 1
#         if res ==0:
#             break
#         temp = temp.next
#     temp.next= temp.next.next
#     return head

#  optimal approach 
def Nthfromlast(head,n):
    fast = head
    slow = head
    if n == 0 or n < 0:
        return head
    for i in range(n):
        fast = fast.next
    if fast == None:
        head = head.next
        return head
    while(fast.next):
        slow = slow.next
        fast = fast.next
    slow.next = slow.next.next
    return head
        


#  function calls 
head = create_ll(arr)
traverse(head)
# head = Nthfromlast(head,n)
# traverse(head)
head = Nthfromlast(head,n)
traverse(head)