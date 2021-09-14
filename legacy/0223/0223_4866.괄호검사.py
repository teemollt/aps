# import sys
# sys.stdin = open("sample_input (4866).txt")

def ver(stack):
    for i in range(n):
        if code[i] == '(' or code[i] == '{':
            stack.append(code[i])
        if code[i] == ')' or code[i] == '}':
            if stack:
                if stack[-1] == '(' and code[i] == ')':
                    stack.pop()
                elif stack[-1] == '{' and code[i] == '}':
                    stack.pop()
                else:
                    return 0
            else:
                return 0
    if stack:
        return 0
    else:
        return 1

t = int(input())
for tc in range(1, t+1):
    code = input()
    n = len(code)
    # 스택
    stack = []
    print('#{} {}'.format(tc, ver(stack)))