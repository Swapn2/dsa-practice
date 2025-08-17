def decimal_to_binary(n):
    result = ""
    while(n >1):
        if n%2 ==1:
            result = result + '1'
        else:
            result = result + '0'
        n = int(n/2)
    result = result +str(n)
    return result[::-1]


#  swap two numbers without using a third variable
# a = int(input())
# b = int(input())

# a = a^b
# b = a^b
# a = a^b
# print("a : ",a,"b : ",b)

#  check if the ith bit is set or not 
# method 1 

# N = int(input())
# i = int(input())

# if ((N&(1<<i))!= 0):
#     print("set bit ")
# else:
#     print("not set bit")

#  method 2 

# N = int(input())
# i = int(input())

# if (((N>>2)&1)==1):
#     print("set bit")
# else:
#     print("not set bit")

# set the ith bit
# N = int(input())
# i = int(input())
# print(decimal_to_binary(N))
# k = ((1<<i)|N)
# print(k)
# print(decimal_to_binary(k))


# clear a ith bit 

# N = int(input())
# i = int(input())

# x = ~(1<<i)
# k = N&x
# print(k)

#  toggle a bit 
# N = int(input())
# i = int(input())

# x = (1<<i)
# k = N^x
# print(k)
# print(decimal_to_binary(k))

# remove thee last set bit (right most set bit )

# N = int(input())
# print(decimal_to_binary(N))
# print(decimal_to_binary(N-1))

# print(N&(N-1))

#  checking if the number is a power of 2 

# N = int(input())

# print(decimal_to_binary(N))
# print(decimal_to_binary(N-1))
# print(decimal_to_binary(N&(N-1)))
# if (N&(N-1)==0):
#     print("yes")
# else:
#     print("No")


#  count the number of set bits 


# code 1
# N = int(input())
# def countsetbit(N):
#     count = 0
#     while(N>1):
#         if N%2 ==1:
#             count+=1
#         N = N//2
#     if N==1:
#         count+=1
#     return count

#  code 2
# N = int(input())
# def countsetbit(N):
#     count = 0
#     while(N>1):
#         count += (N&1) # if N&1 is 1, it means N is odd and has a set bit at the last position
#         N = N>>1
#     if N==1:
#         count+=1
#     return count
        
# print(countsetbit(N))

# method 2
N = int(input())
count =0
while(N!=0):
    count +=1
    N = N&(N-1)

print(count)

