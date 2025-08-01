
class Node:
    def __init__(self,data= 0 ,next = None , prev = None):
        self.data = data 
        self.next = next
        self.prev = prev


# arr = list(map(int ,input().split()))

# #  single linked list creation

# node1 = Node(arr[0])
# current = node1
# for i in range(1,len(arr)):
#     new_node = Node(arr[i])
#     current.next = new_node
#     current = new_node
    
# while node1:
#     print(node1.data)
#     node1 = node1.next

# #  doubly linked list creation

# head = Node(arr[0])
# current = head
# for i in range(1,len(arr)):
#     new_node = Node(arr[i])
#     current.next = new_node 
#     new_node.prev = current
#     current = new_node 

# print("forward traversal")


# last = None 
# while head:
#     print(head.data)
#     last = head
#     head = head.next

# print("backward traversal")

# while last:
#     print(last.data)
#     last = last.prev



# arr = list(map(int ,input().split()))

# head = Node(arr[0])
# current = head
# for i in range(1,len(arr)):
#     new_node = Node(arr[i])
#     current.next = new_node 
#     new_node.prev = current
#     current = new_node 

# print('search output ')

# def search(head,target):
#     index = 0 
#     while head:
#         if head.data == target:
#             return index
#         head = head.next
#         index+=1
#     return -1

# target = int(input("Enter the target to search: "))
# print(search(head,target))



#  Delete a node in doubly linked list

arr = list(map(int,input().split()))

head = Node(arr[0])
current = head

for i in range(1,len(arr)):
    new_node = Node(arr[i])
    current.next = new_node
    new_node.prev = current 
    current = new_node 

#  delete head node

def delete_head(head):
    if head == None:
        return None 
    new_head = head.next
    if new_head:
        new_head.prev = None
    return new_head

head = delete_head(head)
print( "head : " ,head.data)

# delete tail node 

def delete_tail(head):
    if head == None:
        return None
    current = head 
    while current.next:
        current = current.next
    if current.prev:
        current.prev.next = None
    return head
head = delete_tail(head)

print("After deleting tail node:")

while head:
    print(head.data)
    head = head.next

#  delete a node in doubly linked list

def delete_node(head, target):
    current = head
    while current:
        if current.data == target:
            current.prev.next = current.next
            current.next = current.prev
    return head


target = int(input())
head = delete_node(head, target)

