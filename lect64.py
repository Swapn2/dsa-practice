#  built heapq
#  this is most efficient low-level way , it use the min-heap ( i,e; smallest element first)

# import heapq

# pq = []

# heapq.heappush(pq, (3,2))
# heapq.heappush(pq, (3,5))
# heapq.heappush(pq, (1,0))
# heapq.heappush(pq, (2,0))
# heapq.heappush(pq, (4,3))


# print(pq)
# print(pq[0])  # it will give the smallest element but [1] onwards will be unordered
# print(pq[-1])


# max heap if first tie then second in ascending order 

# import heapq

# items = []

# n = int(input())
# for _ in range(n):
#     p,v = map(int,input().split())
#     items.append((p,v))

# pq = []

# for p,v in items:
#     heapq.heappush(pq , (-p,v))

# while pq:
#     neg_p ,v = heapq.heappop(pq)
#     print(-neg_p,v)

#  max heap if first tie then second in Descending order

# import heapq

# items = []

# n = int(input())
# for _ in range(n):
#     p,v = map(int,input().split())
#     items.append((p,v))

# pq = []

# for p,v in items:
#     heapq.heappush(pq , (-p,-v))

# while pq:
#     neg_p, neg_v = heapq.heappop(pq)
#     print(-neg_p, -neg_v)


#  min heap if first tie then second in ascending order

# import heapq

# n= int(input())
# items = []

# for _ in range(n):
#     p,v = map(int,input().split())
#     items.append((p,v))

# pq = []

# for p,v in items:
#     heapq.heappush(pq , (p,v))
# print(pq)
# while pq:
#     p,v = heapq.heappop(pq)
#     print(p,v)

#  # min heap if first tie then second in Descending order

# import heapq

# n = int(input())

# items = []

# for _ in range(n):
#     p,v = map(int,input().split())
#     items.append((p,v))
# pq = []

# for p,v in items:
#     heapq.heappush(pq,(p,-v))
# while pq:
#     p,neg_v = heapq.heappop(pq)
#     print(p,-neg_v)


#  minimize the max distance of gas station

#  brute approach 

# def mindist(arr, k):
#     n = len(arr)
#     howmany = [0]*(n-1)

#     for gasstation in range(1,k+1):
        
#         maxvalue = -1
#         maxindex = -1
#         for i in range(n-1):
#             diff = arr[i+1] - arr[i]
#             sectionlength = diff/(howmany[i]+1)
#             if maxvalue < sectionlength:
#                 maxvalue = sectionlength
#                 maxindex = i
#         howmany[maxindex] +=1 
#     maxans =-1
#     for i in range(n-1):
#         sectionlength = int((arr[i+1] - arr[i])/(howmany[i] +1))
#         maxans = max(maxans,sectionlength)
#     return maxans



# by using heapq

# import heapq
# def mindist(arr,k):

#     n = len(arr)
#     howmany = [0]*(n-1)
#     pq = []

#     for i in range(n-1):
#         heapq.heappush(pq , ((-1)*(arr[i+1]-arr[i]),i))
#     # print(pq)
#     for gasstation in range(1,k+1):
#         neg_p,v = heapq.heappop(pq)

#         howmany[v] +=1 # inserting a station 

#         seclen = (arr[v+1] - arr[v])/(howmany[v]+1)
#         heapq.heappush(pq,((-1)*seclen,v))

#     return pq[0][0]*(-1)
    

# BS approach 
def coutgasstation(arr,dist):
    count = 0
    for i in range(1,len(arr)):
        numberinbetween = int((arr[i]-arr[i-1])/dist)
        if ((arr[i]-arr[i-1]) == numberinbetween*dist):
            numberinbetween -=1
        count +=numberinbetween
    return count

def mindist(arr,k):
    low = 0
    high =0
    n = len(arr)
    for i in range(1,n-1):
        high = max(high, (arr[i+1]-arr[i]))
    diff = 1e-6
    while(high-low > diff):
        mid = (low+high)/2.0
        count = coutgasstation(arr,mid)
        if count > k:
            low = mid
        else:
            high = mid
    return high


arr = list(map(int, input().split()))
k = int(input())

print(mindist(arr,k))
