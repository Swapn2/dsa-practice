
#  maximum point you can obtain from card (either i can choose from right or either from left )

arr = list(map(int,input().split()))
k = int(input())

lsum = 0 
rsum = 0 
maxsum =0 
for i in range(k):
    lsum = lsum + arr[i]
maxsum = lsum
rindex = len(arr)-1
for i in range(k-1 , -1 ,-1):
    lsum = lsum - arr[i]
    rsum = rsum +arr[rindex]
    rindex = rindex -1
    maxsum = max(maxsum, lsum+rsum)
    
print(maxsum)



