def reverseParentheses(s):
    for i in range(len(s)):
        if s[i] == "(":
            start = i
            print(s[:start])
        if s[i] == ")":
            end = i
            print "*"
            print(end)
            return reverseParentheses(s[:start] + s[start + 1:end][::-1] + s[end + 1:])
    return s


test = 'a(b(cd)e)de'
print reverseParentheses(test)
