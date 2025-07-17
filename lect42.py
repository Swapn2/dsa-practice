# #  count inversion (left element > right element)

# def count_inversions(arr):
#     count = 0 
#     for i in range(len(arr)):
#         for j in range(i+1, len(arr)):
#             if arr[i] > arr[j]:
#                 count +=1
#     return count

#  better approach using merge sort
def merge(arr,low,mid,high):
    temp = []
    left = low
    right = mid+1
    while(left <= mid and right <=high):
        if(arr[left] < arr[right]):
            temp.append(arr[left])
            left+=1
        else:
            temp.append(arr[right])
            right +=1
    while(left <=mid):
        temp.append(arr[left])
        left+=1
    while(right <= high):
        temp.append(arr[right])
        right+=1
    for i in range(low, high+1):
        arr[i] = temp[i-low]

def count_pairs(arr, low , mid,high):
    right = mid + 1
    count = 0 
    for left in range(low,mid+1):
        while right <= high and arr[left] > arr[right]:
            right+=1
        count += right -(mid+1)
    return count

def mS(arr, low , high):
    count = 0
    if low>= high:
        return 0
    mid = (low+high)//2
    count += mS(arr,low,mid)
    count += mS(arr,mid+1, high)
    count += count_pairs(arr, low, mid, high)
    merge(arr,low,mid,high)
    return count

def merge_sort(arr):
    count = mS(arr, 0, len(arr)-1)
    return count 




arr= list(map(int, input().split()))
# print(count_inversions(arr))  # Example usage
print(merge_sort(arr))  # Example usage
