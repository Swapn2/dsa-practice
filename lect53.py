#  find peak element arr[i-1] < arr[i] > arr[i+1]

#  brute approach 

def peak_element(arr):
    n = len(arr)

    for i in range(n):
        # if ( i== 0 or arr[i] >arr[i-1]) and  (i == n-1 or arr[i] > arr[i+1]):  not easy to understand LoL
            return arr[i]
    return -1
        

# BS approach 

def peak_element(arr):
    n = len(arr)

    if n==1 : return arr[0]
    if arr[0] > arr[1] : return arr[0]
    elif arr[n-1] > arr[n-2]: return arr[n-1]
    low =1 
    high = n-2
    while(low <= high):
            mid = (low +high)//2
            if arr[mid] > arr[mid+1] and arr[mid] > arr[mid-1]:
                  return arr[mid]
            elif arr[mid] < arr[mid+1]:
                  low = mid+1
            elif arr[mid] > arr[mid+1]:
                  high = mid -1
    return -1  
                  

arr = list(map(int, input().split()))
print(peak_element(arr))