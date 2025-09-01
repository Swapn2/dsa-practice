
# insert interval 

arr = eval(input())
print(arr)
newinterval = eval(input())
print(newinterval)

def function(arr, newinterval):
    res = []
    i = 0 
    while(i < len(arr) and arr[i][1] < newinterval[0]):
        res.append(arr[i])
        i+=1
    while(i < len(arr) and arr[i][0] <newinterval[1]):
        newinterval[0] = min(newinterval[0] , arr[i][0])
        newinterval[1] = max(newinterval[1], arr[i][1])
        i+=1
    res.append(newinterval)
    while(i<len(arr)):
        res.append(arr[i])
        i+=1
    return res

print(function(arr, newinterval))
