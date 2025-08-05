#  find the intersection between Y LL
# 3 7 8 10 
# 99 1 8 10 
class Node:
    def __init__(self, val =0 , next=None):
        self.val = val 
        self.next = next

common = Node(4,Node(5))
head1 = Node(1,Node(2,Node(3,common)))
head2 = Node(9,common)

def print_list(head):
    res = []
    while head:
        res.append(str(head.val))
        head = head.next
    print(" → ".join(res))

# def intersection(head1, head2):
#     temp = head1
#     d = {}
#     while(temp):
#         d[temp] = 1
#         temp = temp.next
#     temp = head2
#     while(temp):
#         if temp in d:
#             return temp
#         temp = temp.next
#     return False

#  other approach 
# def intersection(head1,head2):
#     temp = head1
#     n1 = 0
#     while(temp):
#         n1+=1
#         temp = temp.next
#     temp = head2

#     n2 = 0 
#     while(temp):
#         n2 +=1
#         temp = temp.next
#     print(n1,n2)
#     if n1>n2:
#         return intersection_helper(head1, head2, n1-n2)
#     else:
#         return intersection_helper(head2, head1, n2-n1)

# def intersection_helper(head1,head2,d):
#     temp = head1
#     while(d):
#         temp = temp.next
#         d-=1
#     temp2 = head2
#     # print(temp.val , temp2.val)
#     while(temp2):
#         if temp == temp2:
#             return temp
#         temp2 = temp2.next
#         temp = temp.next
#     return False
    
#  optimal approach 

def intersection(head1,head2):
    if head1 == None or head2 == None:
        return False
    temp1 = head1
    temp2 = head2
    while(temp1 and temp2):
        if temp1 == temp2:
            return temp1
        if temp1.next == None and temp2.next != None:
            temp1 = head2
            temp2 = temp2.next
        elif temp2.next == None and temp1.next != None:
            temp2 = head1
            temp1 = temp1.next
        elif temp1.next == None and temp2.next == None:
            return False 
        else:
            temp1 = temp1.next
            temp2 = temp2.next
node = intersection(head1, head2)
print(node)
print(node.val)
