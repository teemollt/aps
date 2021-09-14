def solve(target):
    #여는 괄호가 나오면, stack에 넣고, 닫는 괄호가 나오면
    #stack에서 pop해서 짝 맞는지 확인
    stack = list()
    for i in range(len(target)):
        if target[i] == "(" or target[i] == "{":
            stack.append(target[i])
        elif target[i] == ")" or target[i] == "}":
            #닫는 괄호이면, 스택이 비어있으면 짝이 안맞는거다.
            if not stack:
               return 0
            tmp = stack.pop()
            #잘못 된 쌍
            if target[i] == ")" and tmp != "(":
                return 0
            elif target[i] == "}" and tmp != "{":
                return 0
    #모든 문자열을 다 확인했는데, 스택에 뭔가 남아있으면, 잘못된거
    if stack:
        return 0
    #스택에서 요소를 뺄때 문제없었고, 남아잇는 것이 없으면, 쌍이 맞는것
    return 1

T = int(input())
for tc in range(1,T+1):
    target= input()
    result = solve(target)
    print("#{} {}".format(tc,result))