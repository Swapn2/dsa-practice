# class starray:
#     def __init__(self,size):
#         self.top = -1
#         self.size= size
#         self.arr= [None]*size

#     def push(self,item):
#         if self.top < self.size:
#             self.top +=1
#             self.arr[self.top] = item
#         else:
#             print("stack overflow")
#     def pop(self):
#         if self.top >=0:
#             val = self.arr[self.top]
#             self.top -=1
#             return val
#         else:
#             print("stack underflow")
#     def peek(self):
#         val = self.arr[self.top]
#         return val
    
    
# s = starray(5)
# s.push(10)
# s.push(1)
# s.push(2)
# print(s.peek())
# print(s.pop())
# print(s.peek())


#  queue using array 

# class Queue:
#     def __init__(self,size):
#         self.size = size 
#         self.front = -1
#         self.rear = -1 
#         self.currsize = 0
#         self.arr = [None]*size
    
#     def push(self,item):
#         if self.currsize ==0:
#             self.front +=1
#             self.rear +=1
#             self.arr[self.rear] = item
#             self.currsize +=1
#         elif self.currsize < self.size:
#             self.rear = (self.rear + 1) % self.size
#             self.arr[self.rear] = item
#             self.currsize +=1
#         else:
#             print("queue overflow")
#     def pop(self):
#         if self.currsize > 0:
#             val = self.arr[self.front]
#             self.front +=1
#             self.currsize -=1
#             print(val)
#         else:
#             print("queue underflow")
#     def peek(self):
#         if self.currsize > 0:
#             print(self.arr[self.front])
#         else:
#             print("queue is empty")


    
# s = Queue(4)
# s.push(3)
# s.push(2)
# s.push(4)
# s.peek()
# s.pop()
# s.pop()
# s.push(2)
# s.push(3)
# s.peek()


#  stack using linked list

# class Node:
#     def __init__(self,data, next = None):
#         self.data = data
#         self.next = next 

# class stack:
#     def __init__(self):
#         self.head = None
#         self.curr = self.head
#         self.size = 0

#     def push(self,item):
#         newnode = Node(item)
#         if self.head == None:
#             self.head = newnode
#             self.curr = self.head
#             self.size+=1
        
#         else:
#             self.curr.next = newnode
#             self.curr = newnode
#             self.size +=1

#     def pop(self):
#         temp = self.head
#         if self.head == None:
#             print("blank")
#         elif(self.head.next == None):
#             val = self.head.data
#             self.head= None
#             self.size-=1
#             print(val)
#             return

#         else:
#             while(temp.next.next):
#                 temp = temp.next
#             val = temp.next.data
#             temp.next = None
#             self.size -=1
#             print(val)
#             return

#     def peek(self):
#         temp = self.head
#         if self.head == None:
#             print("blank")
#         elif(self.head.next == None):
#             print(self.head.data)
#             return
#         else:
#             while(temp.next):
#                 temp = temp.next
#             val = temp.data
#             print(val)
#             return 
        
# s= stack()
# s.push(4)
# s.push(2)
# s.push(3)
# s.push(1)
# print("s",s.size)
# s.peek()
# s.pop()
# print("s",s.size)
# s.pop()
# print("s",s.size)
# s.pop()
# print("s",s.size)
# s.pop()
# print("s",s.size)
# s.push(7)
# print("s",s.size)


#  queue using link list 


class Node:
    def __init__(self,data, next = None):
        self.data = data
        self.next = next 

class Queue:
    def __init__(self):
        self.head = None
        self.curr = self.head
        self.size = 0

    def push(self,item):
        newnode = Node(item)
        if self.head == None:
            self.head = newnode
            self.curr = self.head
            self.size+=1
        
        else:
            self.curr.next = newnode
            self.curr = newnode
            self.size +=1

    def pop(self):
        temp = self.head
        if self.head == None:
            print("blank")
        elif(self.head.next == None):
            val = self.head.data
            self.head= None
            self.size-=1
            print(val)
            return
        else:
            val = temp.data
            self.head = self.head.next
            self.size -=1
            print(val)
            return

    def peek(self):
        temp = self.head
        if self.head == None:
            print("blank")
        elif(self.head.next == None):
            print(self.head.data)
            return
        else:
            val = temp.data
            print(val)
            return 

s= Queue()
s.push(7)
s.push(2)
s.push(3)
s.push(5)
s.pop()
s.peek()
s.pop()
s.pop()
s.peek()




