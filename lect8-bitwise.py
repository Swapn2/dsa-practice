# XOR of a given number in a ggiven range 

#  Q1. given an number N find the XOR all from ! to N

# N = int(input())
# xor = 0
# for i in range(1, N+1):
#     xor = xor^i
# print(xor)

# trick 2

# def xorfunction(N):
#     ans = 0
#     if N%4 == 1 : ans =1
#     elif N%4 ==2: ans = N+1
#     elif N%4 == 3 : ans = 0
#     else:
#         ans = N
#     return ans 

# print(xorfunction(N))

#  Q2. xor from L to R range()
# l = int(input())
# r = int(input())
# def xorLR(l,r):
#     xor1 = xorfunction(l-1)
#     print(xor1)
#     xor2 = xorfunction(r)
#     print(xor2)
#     ans = xor1^xor2
#     return ans
# print(xorLR(l,r))