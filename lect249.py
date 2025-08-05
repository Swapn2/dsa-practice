#  delete middle node in a linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

arr = list(map(int, input().split()))

def create_ll(arr):
    head = ListNode(arr[0])
    curr = head
    for i in range(1, len(arr)):
        new_node = ListNode(arr[i])
        curr.next = new_node
        curr = new_node
    return head

def traverse(head):
    while head:
        print(head.val, end=" ")
        head = head.next
    print("\n")


def delete_middle(head):
    if head == None or head.next == None:
        head = None
        return head
    slow = fast = head
    prev = None
    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next
    prev.next = slow.next
    return head

#  Example usage
head = create_ll(arr)
traverse(head)
head = delete_middle(head)
traverse(head)