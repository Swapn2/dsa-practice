
#  remove k digits so that resulted number would be smallest 

s = input()

def removekdigit(s,k):
    st =[]
    for i in range(len(s)):
        while (len(st) != 0 and k>0 and int(st[-1]) > int(s[i])):
            st.pop()
            k = k-1
        st.append(s[i])
    while(k>0 and len(st)!=0):
        st.pop()
        k-=1
    if len(st) ==0:
        return "0"
    res = ""
    res = "".join(st)
    res = res.lstrip("0")

    if res == "":
        return "0"
    return res

print(removekdigit("1432219", 3))   # expected "1219"
print(removekdigit("10200", 1))     # expected "200"
print(removekdigit("10", 2))        # expected "0"
