#  add 2 number in LL 
class Node:
    def __init__(self,val = 0 , next = None):
        self.val = val
        self.next = next


def addition(head1 , head2):
    t1 = head1
    t2 = head2
    dummynode= Node(-1)
    curr = dummynode
    carry =0
    while(t1 or t2):
        sum = carry
        if t1:
            sum = sum+ t1.val
        if t2:
            sum = sum + t2.val
        new_node = sum%10
        carry = sum//10
        curr.next = Node(new_node)
        curr = curr.next
        if t1:
            t1 = t1.next
        if t2:
            t2 = t2.next
    if carry:
        new_node = Node(carry)
        curr.next = new_node
        curr = curr.next
    return dummynode.next


arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))

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


#  function calls 

head1 = create_ll(arr1)
head2 = create_ll(arr2)
traverse(head1)
traverse(head2)
head = addition(head1,head2)
traverse(head)

