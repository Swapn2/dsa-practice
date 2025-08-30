


#  count the number of nice subarray

arr = list(map(int,input().split()))
k = int(input())

def function(arr,goal):

    l = 0
    r = 0
    sum = 0 
    count = 0
    while(r < len(arr)):
        sum = sum + arr[r]%2
        while(sum > goal):
            sum = sum - arr[l]%2
            l+=1
        count = count + (r-l+1)
        r+=1
    return count

print(function(arr,k))

