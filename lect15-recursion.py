#  optimal way for gettig permutation

def permute(index,arr,ans):
    if index == len(arr):
        ans.append(arr.copy())
        return 
    for i in range(index , len(arr)):
        arr[index], arr[i] = arr[i], arr[index]
        permute(index + 1, arr, ans)
        arr[index], arr[i] = arr[i], arr[index]



arr = list(map(int, input().split()))
ans = []
permute(0,arr,ans)
print(ans)