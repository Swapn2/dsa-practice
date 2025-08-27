#  fruits in the basket 

#  maxlen of a subarray with atmost 2 type of number 

arr = list(map(int,input().split()))
k = int(input())
#  brute appraoch 

# maxlen = 0
# for i in range(len(arr)):
#     st = set()
#     for j in range(i,len(arr)):
#         st.add(arr[j])
#         if len(st) <=k:
#             maxlen = max(maxlen, j-i+1)
#         else:
#             break
# print(maxlen)



#  optimal approach 
from collections import defaultdict
def fruitsinbasket(arr,k):
    l = 0 
    r = 0 
    maxlen = 0 
    d = defaultdict(int)
    while(r<len(arr)):
        d[arr[r]] +=1
        if len(d) > k:
            while( len(d)>k):
                d[arr[l]] -=1
                if d[arr[l]] ==0:
                    del d[arr[l]]
                l+=1
        if len(d) <= k:
            maxlen = max(maxlen ,r-l+1)
        r+=1
    return maxlen

print(fruitsinbasket(arr,k))