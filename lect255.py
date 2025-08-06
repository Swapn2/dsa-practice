# find all the pairs with given sun is dll

class Node:
    def __init__(self,val = 0 , next = None, prev = None):
        self.val = val 
        self.next = next
        self.prev = prev

arr = list(map(int,input().split()))

def create_dll(arr):
    head = Node(arr[0])
    curr = head
    for i in range(1, len(arr)):
        nextnode = Node(arr[i])
        curr.next = nextnode
        nextnode.prev = curr
        curr = curr.next
    return head

def traverse(head):
    while(head):
          print(head.val , end =" ")
          head = head.next
    print("\n")

# def find_pairs(head,key):
#     d = []
#     temp1 = head
#     while(temp1):
#         temp2 = temp1.next
#         while(temp2):
#             if temp1.val + temp2.val == key:
#                 d.append((temp1.val , temp2.val))
#             if temp1.val + temp2.val >key:
#                 break
#             temp2 = temp2.next
#         temp1 = temp1.next
#         if temp1.val > key:
#             break
#     return d
    

#  optimal approach 

def findtail(head):
    temp = head
    while(temp.next):
        temp = temp.next
    return temp

def find_pairs(head,key):
    d = []
    left = head
    right = findtail(head)
    while(left.val <= right.val):
        if left.val + right.val == key:
            d.append((left.val,right.val))
            left= left.next
            right = right.prev
        elif left.val + right.val > key:
            right = right.prev
        elif left.val + right.val < key:
            left = left.next
    return d

        
        


#  function call 

key = int(input())
head = create_dll(arr)
traverse(head)
print(find_pairs(head,key))