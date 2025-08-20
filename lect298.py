#  balanced paranthesis

s = input()

def balanced(s):
    st = []
    for i in range(len(s)):
        if s[i] == "(" or s[i] == "[" or s[i] == "{":
            st.append(s[i])
        else:
            if len(st)==0: return False
            x = st.pop()
            if s[i] == ")" and x == "(":
                continue
            elif s[i] == "]" and x == "[":
                continue
            elif s[i] == "}" and x == "{":
                continue
            else:
                return False
    return True

print(balanced(s))

