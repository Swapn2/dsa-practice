# # Extracting the digits from the number 

# def extract_digit(n):
#     digit = []
#     while n> 0:
#         rem = n%10 
#         n = int(n/10)
#         digit.append(rem)
#     # return digit[::-1]
#     digit.reverse()
#     return digit

    

# n = int(input())
# print(extract_digit(n))

# reverse the number 

# def reverse_number(n):
#     digit = []
#     while n> 0:
#         rem = n%10 
#         n = int(n/10)
#         digit.append(rem)
#     num = int(''.join(map(str,digit)))
#     return num


# n = int(input())
# print(reverse_number(n))

# # palindrame check 

# def palindrome(n):
#     temp = n
#     digit = []
#     while n> 0:
#         rem = n%10 
#         n = int(n/10)
#         digit.append(rem)
#     num = int(''.join(map(str,digit)))
#     if temp == num:
#         print("palindrome")
#     else:
#         print("not palindrome")
    

# palindrome alternative

# def palindrome(n):
#     if n< 0:
#         return False
#     if str(n) == str(n)[::-1]:
#         return True
#     else:
#         False

# n = int(input())
# palindrome(n)

# # Armstrong number check
import numpy as np 
# def armstrong(n):
#     sum = 0
#     temp =n
#     num = int(log10(n)) + 1
#     while n>0:
#         ld = n%10
#         n = int(n/10)
#         sum = sum + ld** num
#     # print(sum)
#     if sum == temp:
#         return True
#     else:
#         return False
    
# n = int(input())
# print(armstrong(n))

# # print all divisors of a number

# def printdivisor(n):
#     digit = []
#     for i in range(1 , int(np.sqrt(n))):
#         if n%i== 0:
#             digit.append(i)
#             if n/i != i:
#                 digit.append(int(n/i))
#     digit.sort()
#     return digit
# n = int(input())
# print(printdivisor(n))


# # check for 

# def prime(n):
#     count = 0 
#     for i in range(1, int(np.sqrt(n))):
#         if n%i == 0:
#             count +=1 
#             if(n%i != i):
#                 count+=1
#     if count == 2 :
#         return True
#     else:
#         return False
    
# n= int(input())
# print(prime(n))

def HCF(a,b):
    while (a> 0 and b> 0 ):
        if a>b :
            a = a%b
        else:
            b = b%a
    if a==0:
        return b
    else:
        return a
    
a = int(input())
b = int(input())

print(HCF(a,b))
