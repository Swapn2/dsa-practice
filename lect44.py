# #  Maximun product subarray
# def max_product_subarray(arr):
#     maxi = -int(1e18)
#     for i in range(len(arr)):
#         for j in range(i+1 , len(arr)):
#             product = 1
#             for k in range(i , j+1):
#                 product = product * arr[k]
#             maxi = max(product,maxi)
#     return maxi

# better approach 

# def max_product_subarray(arr):
#     maxi = -int(1e18)
#     for i in range(len(arr)):
#         product = 1
#         for j in range(i, len(arr)):
#             product = product * arr[j]
#             maxi = max(maxi, product)
#     return maxi


#  optimal approach
def max_product_subarray(arr):
    prefix = 1
    suffix = 1
    maxi = -int(1e18)
    for i in range(len(arr)):
        prefix *= arr[i]
        suffix *= arr[len(arr)-1 -i]
        maxi = max(maxi , max(prefix, suffix))
        if prefix == 0:
            prefix = 1
        if suffix ==0:
            suffix = 1
    return maxi 




arr = list(map(int, input().split()))
print(max_product_subarray(arr))  # Example usage