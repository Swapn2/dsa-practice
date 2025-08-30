#  shortest job first 

arr = list(map(int,input().split()))

def function(arr):
    arr.sort()
    wt = 0
    t = 0
    for i in range(len(arr)):
        wt += t
        t += arr[i]
    return int(wt/len(arr))

print(function(arr))

