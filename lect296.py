#  candy 

arr = list(map(int,input().split()))

# def function(arr):
#     left = [-1]*len(arr)
#     right = [-1]*len(arr)
#     left[0] = 1
#     right[len(arr)-1] = 1

#     for i in range(1, len(arr)):
#         if arr[i] > arr[i-1]:
#             left[i] = left[i-1] +1
#         else:
#             left[i] = 1
#         for i in range(len(arr)-2 , -1,-1):
#             if arr[i] > arr[i+1]:
#                 right[i] = right[i+1] +1
#             else:
#                 right[i] = 1
#         sum = 0
#         for i in range(len(arr)):
#             sum += max(left[i] , right[i])
#     return sum

# print(function(arr))

#  optimal approach 

def function(arr):

    sum = 1
    i = 1
    while(i<len(arr)):
        if arr[i] == arr[i-1]:
            sum = sum+1
            i+=1
            continue
        peak = 1
        while(i<len(arr) and arr[i] > arr[i-1]):
            peak +=1
            sum +=peak
            i+=1
        down = 1
        while(i<len(arr) and arr[i] < arr[i-1]):
            sum += down
            i+=1
            down+=1
        if down > peak:
            sum += (down-peak)
    return sum 
    
print(function(arr))


 