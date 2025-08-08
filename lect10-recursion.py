#  combination sum

def combination_sum(index , arr,target,ds):
    if index == len(arr) or target <0:
        if target ==0:
            print(ds)
        return
    if (arr[index]<= target):
        ds.append(arr[index])
        combination_sum(index,arr,target-arr[index],ds)
        ds.pop()
    combination_sum(index+1,arr, target,ds)



arr = list(map(int ,input().split()))
total = int(input())
l = []
combination_sum(0,arr,total,l)

# other way 


# def combination_sum(index , arr,target,ds,ans):
#     if index == len(arr) or target <0:
#         if target ==0:
#             ans.append(ds.copy())
#         return
#     if (arr[index]<= target):
#         ds.append(arr[index])
#         combination_sum(index,arr,target-arr[index],ds,ans)
#         ds.pop()
#     combination_sum(index+1,arr, target,ds,ans)




# arr = list(map(int ,input().split()))
# total = int(input())
# l = []
# ans = []
# combination_sum(0,arr,total,l,ans)
# print(ans)