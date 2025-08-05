#  find length of  a loop or cycle in a linked list

class Node:
    def __init__(self ,val = 0 ,next = None):
        self.val = val
        self.next = next
    

# Create nodes
head = Node(1)
second = Node(2)
third = Node(38)
fourth = Node(4)
fifth = Node(5)

# Connect the nodes
head.next = second
second.next = third
third.next = fourth
fourth.next = fifth

# Create the cycle: point fifth back to third
fifth.next = third  # Cycle created her

# def length(head):
#     temp = head
#     timer = 1
#     d = {}
#     while(temp):
#         if temp in d:
#             value = d[temp]
#             return timer - value
#         d[temp] = timer
#         timer +=1 
#         temp = temp.next
#     return False

# #  optimal approach 

def length(head):
    slow = head
    fast = head
    while(fast and fast.next):
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            print("loop here")
            return lengthfinder(slow , fast)
    return False
def lengthfinder(slow , fast):
    count =1 
    fast = fast.next
    while(slow != fast):
        count+=1
        fast = fast.next
    return count

print(length(head))