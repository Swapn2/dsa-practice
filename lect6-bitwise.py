#  single number 2 

# arr = list(map(int,input().split()))
# ans =0
# for bitindex in range(31):
#     count = 0
#     for i in range(len(arr)):
#         if arr[i]&(1<<bitindex):
#             count += 1
#     if count%3==1:
#         ans = ans|(1<<bitindex)

# print(ans)

#  trick 2 

# arr = list(map(int,input().split()))
# def singlenum(arr):
    
#     for i in range(1,len(arr),3):
#         # print("i : ",i)
#         if arr[i] != arr[i-1]:
#             return arr[i-1]
#     return arr[-1]

# print(singlenum(arr))


#  trick 3 

arr = list(map(int ,input().split()))
ones = 0
twos = 0
for i in range(len(arr)):
    ones = (ones^arr[i])&(~(twos))
    twos = (twos^arr[i])&(~(ones))
print(ones)


