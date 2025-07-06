#  Quick sort 


def partition(arr, low, high):
    pivot = arr[low]
    i = low
    j = high
    while i < j:
        while (i <= high and arr[i] < pivot):
            i +=1 
        while (j>= low and arr[j] > pivot):
            j-=1
        if i < j:
            arr[i],arr[j] = arr[j] , arr[i]
    pivot , arr[j] = arr[j] , pivot
    return j

def qS(arr, low, high):
    if (low < high):
        pindex = partition(arr , low , high)
        qS(arr, low , pindex -1)
        qS(arr , pindex +1 , high)

def quick_sort(arr):
    qS(arr, 0 , len(arr)-1)
    return arr

arr = list(map(int, input().split()))
print(arr)
print(quick_sort(arr))