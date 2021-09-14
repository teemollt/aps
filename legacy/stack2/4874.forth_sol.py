# 후위표기법으로 표시된 data 읽어서
# 연산의 결과를 반환하는 함수
# 잘못된 data라면, error
def solve(data):

    stack = []
    for i in range(len(data)):
        if data[i] not in oper:
            staack.append(int(data[i]))
        elif data[i] in oper and data[i] != '.':
            # 사직연산 하면됨
            # 스택에서 2개 꺼내서 연산
            if len(stack) < 2: # 피연산자 개수가 모자람
                return 'error'
            else:
                v1 = stack.pop()
                v2 = stack.pop()
    pass


t = int(input())