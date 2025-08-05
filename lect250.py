#  detect a loop or cycle in a linked list

class Node:
    def __init__(self ,val = 0 ,next = None):
        self.val = val
        self.next = next
    

# Create nodes
head = Node(1)
second = Node(2)
third = Node(3)
fourth = Node(4)
fifth = Node(5)

# Connect the nodes
head.next = second
second.next = third
third.next = fourth
fourth.next = fifth

# Create the cycle: point fifth back to third
fifth.next = third  # Cycle created her

def traverse(head):
    while(head):
        print(head.val ,end = " ")
        head = head.next
    print("\n")

#  brute approach
# def detect_cycle(head):
#     temp = head
#     d = {}
#     while(temp):
#         d[temp] = 1
#         if temp in d:
#             # print("yes")
#             return True
#         temp = temp.next
#     return False


#  optimal approach using Floyd's cycle detection algorithm
def detect_cycle(head):
        if head == None or head.next == None:
            return False
        slow = head
        fast = head
        while(fast != None and fast.next != None):
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False



print(detect_cycle(head))
