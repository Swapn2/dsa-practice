# #   subset sum 2:

# def print_subsequence(index, l , arr,ans):
#     if index >= len(arr):
#         ans.add(tuple(l))
#         return 
#     l.append(arr[index])
#     print_subsequence(index+1, l ,arr,ans)
#     l.pop()
#     print_subsequence(index+1 , l , arr,ans)

# arr = list(map(int,input().split()))
# arr.sort()
# ans = set()
# l = []
# print_subsequence(0,l,arr,ans)
# print(list(ans))

#  optimal way to print subsequences with duplicates handled
def print_subsequences(index, arr, l, ans):
    ans.append(l.copy())  # Add current subsequence

    for i in range(index, len(arr)):
        if i > index and arr[i] == arr[i-1]:
            continue
        l.append(arr[i])
        print_subsequences(i + 1, arr, l, ans)
        l.pop()

arr = list(map(int, input().split()))
arr.sort()
ans = []
print_subsequences(0, arr, [], ans)
print(ans)

