#  jump Game 

arr = list(map(int, input().split()))

def function(arr):
    maxindex = 0
    for i in range(len(arr)):
        if i > maxindex:
            return False
        else:
            maxindex = max(maxindex , i+arr[i])
    return True

print(function(arr))