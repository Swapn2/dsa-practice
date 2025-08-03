class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def find_middle(head):
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow  # This is the middle node

# Helper to create a linked list
def create_list(arr):
    dummy = ListNode(-1)
    curr = dummy
    for val in arr:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next

# Example usage
head = create_list([1, 2, 3, 4])
middle = find_middle(head)
print("Middle value:", middle.val)  # Output: 3
