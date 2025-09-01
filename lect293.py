#  minimum num of platform required in railway station 

arr = list(map(int,input().split()))

dept = list(map(int , input().split()))

#  brute approach

# def function(arr , dept):
#     maxcount = 0 
#     for i in range(len(arr)):
#         count = 1
#         for j in range(i+1,len(arr)):
#             if (arr[i] <= dept[j] and arr[j] <= dept[i]):
#                 count+=1
#             maxcount = max(maxcount , count)
#     return maxcount

# print(function(arr , dept))

#  optimal approach 

def function(arr , dept):
    arr.sort()
    dept.sort()
    i = 0
    j = 0
    count = 0
    maxcount = 0
    while(i<len(arr)):
        if arr[i] < dept[j]:
            count +=1
            i+=1
        else:
            count = count -1
            j +=1
        maxcount = max(maxcount , count)
    return maxcount

print(function(arr,dept))