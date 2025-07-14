# #  majority element > n/3 time 
# def majority_element(arr):
#     ls = []
#     for i in range(len(arr)):
#         if (len(ls) ==0 or ls[0] != arr[i]):
#             count = 0 
#             for j in range(len(arr)):
#                 if arr[j] == arr[i]:
#                     count +=1
#             if count > len(arr)//3:
#                 ls.append(arr[i])
#                 # print(ls[0])
#         if len(ls) == 2:
#             break
#     return ls

from collections import defaultdict

# # better soln
# def majority_element(arr):
#     hash = defaultdict(int)
#     ans = []
#     for i in arr:
#         hash[i] +=1
#         if hash[i] > len(arr)//3:
#             ans.append(i)
#     if len(ans) == 2:
#         return ans
    

# optimal approach 

def majority_element(arr):
    count1 = 0
    count2 = 0
    el1 = None
    el2 = None
    ans =[]
    for i in arr:
        if count1 ==0 and i != el2:
            el1 = i
            count1 = 1
        elif count2 ==0 and i != el1:
            el2 = i
            count2 = 1
        elif i == el1:
            count1 += 1
        elif i == el2:
            count2 += 1
        else:
            count1 -= 1
            count2 -= 1
    count1 = 0
    count2 = 0
    for i in arr:
        if i == el1:
            count1 += 1
        elif i == el2:
            count2 += 1
    if count1 > len(arr)//3:
        ans.append(el1)
    if count2 > len(arr)//3:
        ans.append(el2)
    return ans
        


arr = list(map(int, input().split()))
print(majority_element(arr))
