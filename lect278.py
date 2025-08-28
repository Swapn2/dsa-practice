# number of substring containing all three characters 
 
s = input()
# count =0

# for i in range(len(s)):
#     hash = [0]*3
#     for j in range(i,len(s)):
#         hash[ord(s[j]) - ord('a')] =1
#         if (hash[0] + hash[1] +hash[2] == 3):
#             count +=1
# print(count)

#  slight btter 

# for i in range(len(s)):
#     hash = [0]*3
#     for j in range(i,len(s)):
#         hash[ord(s[j]) - ord("a")] =1 
#         if (hash[0] +hash[1] + hash[2]) == 3:
#             count = count + len(s) - j
#             break
# print(count)


#  optimal approach 

def function(s):
    lastseen = [-1,-1,-1]
    count = 0
    for i in range(len(s)):
        lastseen[ord(s[i]) - ord("a")] = i
        if lastseen[0] != -1 and lastseen[1] != -1 and lastseen[2] != -1:
            count += min(lastseen) +1
    return count

print(function(s))