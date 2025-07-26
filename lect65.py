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

import heapq

n = int(input())

items = []

for _ in range(n):
    p,v = map(int,input().split())
    items.append((p,v))
pq = []

for p,v in items:
    heapq.heappush(pq,(p,-v))
while pq:
    p,neg_v = heapq.heappop(pq)
    print(p,-neg_v)