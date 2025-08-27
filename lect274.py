#  longest substring without repeating character 

# brute approach 

# s = input()
# maxlen = 0
# for i in range(len(s)):
#     hash = [0]*256
#     for j in range(i,len(s)):
#         if hash[ord(s[j])] ==1:
#             break
#         else:
#             leng = j-i+1
#         maxlen = max(maxlen , leng)
#         hash[ord(s[j])] =1

# print(maxlen)

#  better approach 

s = input()

def func(s):
    hash = [-1]*256
    l = 0
    r = 0
    maxlen = 0
    while(r<len(s)):
        if hash[ord(s[r])] != -1:
            if hash[ord(s[r])] >= l:
                l = hash[ord(s[r])] +1
        leng = r-l+1
        maxlen = max(leng,maxlen)
        hash[ord(s[r])] = r
        r+=1
    return maxlen

