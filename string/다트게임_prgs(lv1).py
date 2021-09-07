def solution(dartResult):
    tmp = ''
    rst = []
    b = {'S': 1, 'D': 2, 'T': 3}
    op = {'*': 2, '#': -1}
    for i in dartResult:
        if i.isdigit():
            tmp += i
        elif i in b:
            rst.append(int(tmp))
            tmp = ''
            rst[-1] **= b[i]
        else:
            if len(rst) == 1:
                rst[0] *= op[i]
            elif len(rst) > 1:
                if i == '*':
                    rst[-1] *= op[i]
                    rst[-2] *= op[i]
                else:
                    rst[-1] *= op[i]
    answer = sum(rst)
    return answer