# #  4 sum question 
# #  brute force approach
#   1 0 -1 0 -2 2
#   i j  k l
def sum4(arr):
    n = len(arr)
    ans = []
    for i in range(n):
        for j in range(i+1,n):
            triplet = []
            for k in range(j+1,n):
                for l in range(k+1,n):
                    if arr[i] +arr[j]+arr[k] + arr[l] ==0:
                        triplet.append(arr[j])
                        triplet.append(arr[k])
                        triplet.append(arr[i])
                        triplet.append(arr[l])
                        triplet.sort()
                        if triplet not in ans:
                            ans.append(triplet)
    return ans


# #  better approach 

def sum4(arr):
    ans = []
    n = len(arr)
    i = 0 
    while i < n:
        j = i + 1
        while j < n:
            hash = {}  # Reset for every i, j pair
            k = j + 1
            while k < n:
                rem = -(arr[i] + arr[j] + arr[k])
                if rem in hash:
                    quad = [arr[i], arr[j], arr[k], rem]
                    quad.sort()
                    if quad not in ans:
                        ans.append(quad)
                hash[arr[k]] = 1  # Mark current as seen
                k += 1
            j += 1
        i += 1
    return ans


#  optimal approach 
def sum4(arr):
    arr.sort()
    n = len(arr)
    ans = []
    i = 0

    while i < n - 3:
        j = i + 1
        while j < n - 2:
            start = j + 1
            end = n - 1
            while start < end:
                total = arr[i] + arr[j] + arr[start] + arr[end]
                if total < 0:
                    start += 1
                elif total > 0:
                    end -= 1
                else:
                    quad = [arr[i], arr[j], arr[start], arr[end]]
                    if quad not in ans:
                        ans.append(quad)

                    # Skip duplicates for start and end
                    while start < end and arr[start] == arr[start + 1]:
                        start += 1
                    while start < end and arr[end] == arr[end - 1]:
                        end -= 1

                    start += 1
                    end -= 1
            # Skip duplicates for j
            while j < n - 2 and arr[j] == arr[j + 1]:
                j += 1
            j += 1
        # Skip duplicates for i
        while i < n - 3 and arr[i] == arr[i + 1]:
            i += 1
        i += 1

    return ans


            



arr = list(map(int, input().split()))
# print(sum4(arr))
print(sum4(arr))