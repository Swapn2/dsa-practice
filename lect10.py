# # find factorial of a number using recursion 

# def factorial(n):
#     if n == 0:
#         return 1
#     return n * factorial(n-1)

# n = int(input())
# print(factorial(n))

# # sum of first n number 

# def sum_n(n):
#     if n== 0:
#         return 0
#     return n + sum_n(n-1)

# n = int(input())
# print(sum_n(n))

# # reverse an array using recursion

# def reverse_array(i , arr):
#     if i >= len(arr)//2:
#         return 
#     arr[i], arr[len(arr) - i - 1] = arr[len(arr) - i - 1], arr[i]
#     reverse_array(i+1 , arr)

# n = int(input())
# x = [0] *n
# for i in range(n):
#     x[i] = int(input())
# # print(x)
# reverse_array(0,x)
# print(x)

# reverse string using recursion

# def reverse_string(i,s):
#     if i >= len(s)//2:
#         return 
#     if s[i] != s[len(s) - i-1]:
#         return False
#     reverse_string(i+1,s)
#     return True

# s = input()
# print(reverse_string(0,s))

