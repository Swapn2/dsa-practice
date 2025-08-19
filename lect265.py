#  prime or not 

n= int(input())

#  brute approach 
count = 0 
for i in range(1,n+1):
    if n%i==0:
        count +=1
if count ==2:
    print("yes")
else:
    print("no")

#  optimal approach 
# import math
# count = 0
# for i in range(2, int(math.sqrt(n))+1):
#     if n%i ==0:
#         count+=1
#         if n/i != 0:
#             count +=1
#     if count >2:
#         break
# if count ==2:
#     print("yes")
# else:
#     print("No")

