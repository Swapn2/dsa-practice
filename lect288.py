#  jump game 2 

arr = list(map(int,input().split()))


# # brute approach


# def function(index , jumps ,arr):
#     if (index >= len(arr)-1):
#         return jumps
#     mini = float('inf')
#     for i in range(1,arr[index]+1):
#         mini = min(mini , function(index+i , jumps+1,arr))
#     return mini

# print(function(0,0,arr))


# optimal approach 

def function(arr):
    jumps = 0 
    l = 0 
    r = 0 
    while(r<len(arr)-1):
        farthest = 0
        for i in range(l ,r+1):
            farthest = max(i+arr[i], farthest)
        l = r+1
        r = farthest
        jumps +=1
    return jumps

print(function(arr))