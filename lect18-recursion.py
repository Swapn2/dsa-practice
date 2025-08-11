#  palindrom string partitioning 

def partition(index, s, ans, ds):
    if index == len(s):
        ans.append(ds.copy())
        return 
    for i in range(index , len(s)):
        if ispalindrome(s,index , i):
            ds.append(s[index:i+1])
            partition(i+1 , s,ans ,ds )
            ds.pop()

def ispalindrome(s,start ,end):
    while(start <= end):
        if s[start] != s[end]:
            return False
        start +=1
        end -=1
    return True


s = input()
ans = []
ds = []
partition(0, s,ans,ds)
print(ans)


    