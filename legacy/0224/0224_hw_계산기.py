import sys
sys.stdin = open("input (hw).txt")
t = 10
for tc in range(1, t+1):
    n = int(input())
    # 문자열 계산식 입력
    sen = input()
    # 담아줄 스택 만들
    stack = []
    num_stack = []
    # 연산자의 우선순위 담은 dict 만듬
    pri = {'*': 1, '+': 0}
    for i in range(n):
        x = sen[i]
        # sen[i]가 숫자라면
        if x not in pri.keys():
            # 넘버스택에 int로 추가
            num_stack.append(int(x))
            # x가 연산자일때
        else:
            # stack에 이미 들어있을때
            if stack:
                # top의 우선순위보다 높을때
                if pri[stack[-1]] < pri[x]:
                    # 그냥 stack에 추가
                    stack.append(x)
                # 같거나 낮을때
                else:
                    if stack[-1] == '+':
                        stack.append(x)
                    # numstack에서 숫자 두개 뽑아서 곱셈하고 다시 추가, stack에서 하나 pop하고 현재 x추가
                    else:
                        a = num_stack.pop()
                        b = num_stack.pop()
                        num_stack.append(a*b)
                        stack.pop()
                        stack.append(x)
            # 스택에 아무것도 없을때
            else:
                # 스택에 그냥 추가
                stack.append(x)

    # 반복문 끝나고 num스택에 남은 피연산자들을 stack에 남은 연산자대로 연산
    for i in range(len(stack)):
        if stack[-1] == '*':
            a = num_stack.pop()
            b = num_stack.pop()
            num_stack.append(a * b)
            stack.pop()
        else:
            a = num_stack.pop()
            b = num_stack.pop()
            num_stack.append(a + b)
            stack.pop()

    rst = num_stack[-1]

    print('#{} {}'.format(tc, rst))






