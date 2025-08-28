#  longrdt substring with atmost k distinct characters
from collections import defaultdict
s = input()
k = int(input())

# def function(s,k):
#     maxlen = 0 
#     map = defaultdict(int)
#     for i in range(len(s)):
#         map.clear()
#         for j in range(i,len(s)):
#             map[ord(s[j])] +=1
#             if len(map) <= k:
#                 maxlen = max(maxlen, j-i+1)
#             else:
#                 break
#     return maxlen

# print(function(s,k))

#  better approach 

# def function(s,k):
#     maxlen = 0
#     l = 0 
#     r = 0 
#     map = defaultdict(int)
#     while(r<len(s)):
#         map[ord(s[r])] +=1
#         while(len(map) > k):
#             map[ord(s[l])] -=1
#             if map[ord(s[l])] ==0:
#                 del map[ord(s[l])]
#             l+=1
#         if len(map) <= k:
#             maxlen = max(maxlen , r-l+1)
#         r+=1
#     return maxlen 

# print(function(s,k))


#  optimal approach 

def function(s,k):
    maxlen = 0
    l = 0 
    r = 0 
    map = defaultdict(int)
    while(r<len(s)):
        map[ord(s[r])] +=1
        if(len(map) > k):
            map[ord(s[l])] -=1
            if map[ord(s[l])] ==0:
                del map[ord(s[l])]
            l+=1
        if len(map) <= k:
            maxlen = max(maxlen , r-l+1)
        r+=1
    return maxlen 

print(function(s,k))
