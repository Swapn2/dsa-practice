#  maximum consecutive ones 1111 pr () longest subarray with atmost k zeros )

arr =  list(map(int,input().split()))
k = int(input())
#  brute appraoch 
# maxlen= 0
# for i in range(len(arr)):
#     zeros = 0
#     for j in range(i,len(arr)):
#         if zeros >k:
#             break
#         if arr[j] == 0:
#             zeros +=1
#         else:
#             maxlen = max(maxlen, j-i+1)
# print(maxlen)


#  better approach 

# def con1(arr,k):
#     l =0 
#     r =0 
#     maxlen = 0
#     zero = 0
#     while(r<len(arr)):
#         if arr[r] ==0:
#             zero+=1
#         while zero >k:
#             if arr[l] ==0:
#                 zero -=1
#             l +=1
#         if zero <=k:
#             leng = r-l+1
#         maxlen = max(maxlen,leng)
#         r+=1
#     return maxlen

# print(con1(arr,k))

#  optimal approach 

def con1(arr,k):
    l= 0 
    r = 0 
    maxlen = 0 
    zero = 0 
    while(r<len(arr)):
        if arr[r] ==0:
            zero +=1
        if zero >k:
            if arr[l] ==0:
                zero -=1
            l+=1
        if zero <= k:
            leng = r-l+1
        maxlen = max(maxlen,leng)
        r+=1
    return maxlen
print(con1(arr,k))