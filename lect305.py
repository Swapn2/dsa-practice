#  sum of subarray minimums

arr = list(map(int,input().split()))

#  brute approach 

# sum = 0 
# for i in range(len(arr)):
#     mini = arr[i]
#     for j in range(i, len(arr)):
#         mini = min(mini, arr[j])
#         sum = sum + mini
# print(sum)


#  optimal approach 

def findnse(arr):
    nse = [0]*(len(arr)) 
    st = []
    for i in range(len(arr)-1, -1,-1):
        while len(st)!=0 and arr[st[-1]] >= arr[i]:
            st.pop()
        if len(st) ==0:
            nse[i] = len(arr)
        else:
            nse[i] = st[-1]
        st.append(i)
    return nse

def findpsee(arr):
    psee = [0]*len(arr)
    st = []
    for i in range(len(arr)):
        while len(st)!= 0 and arr[st[-1]] > arr[i]:
            st.pop()
        if len(st)==0:
            psee[i] = -1
        else:
            psee[i] = st[-1]
        st.append(i)
    return psee

def sum(arr):
    nse = findnse(arr)
    psee = findpsee(arr)
    total = 0 
    for i in range(len(arr)):
        left = i - psee[i]
        right = nse[i] - i
        total = total + right*left*arr[i]
    return total

print(sum(arr)) 
print(findnse(arr))
print(findpsee(arr))