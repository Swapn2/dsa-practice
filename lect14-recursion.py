# print all permutation of string 

def permute(arr,ds,ans,map):
    if len(ds) == len(arr):
        ans.append(ds.copy())
        return
    for i in range(len(arr)):
        if i not in map:
            map[i] = 1
            ds.append(arr[i])
            permute(arr,ds,ans,map)
            ds.pop()
            del map[i]

arr = list(map(str, input().split()))
ans = []
map = {}
permute(arr, [], ans, map)
print(ans)