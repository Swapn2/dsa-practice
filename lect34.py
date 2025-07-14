#  pascal triangle :
# 1. given R and C find the element at that location 

def nCr(r,c):
    r = r-1
    c= c-1
    res = 1
    for i in range(c):
        res = res*(r-i)
        res = res/(i+1)
    return int(res)


# 2. print Nth row of the pascal triangle 

def Nthrow(r):
    ans = 1
    for i in range(1,r+1):
        print(int(ans) ,end =' ')
        ans = ans*((r-i)/i)
    # print(int(ans))
    print('\n')


# # 3. given row print entire pascal Triangle brute approach 
# def pascaltriangle(r):
#     ans = []
#     for i in range(1,r+1):
#         temp = []
#         for j in range(1,i+1):
#             temp.append(nCr(i,j))
#         ans.append(temp)
#     return ans


# optimal approach 

def pascaltriangle(r):
    for i in range(1,r+1):
        Nthrow(i)

            




r = int(input())
c = int(input())
print(nCr(r,c))
Nthrow(r)
pascaltriangle(r)
# print(pascaltriangle(r))