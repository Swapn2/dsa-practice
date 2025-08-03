#  check list is palindrome or not

class Node:
    def __init__(self, val = 0 , next = None):
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

#  Reverse brute approach
def palindrome(head):
    temp = head 
    stack = []
    while(temp):
        stack.append(temp.val)
        temp = temp.next
    temp = head 
    while(temp):
        if temp.val != stack.pop():
            return False
        temp = temp.next
    return True

#  function call 

head = create_ll(arr)
traverse(head)
print(palindrome(head))