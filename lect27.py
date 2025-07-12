#  next permuation

def next_permutation(arr):
    index = -1
    n = len(arr)
    for i in range(n-2 ,-1,-1 ):
        if arr[i] < arr[i+1]:
            index = i
            break
    if index == -1:
        reverse(arr, 0, n-1)
        return arr
    for i in range(n-1,-1,-1):
        if arr[i] > arr[index]:
            arr[i],arr[index] = arr[index],arr[i]
            break
    reverse(arr, index+1, n-1)
    return arr

def reverse(arr,start ,end):
    while start < end:
        arr[start] , arr[end] = arr[end]  , arr[start]
        start +=1
        end -=1
    return arr 



arr = list(map(int, input().split()))
n = len(arr)-1
print(next_permutation(arr))