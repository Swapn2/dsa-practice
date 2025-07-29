#  median of two sorted array optimal appraoch 


def median(arr1,arr2):
    if len(arr1) > len(arr2):
        return median(arr2, arr1)
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