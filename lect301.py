#  next greater element (monotonic stack)

arr = list(map(int, input().split()))

# nge = []
# for i in range(len(arr)):
#     for j in range(i,len(arr)):
#         if arr[j] > arr[i]:
#             nge.append(arr[j])
#             break
#         elif j == len(arr)-1:
#             nge.append(-1)
# print(nge)


def NGE(arr):

    s = []
    ans = []
    for i in range(len(arr)-1,-1,-1):
        if len(s)==0:
            ans.append(-1)
            s.append(arr[i])
        else:
            if arr[i] < s[-1]:
                ans.append(s[-1])
                s.append(arr[i])
            else:
                while(len(s)!= 0 and s[-1] <= arr[i]):
                    s.pop()
                if len(s)==0:
                    ans.append(-1)
                    s.append(arr[i])
                else:
                    ans.append(s[-1])
                    s.append(arr[i])
    return ans[::-1]

print(NGE(arr))