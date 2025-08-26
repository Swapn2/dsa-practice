#  sum of subarray ranges 

arr = list(map(int, input().split()))

#  brute approach 

sum = 0 
for i in range(len(arr)):
    large = arr[i]
    small = arr[i]
    for j in range(i+1, len(arr)):
        large = max(large,arr[j])
        small = min(small,arr[j])
        sum = sum + (large - small)
print(sum)


#  optimal approach 

def findnse(arr):
    nse = [0]*len(arr)
    st = []
    for i in range(len(arr)-1,-1,-1):
        while(len(st)!=0 and arr[st[-1]] >= arr[i]):
            st.pop()
        if len(st)==0:
            nse[i] = len(arr)
        else:
            nse[i] = st[-1]
        st.append(i)
    return nse

def findpsee(arr):
    psee = [0]*len(arr)
    st = []
    for i in range(len(arr)):
        while(len(st)!=0 and arr[st[-1]] > arr[i]):
            st.pop()
        if len(st)==0:
            psee[i] = -1
        else:
            psee[i] = st[-1]
        st.append(i)
    return psee

def sum_min_subarray(arr):
    total = 0
    nse = findnse(arr)
    psee = findpsee(arr)
    for i in range(len(arr)):
        left = i - psee[i]
        right = nse[i] - i
        total = total + (left *right*arr[i])
    return total


def findnge(arr):
    nge = [0]*len(arr)
    st = []
    for i in range(len(arr)-1,-1,-1):
        while(len(st)!=0 and arr[st[-1]] <= arr[i]):
            st.pop()
        if len(st)==0:
            nge[i] = len(arr)
        else:
            nge[i] = st[-1]
        st.append(i)
    return nge

def findpgee(arr):
    pgee = [0]*len(arr)
    st = []
    for i in range(len(arr)):
        while(len(st)!=0 and arr[st[-1]] < arr[i]):
            st.pop()
        if len(st)==0:
            pgee[i] = -1
        else:
            pgee[i] = st[-1]
        st.append(i)
    return pgee

def sum_max_subarray(arr):
    total = 0
    nse = findnge(arr)
    psee = findpgee(arr)
    for i in range(len(arr)):
        left = i - psee[i]
        right = nse[i] - i
        total = total + (left *right*arr[i])
    return total


def sum_range_subarray(arr):
    sum = 0 
    x = sum_max_subarray(arr)
    y = sum_min_subarray(arr)
    return x-y

print(sum_range_subarray(arr))