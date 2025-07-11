#  best time to sell and buy stocks DP
def profit(arr):
    minimal = arr[0]
    profit = 0
    for i in range(1, len(arr)):
        cost = arr[i] - minimal
        profit = max(cost,minimal)
        minimal = min(minimal , arr[i])
    return profit

arr = list(map(int , input().split()))
print(profit(arr))
