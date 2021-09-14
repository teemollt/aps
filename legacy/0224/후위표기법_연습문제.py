# 입력 받은 중위 표기식에서 토큰을 읽는다.
# 토큰이 피연산자이면 토큰을 출력한다
# 토큰이 연산자(괄호포함)일 때, 이 토큰이 스택의 top에 저장되어 있는 연산자보다 우선순위가 높으면 스택에 push하고, 그렇지 않다면 스택 top의 연산자의 우선순위가 토큰의 우선순위보다 작을 때까지 스택에서 pop 한 후 토큰의 연산자를 push한다. 만약 top에 연산자가 없으면 push한다.
# 토큰이 오른쪽 괄호 ‘)’이면 스택 top에 왼쪽 괄호 ‘(‘가 올 때까지 스택에 pop
# 연산을 수행하고 pop 한 연산자를 출력한다. 
# 왼쪽 괄호를 만나면 pop만 하고 출력하지는 않는다.
# 중위 표기식에 더 읽을 것이 없다면 중지하고, 더 읽을 것이 있다면 1부터 다시 반복한다.
# 스택에 남아 있는 연산자를 모두 pop하여 출력한다.
# (6+5*(2-8)/2)
# 6 5 2 8  - * 2 / +
in_come_pri = {  "(": 3 ,"*": 2 , "/": 2 , "+": 1 , "-": 1 }
in_stack_pri = { "*": 2 , "/": 2 , "+": 1 , "-": 1, "(": 0 }
ex_str = input()
stack = list()
#문자열에서 토큰 하나씩 읽어오기
def post_ex(ex_str):
    for i in range(len(ex_str)):
        token = ex_str[i]
        #토큰이 연산자 일때, 우선순위 비교
        if token in {"(","*","/","+","-" }:

            #token은 들어오는 애, stack 의 top stack에 있는 애
            #token은 in_come_priority를 적용
            #top은 in_stack priority를 적용
            #숫자가 큰 것이 우선순위가 높은것
            # token이  stack의 top 보다 우선순위가 높으면, push
            if not stack or in_come_pri[token] > in_stack_pri[stack[-1]]:
                #token이 우선순위가 높음
                stack.append(token)
            else:
                # 우선순위가 낮으면, 나보다 낮은애가 top에 있을때 까지 pop 하고 push
                while stack and in_come_pri[token] <= in_stack_pri[stack[-1]]:
                    print(stack.pop(),end=" ")
                stack.append(token)

        elif token == ")": # 닫는 괄호이면
            #스택의 top이 여는 괄호일 때 까지, pop 하고, 출력
            #왼쪽 괄호가 나오면, pop
            while stack[-1] != "(":
                print(stack.pop(),end=" ")
            stack.pop()
        else: #숫자이면,
            #숫자는 출력하면 됨
            print(token,end=" ")

post_ex(ex_str)