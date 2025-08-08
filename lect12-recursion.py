#  sum subset 1 :

def sum_subset(index , arr, sum ,ans):
    if index == len(arr):
        ans.append(sum)
        return 
    sum+=arr[index]
    sum_subset(index+1,arr,sum,ans)
    sum-=arr[index]
    sum_subset(index+1,arr,sum,ans)


arr = list(map(int, input().split()))
sum = 0
ans = []
sum_subset(0, arr, sum, ans)
ans.sort()
print(ans)


