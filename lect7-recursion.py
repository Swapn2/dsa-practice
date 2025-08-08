# printing sequences where sum is k 

def print_subsequences(index , l , arr,sum,total):
    if index == len(arr):
        if sum == total:
            print(l)
        return 
    l.append(arr[index])
    sum += arr[index]
    print_subsequences(index+1, l , arr,sum,total)
    l.pop()
    sum -= arr[index]
    print_subsequences(index+1 , l , arr, sum ,total)


arr = list(map(int ,input().split()))
arr.sort()
total = int(input())
l = []
print_subsequences(0, l, arr, 0, total)



#  print any subsequence where sum is k not all need to print :
#  technique to print the answer 

# printing sequences where sum is k 

# def print_subsequences(index , l , arr,sum,total):
#     if index == len(arr):
#         if sum == total:
#             print(l)
#             return True
#         else:
#             return False
#     l.append(arr[index])
#     sum += arr[index]
#     if (print_subsequences(index+1, l , arr,sum,total) == True):
#         return True
#     l.pop()
#     sum -= arr[index]
#     if (print_subsequences(index+1 , l , arr, sum ,total)== True):
#         return True
#     return False


#  count the subsequences where sum is k

# def print_subsequences_count(index , l , arr,sum ,total):
#     if index == len(arr):
#         if sum == total:
#             return 1
#         else:
#             return 0
#     l.append(arr[index])
#     sum += arr[index]
#     left = print_subsequences_count(index+1,l,arr,sum,total)
#     l.pop()
#     sum -= arr[index]
#     right = print_subsequences_count(index+1 , l, arr,sum,total)
#     return left+right




# arr = list(map(int ,input().split()))
# total = int(input())
# l = []
# print(print_subsequences_count(0, l, arr, 0, total))