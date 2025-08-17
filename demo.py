
def phonenumber(digits):
    if not digits:
        return []
    d = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }
    def backtrack(index , combo):
        if len(digits)==index:
            result.append(combo)
            return 
        for letter in d[digits[index]]:
            backtrack(index+1 , combo+letter)
    result = []
    backtrack(0,"")
    return result

st = input()
ans = phonenumber(st)
print(ans)

    








# from collections import deque


# def isvalid(s):
#     opencount = 0
#     closecount = 0 
#     for i in range(len(s)):
#         if s[i] == "(":
#             opencount+=1
#         if s[i] == ")":
#             closecount+=1
#         if closecount > opencount:
#             return False
#     return True


# def generate_parentesis(n):
#     queue = deque([("",0,0)])
#     result = []
#     while(queue):
#         curr , open_count , close_count = queue.popleft()
#         if open_count < n:
#             queue.append((curr+"(",open_count+1,close_count))
#         if close_count <n:
#             queue.append((curr+")",open_count,close_count+1))
#         if len(curr)==2*n:
#             if isvalid(curr):
#                 result.append(curr)
#                 continue
#     return result



# n = int(input())
# ans = generate_parentesis(n)
# print(ans)



#  optimal approach (backtracking)

# def generate_parenthesis(curr , open_count , close_count,result,n):
#     if len(curr) == 2*n:
#         result.append(curr)
#         return 
#     if open_count<n :
#         generate_parenthesis(curr+"(",open_count+1,close_count,result,n)
#     if close_count<open_count:
#         generate_parenthesis(curr+")",open_count,close_count+1,result,n)
    

# n = int(input())
# result = []
# generate_parenthesis("",0,0,result,n)
# print(result)





