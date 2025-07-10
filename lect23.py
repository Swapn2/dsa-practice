# #  majority element > n/2 times 


# def majority(arr):
#     n = len(arr)//2
#     for i in range(len(arr)):
#         count = 0 
#         for j in range(len(arr)):
#             if arr[i] == arr[j]:
#                 count +=1
#         if count > n:
#             return arr[i]
# arr = list(map(int , input().split()))
# print(majority(arr)) 

# #  better approach 
# from collections import deafultdict
# def majority(arr):
#     n = len(arr)//2
#     hash = deafultdict(int)

#     for i in arr:
#         hash[i] +=1
#     for key in hash:
#         if hash[key] > n:
#             return key
# 

# optimal approach Moores voting algorithm 

def majority(arr):
    el = 0
    count = 0
    n = len(arr)//2
    for i in range(len(arr)):
        if count ==0:
            el = arr[i]
            count = 1
        elif arr[i] == el:
            count +=1
        else:
            count -=1
    occur = 0
    for i in range(len(arr)):
        if arr[i] == el:
            occur +=1
    if occur > n:
        return el
    
arr = list(map(int, input().split()))
print(majority(arr))