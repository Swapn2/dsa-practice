# #  find the missing and repeating elements in an array
# def find_missing_and_repeating(arr):
#     missing = -1
#     repeating = -1
#     n = len(arr)
#     for i in range(1,n+1):
#         count = 0
#         for j in range(n):
#             if arr[j] == i:
#                 count+=1
#         if count ==2:
#             repeating = i
#         if count == 0:
#             missing = i
#         if repeating != -1 and missing != -1:
#             break
#     return {repeating, missing}


# better approach 
# def find_missing_and_repeating(arr):
#     repeating = -1
#     missing = -1
#     hash = [0]*(len(arr)+1)
#     for i in range(len(arr)):
#         hash[arr[i]] += 1
#     for i in range(1,len(hash)):
#         if hash[i] ==2:
#             repeating = i
#         if hash[i] == 0:
#             missing = i
#     print(hash)
# return {repeating,missing}


#  optimal approach 
# def find_missing_and_repeating(arr):
#     n= len(arr)
#     sum = 0
#     sum2 = 0
#     sumn = 0
#     sum2n= 0

#     for i in range(n):
#         sum = sum+arr[i]
#     for i in range(n):
#         sum2 = sum2 + arr[i]**2
#     sumn = int(n*(n+1)/2)
#     for i in range(1,n+1):
#         sum2n = sum2n + i**2
#     m = sum - sumn     # x - y
#     n = sum2 - sum2n   # x2 - y2

#     x_plus_y = n//m  # x+y
#     x = (m + n//m)//2
#     y = n//m -x

#     return {x,y}


# #  optimal approach 


def find_missing_and_repeating(arr):
    n = len(arr)
    xor1 = 0

    # Step 1: XOR all array elements and numbers from 1 to n
    for i in range(n):
        xor1 = xor1 ^ arr[i]

    for i in range(1, n + 1):
        xor1 = xor1 ^ i

    # xor1 = missing ^ repeating

    # Step 2: Find rightmost set bit
    set_bit = xor1 & -xor1

    x = 0  # One of the numbers (missing or repeating)
    y = 0  # The other one

    # Step 3: Divide elements into two groups
    for i in range(n):
        if arr[i] & set_bit:
            x = x ^ arr[i]
        else:
            y = y ^ arr[i]

    for i in range(1, n + 1):
        if i & set_bit:
            x = x ^ i
        else:
            y = y ^ i
    return {x,y}

    # # Step 4: Check which is repeating
    # if arr.count(x) == 2:
    #     return (x, y)  # x is repeating, y is missing
    # else:
    #     return (y, x)  # y is repeating, x is missing


    

arr = list(map(int,input().split()))
print(find_missing_and_repeating(arr))
            

