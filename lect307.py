#  asteriod collision

arr = list(map(int,input().split()))

def war(arr):
    st = []
    for i in range(len(arr)):
        if arr[i] > 0:
            st.append(arr[i])
        else:
            while(len(st)!=0 and st[-1] >0 and st[-1] < abs(arr[i])):
                st.pop()
            if len(st) != 0 and st[-1] == abs(arr[i]):
                st.pop()
            elif len(st)==0 or st[-1]< 0:
                st.append(arr[i])
    return st

print(war(arr))