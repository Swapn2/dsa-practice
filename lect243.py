#  sort the link list of 0's, 1's and 2's 

class Node:
    def __init__(self , val =0 , next = None):
        self.val = val 
        self.next = next


arr = list(map(int,input().split()))


def create_ll(arr):
    head = Node(arr[0])
    curr = head
    for i in range(1,len(arr)):
        curr.next = Node(arr[i])
        curr = curr.next
    return head

def traverse(head):
    while(head):
        print(head.val ,end = " ")
        head = head.next
    print("\n")


#  brute approach

def sorting(head):
    temp = head
    count0 = 0
    count1 = 0
    count2 = 0
    while(temp):
        if temp.val == 0:
            count0 +=1
            temp = temp.next
        elif temp.val == 1:
            count1 +=1
            temp = temp.next
        elif temp.val == 2:
            count2 +=1
            temp = temp.next
        else:
            temp = temp.next
    # print("done")
    temp = head
    while(count0):
        temp.val = 0
        temp = temp.next
        count0 -=1
    while(count1):
        temp.val = 1
        temp = temp.next
        count1 -=1
    while(count2):
        temp.val = 2
        temp = temp.next
        count2 -=1
    return head


#  optimal approach 
def sorting_optimal(head):
    if head == None or head.next == None:
        return head
    zerohead = Node(-1)
    onehead = Node(-1)
    twohead = Node(-1)
    zero = zerohead
    one = onehead
    two = twohead
    temp = head
    while(temp):
        if temp.val == 0:
            zero.next = temp
            zero = zero.next
            temp = temp.next
        elif temp.val == 1:
            one.next = temp
            one = one.next
            temp = temp.next
        elif temp.val == 2:
            two.next = temp
            two = two.next
            temp = temp.next
    if onehead.next:
        zero.next = onehead.next
    else:
        zero.next = twohead.next
    if twohead.next:
        one.next = twohead.next
    else:
        one.next = None
    two.next = None
    if zerohead.next:
        return zerohead.next
    elif onehead.next:
        return onehead.next
    else:
        return twohead.next


#  fuinction calls 

head = create_ll(arr)
traverse(head)
# head =  sorting(head)
# traverse(head)
head = sorting_optimal(head)
traverse(head)
