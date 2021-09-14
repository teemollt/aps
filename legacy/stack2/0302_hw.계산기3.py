import sys
sys.stdin = open("input (3).txt")
t = 10
for tc in range(1, t+1):
    n = int(input())
    sen = input()
    num = []
    cal = []
    c = ['(', ')', '+', '*']
    for i in sen:
        # 숫자면 숫자스택에 쌓기
        if i not in c:
            num.append(int(i))
        else:
            # 일단 비어있으면 무조건 스택에 넣기
            if not cal:
                cal.append(i)
            # 아니면 무엇인지에 따라..
            # +면
            elif i == '+':
                # cal의 top이 뭐냐에 따라..
                # + 나 (면 그냥 쌓기
                if cal[-1] == '+' or cal[-1] == '(':
                    cal.append(i)
                    # *면 * 계산해주고 쌓기
                elif cal[-1] == '*':
                    while cal[-1] == '*':
                        cal.pop()
                        num.append(num.pop() * num.pop())
                    cal.append(i)
            # *이면
            elif i == '*':
                cal.append(i)
            # ( 이면
            elif i == '(':
                cal.append(i)
            # ) 이면
            elif i == ')':
                # ( 나올때까지 계산 다하기
                while cal[-1] != '(':
                    if cal[-1] == '*':
                        cal.pop()
                        num.append(num.pop() * num.pop())
                    elif cal[-1] == '+':
                        cal.pop()
                        num.append(num.pop() + num.pop())
                # 괄호 안 계산 끝나고 나면 ( 팝해주기
                cal.pop()

        # 남은거 더해주기

    while cal:
        if cal[-1] == '*':
            cal.pop()
            num.append(num.pop() * num.pop())
        elif cal[-1] == '+':
            cal.pop()
            num.append(num.pop() + num.pop())

        # 마지막에 남은 숫자 반환
    rst = num[-1]

    print('#{} {}'.format(tc, rst))

