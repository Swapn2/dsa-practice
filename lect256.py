#  remove duplicates from a sorted doubly linked list

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


def remove_duplicates(head):
    temp = head
    while(temp and temp.next):
        nextnode = temp.next
        while(nextnode.val == temp.val and nextnode != None):
            nextnode = nextnode.next
        temp.next = nextnode
        if nextnode:
            nextnode.prev = temp
        temp = temp.next
    return head

#  main code
head = create_dll(arr)
traverse(head)
head = remove_duplicates(head)
traverse(head)
