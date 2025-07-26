#  median of two sorted array 
# brute approach 

# def median(arr1,arr2):
#     n1= len(arr1)
#     n2 = len(arr2)
#     left =0
#     right = 0
#     ans = []
#     while(left<n1 and right < n2):
#         if(arr1[left] <= arr2[right]):
#             ans.append(arr1[left])
#             left+=1
#         else:
#             ans.append(arr2[right])
#             right +=1
#     while(left<n1):
#         ans.append(arr1[left])
#         left+=1
#     while(right<n2):
#         ans.append(arr2[right])
#         right+=1
#     if((n1+n2)%2 ==1):
#         return ans[(n1+n2)//2]
#     else:
#         i = int((n2+n1)/2)
#         med = (ans[i]+ans[i-1])/2
#         return med

#  better approach 
# def median(arr1,arr2):
#     el1 = -1
#     el2 = -1
#     n1 = len(arr1)
#     n2 = len(arr2)
#     idx1 = (n1+n2)//2
#     # print(idx1)
#     idx2 = idx1-1
#     left = 0
#     right = 0
#     count =0
#     while(left <n1 and right <n2):
#         if(arr1[left]<= arr2[right]):
#             if idx1 == count: el1 = arr1[left]
#             if idx2 == count: el2 = arr1[left]
#             left += 1
#             count+=1
#         else:
#             if idx1 == count: el1 = arr2[right]
#             if idx2 == count: el2 = arr2[right]
#             count += 1
#             right += 1
#     while(left<n1):
#         if idx1 == count: el1 = arr1[left]
#         if idx2 == count: el2 = arr1[left]
#         count+=1
#         left += 1
#     while(right<n2):
#         if idx1 == count: el1 = arr2[right]
#         if idx2 == count: el2 = arr2[right]
#         count += 1
#         right += 1
#     if (n1+n2)%2 ==1:
#         return el1
#     else:
#         return (el1 + el2)/2

# optimal approach 

def median(arr1,arr2):
    n1 = len(arr1)
    n2 = len(arr2)
    low = 0
    onleft = (n1+n2+1)//2
    high = max(n2,n1)
    while(low <= high):
        mid1 = (low+high)//2
        mid2 = onleft - mid1
        l1, l2, r1, r2 = float('-inf'), float('-inf'), float('inf'), float('inf')
        if mid1-1 >= 0:
            l1 = arr1[mid1-1]
        if mid2 -1 >=0:
            l2 = arr2[mid2-1]
        if mid1 <n1:
            r1 = arr1[mid1]
        if mid2 <n2:
            r2 = arr2[mid2]
        if (l1<= r2 and l2<= r1):
            print(l1,l2,r1,r2)
            if((n1+n2)%2 ==0):
                med = (max(l1,l2)+ min(r1,r2))/2
                return med
            else:
                return max(l1,l2)
        elif (l2 >r1):
            low = mid1+1
        else:
            high = mid1-1



arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))
print(median(arr1,arr2))