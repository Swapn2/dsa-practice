# #  rearrange the elements ( alternate sign order )

# def rearrange(arr):
#     n = len(arr)//2
#     pos =[]
#     neg = []
#     for i in range(len(arr)):
#         if arr[i] <0:
#             neg.append(arr[i])
#         else:
#             pos.append(arr[i])
#     print(pos)
#     print(neg)
#     for i in range(n):
#         arr[2*i] = pos[i]
#         arr[(2*i+1)] = neg[i]
#     return arr

# arr = list(map(int,input().split()))
# print(rearrange(arr))

# # #  rearrange the elements ( alternate sign order )
# def rearrange(arr):
#     ans = [0]*len(arr)
#     odd = 1
#     eve = 0
#     for i in range(len(arr)):
#         if arr[i] <0:
#             ans[odd] = arr[i]
#             odd +=2
#         elif arr[i] >0:
#             ans[eve] = arr[i]
#             eve +=2
#     return ans

# arr= list(map(int,input().split()))
# print(rearrange(arr))


# 
# # #  rearrange the elements ( alternate sign order ) if no of neg != no of pos 
# def rearrange(arr):
#     pos = []
#     neg =[]
#     n = len(arr)
#     for i in range(n):
#         if arr[i] < 0:
#             neg.append(arr[i])
#         else:
#             pos.append(arr[i])
#     if len(pos) < len(neg):
#         for i in range(len(pos)):
#             arr[2*i]= pos[i]
#             arr[2*i +1] = neg[i]
#         index = 2*len(pos)
#         for i in range(len(pos) ,len(neg)):
#             arr[index] = neg[i]
#             index+=1
#     else:
#         for i in range(len(neg)):
#             arr[2*i]= pos[i]
#             arr[2*i +1] = neg[i]
#         index = 2*len(neg)
#         for i in range(len(neg) ,len(pos)):
#             arr[index] = pos[i]
#             index+=1
#     return arr

# arr = list(map(int,input().split()))
# print(rearrange(arr))

