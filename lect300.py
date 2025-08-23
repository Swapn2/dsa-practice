#  min stack array :

# class MinStack:
#     def __init__(self):
#         self.st = []
#         self.min = []
#     def push(self, item):
#         self.st.append(item)
#         if len(self.min)==0 or item <= self.min[-1]:
#             self.min.append(item)
#     def pop(self):
#         if len(self.st):
#             x = self.st.pop()
#             if x == self.min[-1]:
#                 self.min.pop()
#     def top(self):
#         return self.st[-1]
#     def getmin(self):
#         return self.min[-1]
    


#  optimal approach 

class MinStack:
    def __init__(self):
        self.st = []
        self.min = None
    def push(self,item):
        if len(self.st)==0:
            self.st.append(item)
            self.min = item
        elif item < self.min:
            self.st.append(2*item - self.min)
            self.min = item
        else:
            self.st.append(item)
    def pop(self):
        if len(self.st)==0:
            return
        x = self.st.pop()
        if x< self.min:
            self.min = 2*self.min -x
    def top(self):
        if len(self.st)==0:
            return 
        x = self.st[-1]
        if (x > self.min): return x
        else:
            return self.min
    def getmin(self):
        return self.min
    



stack = MinStack()

stack.push(5)
stack.push(3)
stack.push(7)
stack.push(2)

print("Current Min:", stack.getmin())
print("Top Element:", stack.top())

stack.pop()
print("Top after pop:", stack.top())
print("Min after pop:", stack.getmin())

stack.pop()
print("Top after pop:", stack.top())
print("Min after pop:", stack.getmin())
