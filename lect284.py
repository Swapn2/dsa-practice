
#  assing cookies

greed = list(map(int ,input().split()))

size = list(map(int , input().split()))

def function(greed , size ):
    greed.sort()
    size.sort()
    l = 0
    r = 0
    n = len(greed)
    m = len(size)
    while(l<n and r< m):
        if greed[l] <= size[r]:
            l+=1
        r+=1
    return l

print(function(greed , size))
