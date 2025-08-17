def decimal_to_binary(n):
    result = ""
    while(n >1):
        if n%2 ==1:
            result = result + '1'
        else:
            result = result + '0'
        n = int(n/2)
    result = result +str(n)
    return result[::-1]

# Power set(print all subsets)

arr = list(map(int,input().split()))

subset = 1<<len(arr)
ans = []
for num in range(subset):
    list =[]
    for i in range(len(arr)):
        if (num&(1<<i)):
            list.append(arr[i])
    ans.append(list)
print(ans)

