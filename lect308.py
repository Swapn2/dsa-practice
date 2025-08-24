#  larget rectangle in histogram 

arr = list(map(int , input().split()))

#  brtue approach 
def findnse(arr):
    nse = [0]*len(arr)
    st =[]
    for i in range(len(arr)-1,-1,-1):
        while(len(st)!=0 and arr[st[-1]] >= arr[i]):
            st.pop()
        if len(st) == 0:
            nse[i] = len(arr)
        else:
            nse[i] = st[-1]
        st.append(i)
    return nse


def findpsee(arr):
    psee = [0]*len(arr)
    st = []
    for i in range(len(arr)):
        while len(st) !=0 and arr[st[-1]] > arr[i]:
            st.pop()
        if len(st) ==0:
            psee[i] = -1
        else:
            psee[i] = st[-1]
        st.append(i)
    return psee

def LR(arr):
    nse = findnse(arr)
    psee = findpsee(arr)
    maxi =0
    for i in range(len(arr)):
        maxi = max(maxi, (arr[i]*(nse[i] - psee[i] -1)))
    return maxi


#  optimal approach 

def lr(arr):
    maxarea = 0
    st = []
    
    for i in range(len(arr)):
        while len(st) != 0 and arr[st[-1]] > arr[i]:
            element = st.pop()
            if len(st) == 0:
                pse = -1
            else:
                pse = st[-1]
            nse = i
            maxarea = max(maxarea, arr[element] * (nse - pse - 1))
        st.append(i)

    # now clear remaining stack
    while len(st) != 0:
        element = st.pop()
        if len(st) == 0:
            pse = -1
        else:
            pse = st[-1]
        nse = len(arr)
        maxarea = max(maxarea, arr[element] * (nse - pse - 1))

    return maxarea

    
        




print(LR(arr))
print(lr(arr))
