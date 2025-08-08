#  printing subsequences ( recursion on subsequences)

def print_subsequence(index, l , arr):
    if index >= len(arr):
        print(l)
        return 
    l.append(arr[index])
    print_subsequence(index+1, l ,arr)
    l.pop()
    print_subsequence(index+1 , l , arr)


arr = list(map(int,input().split()))
arr.sort()
l = []
print_subsequence(0,l,arr)