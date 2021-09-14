import sys
sys.stdin = open("sample_input (4874).txt")

def sol(a):
    global stack
    c = ['+', '*', '-', '/', '.']
    if a not in c:
        stack.append(int(a))
    else:
        if a == '.':
            if len(stack):
                return stack[0]
            else:
                return 'error'
        else:
            if len(stack) < 2:
                return 'error'
            else:
                num1 = stack.pop()
                num2 = stack.pop()
                if a == '+':
                    stack.append(num2 + num1)
                elif a == '*':
                    stack.append(num2 * num1)
                elif a == '-':
                    stack.append(num2 - num1)
                elif a == '/':
                    stack.append(num2 // num1)
t = int(input())
for tc in range(1, t+1):
    f = list(input().split())
    stack = []
    # 반복
    for i in f:
        rst = sol(i)
        if rst:
            break
    print('#{} {}'.format(tc, rst))
