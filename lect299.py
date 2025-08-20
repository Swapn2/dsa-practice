#  prefix , infix , postfix conversion


# Infix to postfix 
s = input()

def priority(op):
    if op == '+' or op == '-':
        return 1
    if op == '*' or op == '/':
        return 2
    if op == '^':
        return 3
    return 0


# def infixtopostfix(s):
#     i = 0 
#     st = []
#     ans = ""
#     while (i<len(s)):
#         if (((s[i] >= "a") and (s[i] <= "z")) or ((s[i] >= "A")and(s[i] <= "Z")) or ((s[i] >= "0")and (s[i] <= "9"))):
#             ans = ans + s[i]
#         elif s[i] == "(":
#             st.append(s[i])
#         elif s[i] == ")":
#             while(len(st)!=0 and st[-1] != "("):
#                 ans = ans + st[-1]
#                 st.pop()
#             st.pop()
#         else:
#             while(len(st) !=0 and priority(s[i]) <= priority(st[-1])):
#                 ans  = ans+st[-1]
#                 st.pop()
#             st.append(s[i])
#         i+=1
#     while(len(st)!=0):
#         ans = ans + st[-1]
#         st.pop()
#     return ans

# print(infixtopostfix(s))



#  infix to prefix 

# def infixtoprefix(str):
#     i = 0 
#     ans = ""
#     st = []
 
#     s = ""
#     for ch in str[::-1]:
#         if ch == "(":
#             s += ")"
#         elif ch == ")":
#             s += "("
#         else:
#             s += ch
#     print(s)

#     while(i < len(s)):
#         if (((s[i] >= "a") and (s[i]<= "z")) or ((s[i] >= "A") and (s[i] <="Z")) or ((s[i] >="0") and (s[i] <="9"))):
#             ans = ans + s[i]
#         elif (s[i] == "("):
#             st.append(s[i])
#         elif s[i] == ")":
#             while(len(st)!=0 and st[-1] != "(" ):
#                 ans = ans + st[-1]
#                 st.pop()
#             st.pop()
#         else:
#             if(s[i] == "^"):
#                 while(len(st)!= 0 and priority(s[i]) <= priority(st[-1])):
#                     ans = ans+st[-1]
#                     st.pop()
#             else:
#                 while(len(st)!= 0 and priority(s[i]) < priority(st[-1])):
#                     ans = ans + st[-1]
#                     st.pop()
#             st.append(s[i])
#         i+=1
#     print(st)
#     print(ans)
#     while(len(st)!=0):
#         ans = ans + st[-1]
#         st.pop()
#     return ans[::-1]


# print(infixtoprefix(s))

#  postfix to infix 

# def postfixtoinfix(s):
#     i = 0 
#     st = []
#     while(i<len(s)):
#         if (((s[i] >= "a") and (s[i]<= "z")) or ((s[i] >= "A") and (s[i] <="Z")) or ((s[i] >="0") and (s[i] <="9"))):
#             st.append(s[i])
#         else:
#             t1 = st[-1]
#             st.pop()
#             t2 = st[-1]
#             st.pop()
#             conn = "("+t2+s[i]+t1+")"
#             st.append(conn)
#         i+=1
#     return st[-1]

# print(postfixtoinfix(s))

#  prefix to infix 

# def prefixtoinfix(s):
#     i = len(s)-1
#     st = []
#     while (i>=0):
#         if (((s[i] >= "a") and (s[i]<= "z")) or ((s[i] >= "A") and (s[i] <="Z")) or ((s[i] >="0") and (s[i] <="9"))):
#             st.append(s[i])
#         else:
#             t1 = st[-1]
#             st.pop()
#             t2 = st[-1]
#             st.pop()
#             conn = "("+ t1+s[i] + t2+")"
#             st.append(conn)
#         i-=1
#     return st[-1]

# print(prefixtoinfix(s))



#  postfix to prefix 

# def postfixtoprefix(s):
#     i = 0
#     st = []
#     while(i<len(s)):
#         if (((s[i] >= "a") and (s[i]<= "z")) or ((s[i] >= "A") and (s[i] <="Z")) or ((s[i] >="0") and (s[i] <="9"))):
#             st.append(s[i])
#         else:
#             t1 = st[-1]
#             st.pop()
#             t2 = st[-1]
#             st.pop()
#             conn = s[i] + t2+t1
#             st.append(conn)
#         i+=1
#     return st[-1]

# print(postfixtoprefix(s))


#   prefix to postfix 

def prefixtopostfix(s):
    i = len(s)-1
    st = []
    while(i>=0):
        if (((s[i] >= "a") and (s[i]<= "z")) or ((s[i] >= "A") and (s[i] <="Z")) or ((s[i] >="0") and (s[i] <="9"))):
            st.append(s[i])
        else:
            t1 =st[-1]
            st.pop()
            t2 = st[-1]
            st.pop()
            conn = t1+t2+s[i]
            st.append(conn)
        i-=1
    return(st[-1])

print(prefixtopostfix(s))