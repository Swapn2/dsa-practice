class Node:
    def __init__(self,val = 0 , next = None):
        self.val = val 
        self.next = next

arr = list(map(int, input().split()))

    
def ll(arr):    
    head = Node(arr[0])
    curr = head
    for i in range(1,len(arr)):
        new_node = Node(arr[i])
        curr.next = new_node 
        curr = new_node
    return head
        

def traverse(head):
    while head:
        print(head.val , end = " ")
        head = head.next
    print("\n")


def deletehead(head):
    if head == None:
        return head
    else:
        head = head.next
        return head
    
def deletetail(head):
    if head == None:
        return None
    curr = head
    while curr.next.next:
        curr = curr.next
    curr.next = None
    return head

def deleteKth(head,k):
    if head == None:
        return head
    if k==1:
        return deletehead(head)
    count = 0
    curr = head
    while(count < k-2):
        if curr:
            curr= curr.next
            count+=1
        else:
            return head
    if curr.next == None:
        return head
    if curr.next.next:
        curr.next = curr.next.next
        return head
    else:
        curr.next = None
        return head
    return head

def inserthead(head , k):
    new_node = Node(k)
    if head == None:
        head = new_node
        return head
    else:
        new_node.next = head
        return new_node
    
def inserttail(head,k):
    new_node = Node(k)
    if head == None:
        head = new_node
        return head
    else:
        curr = head
        while(curr.next != None):
            curr = curr.next
        curr.next = new_node
        return head
    

def insertkth(head,k,val):
    if k< 1:
        return head
    new_node = Node(val)
    if head == None :
        head = new_node
        return head
    if k ==1:
        return inserthead(head, val)
    count = 0
    curr = head
    while(count < k-2):
        if curr:
            curr = curr.next
            count+=1
        else:
            return head
    if curr:
        new_node.next = curr.next
        curr.next = new_node
        return head
        


# function calls 
head = ll(arr)
traverse(head)    
head = deletehead(head)
print("After deleting head:")
traverse(head)
head = deletetail(head)
print("After deleting tail:")
traverse(head)
head = deleteKth(head,2)
print("After deleting 2nd element:")
traverse(head)
head = inserthead(head,50)
print("After inserting 50 at head:")
traverse(head)
head = inserttail(head,33)
print("After inserting 33 at tail:")
traverse(head)
head = insertkth(head, 0, 99)
print("After inserting 99 at 10th position:")
traverse(head)




