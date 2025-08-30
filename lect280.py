
#  binary sub array wiht sum k

arr = list(map(int, input().split()))
goal = int(input())


def function(arr,goal):
    l = 0 
    r = 0 
    sum = 0 
    count = 0
    while(r < len(arr)):
        sum = sum + arr[r]
        while(sum > goal):
            sum = sum - arr[l]
            l+=1
        count = count + r-l+1
        r+=1
    return count


x = function(arr,goal)
y = function(arr,goal-1)
print(x-y)

