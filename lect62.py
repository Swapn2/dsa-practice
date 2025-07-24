#  allocate books 
#  read the PS with notes 
# desclaimer is that its logic is similar to shiping pacakge problem 
#  so answer range (max(arr)  to   sum(arr))

# def minPages(arr,students):
#     n = sum(arr)
#     k = max(arr)
#     for i in range(k, n+1):
#         if allocation(arr,i) == students:
#             return i
#     return -1
        
def allocation(arr, pages):
    sumpage = 0
    stu =1
    for i in range(len(arr)):
        if arr[i] + sumpage > pages:
            stu +=1
            sumpage =0
        sumpage +=arr[i]
    return stu



# BS approach 

def minPages(arr,students):
    low = max(arr)
    high = sum(arr)
    ans = -1
    while(low <= high):
        mid = (low+high)//2
        if allocation(arr,mid) <= students:
            ans = mid
            high = mid -1
        else:
            low = mid+1
    return ans 




arr = list(map(int,input().split()))
students = int(input())
print(minPages(arr,students))