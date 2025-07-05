# #  hashing

# arr = list(map(int,input().split()))
# print(arr)

# hash = [0]*13 # 13 becoz 12 is the max value in the query 

# # precomputation

# for i in range(6):
#     hash[arr[i]] +=1 

# no_query = int(input())
# while no_query>0:
#     query = int(input())
#     no_query -=1
#     # fetching the value from hash
#     print(hash[query])


# **********************************************************************************

# #  hashing with lower letters string only 

# s = input()
# print(s)

# hash  = [0]* 26
# # precomputation
# for i in range(0,len(s)):
#     hash[ord(s[i]) - ord('a')] +=1

# no_query = int(input())
# while no_query > 0 :
#     query = input()
#     no_query -=1
#     # fetching the value from hash
#     print(hash[ord(query[0]) - ord('a')])

# **************************************************************************************8

# # #  hashing with 256 chara only 
# s = input()
# print(s)

# hash  = [0]* 256
# # precomputation
# for i in range(0,len(s)):
#     hash[ord(s[i])] +=1

# no_query = int(input())
# while no_query > 0 :
#     query = input()
#     no_query -=1
#     # fetching the value from hash
#     print(hash[ord(query[0])])

# *******************************************************************************8

# # #  Hasing by dictionary

# arr = list(map(int,input().split()))
# print(arr)

# from collections import defaultdict
# # pre computation
# hash = defaultdict(int)
# for i in range(len(arr)):
#     hash[arr[i]] +=1
# print(hash)

# no_query = int(input())

# while(no_query > 0 ):
#     query = int(input())
#     no_query -= 1
#     # fetching the value from hash
#     print(hash[query])
 