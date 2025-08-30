



#  longest repeating character replacement
s = input()
k = int(input())

maxf = 0
maxlen = 0 
for i in range(len(s)):
    hash = [0]*26
    for j in range(i,len(s)):
        hash[ord(s[j]) - ord("A")] +=1
        maxf = max(maxf, hash[ord(s[j]) - ord("A")])
        changes= j-i+1 - maxf
        if changes <= k:
            maxlen = max(maxlen , j-i+1)
        else:
            break
print(maxlen)



# def function(s,k):
#     l = 0
#     r = 0 
#     maxlen = 0
#     hash = [0]*26
#     maxfreq = 0
#     while(r< len(s)):
#         hash[ord(s[r]) - ord("A")] +=1
#         maxfreq = max(maxfreq , hash[ord(s[r]) - ord("A")])
#         if(((r-l+1) - maxfreq) > k):
#             hash[ord(s[l]) -ord("A")] -=1
#             l+=1
#         if (((r-l+1) - maxfreq) <= k):
#             maxlen = max(maxlen , r-l+1)
#         r+=1
#     return maxlen

# print(function(s,k))
