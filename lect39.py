# #  Merge overlapping intervals

# def merge_intervals(arr):
#     n = len(arr)
#     ans = []
#     arr.sort()
#     ans.append([arr[0][0],arr[0][1]])
#     for i in range(n):
#         start = arr[i][0]
#         end = arr[i][1]

#         if len(ans)!= 0 and end <= ans[-1][1]:
#             continue
#         elif start <= ans[-1][1] and end >= ans[-1][1]:
#             ans[-1][1] = max(ans[-1][1],end)
#         elif start > ans[-1][1]:
#             ans.append([start,end])
#     return ans






row = int(input())
col = int(input())
arr = []
for i in range(row):
    rows = list(map(int , input().split()))
    if len(rows) == col:
        arr.append(rows)
print(arr)
print(merge_intervals(arr))
