#  delete all occurrences of a given value in a doubly linked list

class Node:
    def __init__(self,val = 0, next = None, prev = None):
        self.val = val 
        self.next = next
        self.prev = prev

arr = list(map(int,input().split()))

def create_ll(arr):
    head = Node(arr[0])
    curr = head
    for i in range(1,len(arr)):
        nextnode = Node(arr[i])
        curr.next = nextnode 
        nextnode.prev = curr
        curr = curr.next
    return head


def traverse(head):
    while(head):
        print(head.val,end =" ")
        head = head.next
    print("\n")


def del_oc(head,key):
    temp = head
    while(temp):
        if temp.val == key:
            if temp == head:
                head=head.next
            nextnode = temp.next
            prevnode = temp.prev
            if nextnode:
                nextnode.prev = prevnode
            if prevnode:
                prevnode.next = nextnode
            temp = nextnode
        else:
            temp = temp.next
    return head

key = int(input())
head = create_ll(arr)
traverse(head)
head = del_oc(head, key)
traverse(head)
