# #  3 sum question 
# #  brute force approach

# def sum3(arr):
#     n = len(arr)
#     ans = []
#     for i in range(n):
#         for j in range(i,n):
#             triplet = []
#             for k in range(j+1,n):
#                 if arr[i] +arr[j]+arr[k] ==0:
#                     triplet.append(arr[i])
#                     triplet.append(arr[j])
#                     triplet.append(arr[k])
#                     triplet.sort()
#                     if triplet not in ans:
#                         ans.append(triplet)
#     return ans


#  better approach 

# def sum3(arr):
#     hash = {}

#     ans = []
#     n = len(arr)
#     i = 0 
#     j = 0
#     while( i < n):
#         j = i+1
#         while j< n:
#             rem = -(arr[i] + arr[j])
#             if rem not in hash:
#                 hash[arr[j]] = arr[j]
#                 j+=1
#             elif rem in hash:
#                 triplet = []
#                 triplet.append(arr[i])
#                 triplet.append(arr[j])
#                 triplet.append(rem)
#                 triplet.sort()
#                 j+=1
#                 if triplet not in ans:
#                     ans.append(triplet)
#         i+=1
#     return ans
                
#   optimal approach 
def sum3(arr):
    arr.sort()
    n = len(arr)
    ans = []
    start = 0

    while start < n - 2:  # At least 3 elements needed
        j = start + 1
        last = n - 1
        while j < last:
            total = arr[start] + arr[j] + arr[last]
            if total > 0:
                last -= 1
            elif total < 0:
                j += 1
            else:
                triplet = [arr[start], arr[j], arr[last]]
                if triplet not in ans:
                    ans.append(triplet)
                # Skip duplicates for j and last
                while j < last and arr[j] == arr[j + 1]:
                    j += 1
                while j < last and arr[last] == arr[last - 1]:
                    last -= 1
                j += 1
                last -= 1
        # Skip duplicates for start
        while start < n - 2 and arr[start] == arr[start + 1]:
            start += 1
        start += 1

    return ans

            



arr = list(map(int, input().split()))
print(sum3(arr))