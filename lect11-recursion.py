
# #  combination sum

# def combination_sum(index , arr,target,ds,ans):
#     if index == len(arr) or target <0:
#         if target ==0:
#             ans.add(tuple(sorted(ds.copy())))
#         return
#     if (arr[index]<= target):
#         ds.append(arr[index])
#         combination_sum(index+1,arr,target-arr[index],ds,ans)
#         ds.pop()
#     combination_sum(index+1,arr, target,ds,ans)




# arr = list(map(int ,input().split()))
# total = int(input())
# l = []
# ans = set()
# combination_sum(0,arr,total,l,ans)
# print(list(ans))


# other way optimal 

def combination_sum(index , target , arr,ans,ds):
    if target ==0:
        ans.append(ds.copy())
        # print(ans)
        return
    for i in range(index ,len(arr)):
        if i > index and arr[i] == arr[i-1]:
            continue
        if (arr[i]>target):
            break
        ds.append(arr[i])
        combination_sum(i+1,target-arr[i], arr,ans,ds)
        ds.pop()
 
arr = list(map(int ,input().split()))
total = int(input())
arr.sort()
print(arr)
l = []
ans = []
combination_sum(0,total,arr,ans,l)
print(ans)