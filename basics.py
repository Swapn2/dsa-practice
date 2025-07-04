# print("Hey Swapn!")
# print("Hey Swapn!")
# print("Hello\nSwapn")
# print("swapn" , end = '')
# print('Gupta')

# x = int(input())
# y = int(input())
# print("value of x :",x,"value of y :",y)
# print(x+y)


# # data types
# # int 
# x = int(10)
# print(x)
# # there is long , long long and int same in pyhton 
# x = 1000000000000000000000000000000000
# print(x)
# # float double
# x= float(10.3)
# y = float(5)
# print(x)
# print(y)

# # strings and getline same 
# x = input()
# print(x)
# # character 256 
# x = 'a'
# print(x)

# # *******************************************************
# # take input of the age and print you are adult or not 
# x = int(input())
# if x >= 18:
#     print('Adult')
# else:
#     print('Not Adult')

# # **************************************************************
# '''
# A school has following rules for grading systems:
# a. Below 25       - F
# b. 25 to 45       - E
# c. 46 to 50       - D
# d. 51 to 60       - C
# e. 61 to 80       - B
# f. Above 80       - A
# '''
# marks = int(input())
# if marks <25:
#     print("F")
# elif marks <45:
#     print("E")
# elif marks <50:
#     print('D')
# elif marks <= 60:
#     print("C")
# elif marks <80:
#     print('B')
# elif marks >=80:
#     print('A')
# # **************************************************************

# there are many ways to handle switch case scenarios
# # using Dictionary

# def day_of_week(day_number):
#     days = {
#         1: 'Monday',
#         2: "Tuesday",
#         3: 'Wednesday',
#         4: 'Thursady',
#         5: 'Friday',
#         6: 'Saturday',
#         7: 'Sunday',
#     }
#     return days[day_number]
# x = int(input())
# print(day_of_week(x))


# # using match 

# def days_of_week(day_number):
#     match day_number:
#         case 1:
#             return 'Monday'
#         case 2:
#             return 'Tuesday'
#         case 3:
#             return 'Wednesday'
#         case 4:
#             return 'Thursady'
#         case 5:
#             return 'Friday'
#         case 6:
#             return 'Saturday'
#         case 7:
#             return 'Sunday'
#         case _:
#             return 'Invalid day number'
# x = int(input())
# print(days_of_week(x))


# ****************************************************************

# basic of arrays 

# #  in python we dont have array Pre-fill list with dummy values, then overwrite
# x = [0]* 5 # Create a list with 50 zeros

# x[0] = int(input())
# x[1] = int(input())
# x[2] = int(input())
# x[3] = int(input())

# print(x)

# #  also we can use numpy to create arrays 
# # by using np array 

# import numpy as np 
# x = np.zeros(4, dtype=int)  # Create a NumPy array with one element initialized to 4])
# x[0] = int(input())
# x[1] = int(input())  # if input is 2.2 it would raise error so be careful 
# #  for safe side we can use int(float(input()))
# x[2] = int(input())
# x[3] = int(input())

# print(x)
# print(x[3]+x[1])


# # 2D array 
# x = np.zeros((3,4),dtype = int)
# x[0][0] = 43
# x[2][3] = 12 
# print(x)


# # strings 
# in cpp string is mutable but not in python 
# x = 'swapn'
# print(x[1])
# print(len(x))
# print(x[len(x)-1])


# # for loop in python

# for i in range(5):
#     print('swapn')

# # while loop 

# i = 1
# while i<5:
#     print('swapn')
#     i += 1
# # do is not available in python so 
# while True:
#     x = int(input("Enter a positive number: "))
#     if x > 0:
#         break
# print("You entered:", x)

# Functions 

# # void
# def name():
#     print('swapn')

# name()

# # # parameterized function
# def add(x,y):
#     return x+y
# x = int(input())
# y = int(input())
# print(add(x,y))



# def dosomething(num):  # pass by value 
#     print(num)
#     num += 10 
#     print(num)
#     num += 10
#     print(num)

# num = int(30)
# dosomething(num)
# print(num)

# so for pass my Refrence should be belonging to :list, dict, object data types 

# def dosomething(num):  # pass the whole list
#     print(num[0])
#     num[0] += 10
#     print(num[0])
#     num[0] += 10
#     print(num[0])

# num = [30]
# dosomething(num)
# print(num[0])  
