#  binary search on answer 
#  find the sqrt of the integer 

# def sqrt(n):
#     ans = -1
#     for i in range(n+1):
#         if i*i <= n:
#             ans = i
#         else:
#             break
#     return ans 
        

#  BS approach 

def sqrt(n):
    ans = -1 
    low = 1 
    high = n
    while( low <= high ):
        mid = (low+high)//2
        if mid*mid <= n:
            low = mid+1
            ans = mid
        elif mid*mid >n:
            high = mid -1
    return ans
        

k = int(input())        
print(sqrt(k))