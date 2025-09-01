# valid parenthesis string 

s = input()
index = 0 
count = 0
#  brute approach 

# def function(s,index , count ):
#     if count < 0 : return False
#     if index ==len(s):
#         return count ==0
#     if s[index] == "(":
#         return function(s,index+1,count+1)
#     if s[index] == ")":
#         return function(s,index+1,count-1)
#     return function(s,index+1,count+1) or function(s,index+1, count-1) or function(s,index+1 , count)

# print(function(s,index , count))

#  optimal approach 

def function(s):
    min = 0
    max = 0
    for i in range(len(s)):
        if (s[i] == "("):
            min = min+1
            max = max+1
        elif (s[i] == ")"):
            min = min -1
            max = max +1
        else:
            min = min -1 
            max = max+1
        if min < 0:
            min = 0
        if max < 0:
            return False
    return min == 0
    
print(function(s))